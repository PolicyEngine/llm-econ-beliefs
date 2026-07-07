import pytest

from llm_econ_beliefs import (
    build_claude_command,
    build_litellm_belief_tool,
    build_openai_chat_payload,
    build_openai_response_payload,
    resolve_anthropic_model_name,
    resolve_litellm_model_name,
    run_anthropic_prompt_logged,
)
from llm_econ_beliefs.providers import (
    run_litellm_prompt_logged,
)


def test_build_claude_command_includes_model_and_schema():
    command = build_claude_command("hello", model_name="sonnet")

    assert command[0].endswith("claude")
    assert "--model" in command
    assert "sonnet" in command
    assert "--json-schema" in command
    assert command[-1] == "hello"


def test_build_openai_chat_payload_includes_n_and_schema():
    payload = build_openai_chat_payload(
        "hello",
        model_name="gpt-5.4-mini",
        n=4,
        temperature=0.8,
    )

    assert payload["model"] == "gpt-5.4-mini"
    assert payload["n"] == 4
    assert payload["temperature"] == 0.8
    assert payload["response_format"]["type"] == "json_schema"
    assert payload["messages"][-1]["content"] == "hello"
    assert payload["messages"][0]["content"] == (
        "Follow the user's instructions exactly and return only the final answer."
    )


def test_build_openai_chat_payload_rejects_n_above_api_limit():
    with pytest.raises(ValueError, match="n must be <= 8"):
        build_openai_chat_payload(
            "hello",
            model_name="gpt-5.4-mini",
            n=9,
        )


def test_build_openai_response_payload_with_full_tools():
    payload = build_openai_response_payload(
        "hello",
        model_name="gpt-5.4-mini",
        tool_regime="full",
    )

    assert payload["model"] == "gpt-5.4-mini"
    assert payload["tool_choice"] == "auto"
    assert payload["tools"][0]["type"] == "web_search"
    assert payload["tools"][1]["type"] == "code_interpreter"
    assert payload["include"] == ["web_search_call.action.sources"]


def test_resolve_litellm_model_name_supports_policybench_aliases():
    assert resolve_litellm_model_name("claude-haiku-4.5") == "claude-haiku-4-5-20251001"
    assert resolve_litellm_model_name("gemini-3-flash-preview") == "gemini/gemini-3-flash-preview"
    assert resolve_litellm_model_name("custom-model") == "custom-model"


def test_build_litellm_belief_tool_uses_schema():
    tool = build_litellm_belief_tool()

    assert tool["type"] == "function"
    assert tool["function"]["name"] == "submit_belief"
    assert tool["function"]["parameters"]["required"] == [
        "interpretation",
        "point_estimate",
        "quantiles",
        "citations",
        "reasoning_summary",
    ]


class _FakeLiteLLM:
    def __init__(self, response):
        self._response = response

    def completion(self, **kwargs):
        self.kwargs = kwargs
        return self._response

    @staticmethod
    def completion_cost(*, completion_response):
        return 0.123


class _FakeLiteLLMCostFromTicks(_FakeLiteLLM):
    @staticmethod
    def completion_cost(*, completion_response):
        raise RuntimeError("no direct cost")


class _FakeFunction:
    def __init__(self, arguments):
        self.arguments = arguments


class _FakeToolCall:
    def __init__(self, arguments):
        self.function = _FakeFunction(arguments)


class _FakeMessage:
    def __init__(self, *, content=None, tool_calls=None):
        self.content = content
        self.tool_calls = tool_calls


class _FakeChoice:
    def __init__(self, message):
        self.message = message


class _FakeUsage:
    def __init__(self, payload):
        self._payload = payload

    def model_dump(self):
        return dict(self._payload)


class _FakeResponse:
    def __init__(self, *, message, usage, request_id="resp_1"):
        self.id = request_id
        self.choices = [_FakeChoice(message)]
        self.usage = _FakeUsage(usage)


def test_run_litellm_prompt_logged_reads_json_object(monkeypatch):
    response = _FakeResponse(
        message=_FakeMessage(content='{"point_estimate": 0.5}'),
        usage={"prompt_tokens": 10, "completion_tokens": 20, "total_tokens": 30},
    )
    fake_litellm = _FakeLiteLLM(response)
    monkeypatch.setattr(
        "llm_econ_beliefs.providers._import_litellm",
        lambda: fake_litellm,
    )

    result = run_litellm_prompt_logged("hello", model_name="gemini-3-flash-preview")

    assert result.outputs == ['{"point_estimate": 0.5}']
    assert result.request_id == "resp_1"
    assert result.usage["litellm_cost_usd"] == 0.123
    assert fake_litellm.kwargs["response_format"] == {"type": "json_object"}


def test_run_litellm_prompt_logged_reads_function_call(monkeypatch):
    response = _FakeResponse(
        message=_FakeMessage(
            tool_calls=[_FakeToolCall('{"point_estimate": 0.5, "quantiles": {}}')]
        ),
        usage={"prompt_tokens": 10, "completion_tokens": 20, "total_tokens": 30},
    )
    fake_litellm = _FakeLiteLLM(response)
    monkeypatch.setattr(
        "llm_econ_beliefs.providers._import_litellm",
        lambda: fake_litellm,
    )

    result = run_litellm_prompt_logged("hello", model_name="claude-haiku-4.5")

    assert result.outputs == ['{"point_estimate": 0.5, "quantiles": {}}']
    assert result.request_id == "resp_1"
    assert fake_litellm.kwargs["tool_choice"]["function"]["name"] == "submit_belief"


def test_run_litellm_prompt_logged_falls_back_to_cost_ticks(monkeypatch):
    response = _FakeResponse(
        message=_FakeMessage(content='{"point_estimate": 0.5}'),
        usage={
            "prompt_tokens": 10,
            "completion_tokens": 20,
            "total_tokens": 30,
            "cost_in_usd_ticks": 2164000,
        },
    )
    fake_litellm = _FakeLiteLLMCostFromTicks(response)
    monkeypatch.setattr(
        "llm_econ_beliefs.providers._import_litellm",
        lambda: fake_litellm,
    )

    result = run_litellm_prompt_logged("hello", model_name="gemini-3-flash-preview")

    assert result.usage["litellm_cost_usd"] == pytest.approx(0.0002164)


class _FakeAnthropicUsage:
    def __init__(self, input_tokens=700, output_tokens=350, cache_read=0):
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.cache_creation_input_tokens = 0
        self.cache_read_input_tokens = cache_read


class _FakeAnthropicBlock:
    def __init__(self, type_, text=None):
        self.type = type_
        self.text = text


class _FakeAnthropicStopDetails:
    def __init__(self, explanation):
        self.explanation = explanation


class _FakeAnthropicMessage:
    def __init__(
        self,
        *,
        stop_reason="end_turn",
        content=None,
        stop_details=None,
        usage=None,
    ):
        self.stop_reason = stop_reason
        self.content = content if content is not None else [
            _FakeAnthropicBlock("text", '{"point_estimate": 0.5}')
        ]
        self.stop_details = stop_details
        self.usage = usage or _FakeAnthropicUsage()
        self.id = "msg_1"


class _FakeAnthropicStream:
    def __init__(self, message):
        self._message = message

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def get_final_message(self):
        return self._message


class _FakeAnthropicMessages:
    def __init__(self, message):
        self._message = message
        self.kwargs = None

    def stream(self, **kwargs):
        self.kwargs = kwargs
        return _FakeAnthropicStream(self._message)


class _FakeAnthropicClient:
    def __init__(self, message):
        self.messages = _FakeAnthropicMessages(message)


def test_resolve_anthropic_model_name_maps_panel_aliases():
    assert resolve_anthropic_model_name("claude-opus-4.8") == "claude-opus-4-8"
    assert resolve_anthropic_model_name("claude-fable-5") == "claude-fable-5"
    assert resolve_anthropic_model_name("claude-sonnet-5") == "claude-sonnet-5"


def test_resolve_litellm_model_name_supports_july_2026_additions():
    assert resolve_litellm_model_name("grok-4.3") == "xai/grok-4.3"
    assert resolve_litellm_model_name("gemini-3.5-flash") == "gemini/gemini-3.5-flash"


def test_run_anthropic_prompt_logged_uses_structured_output_without_sampling_params():
    client = _FakeAnthropicClient(_FakeAnthropicMessage())

    result = run_anthropic_prompt_logged(
        "hello",
        model_name="claude-opus-4.8",
        client=client,
    )

    kwargs = client.messages.kwargs
    assert kwargs["model"] == "claude-opus-4-8"
    assert "temperature" not in kwargs
    assert "top_p" not in kwargs
    assert "thinking" not in kwargs
    assert kwargs["output_config"]["format"]["type"] == "json_schema"
    assert kwargs["messages"] == [{"role": "user", "content": "hello"}]
    assert result.outputs == ['{"point_estimate": 0.5}']
    assert result.request_id == "msg_1"
    assert result.usage["input_tokens"] == 700
    assert result.usage["output_tokens"] == 350
    assert result.usage["total_tokens"] == 1050


def test_run_anthropic_prompt_logged_reads_text_after_thinking_blocks():
    message = _FakeAnthropicMessage(
        content=[
            _FakeAnthropicBlock("thinking"),
            _FakeAnthropicBlock("text", '{"point_estimate": 0.9}'),
        ]
    )
    client = _FakeAnthropicClient(message)

    result = run_anthropic_prompt_logged(
        "hello",
        model_name="claude-fable-5",
        client=client,
    )

    assert result.outputs == ['{"point_estimate": 0.9}']


def test_run_anthropic_prompt_logged_raises_on_refusal():
    message = _FakeAnthropicMessage(
        stop_reason="refusal",
        stop_details=_FakeAnthropicStopDetails("declined by policy"),
    )
    client = _FakeAnthropicClient(message)

    with pytest.raises(RuntimeError, match="declined by policy"):
        run_anthropic_prompt_logged(
            "hello",
            model_name="claude-fable-5",
            client=client,
        )


def test_run_anthropic_prompt_logged_raises_on_truncation():
    message = _FakeAnthropicMessage(stop_reason="max_tokens")
    client = _FakeAnthropicClient(message)

    with pytest.raises(RuntimeError, match="truncated"):
        run_anthropic_prompt_logged(
            "hello",
            model_name="claude-sonnet-5",
            client=client,
        )


def test_run_litellm_prompt_logged_uses_model_specific_completion_cap(monkeypatch):
    response = _FakeResponse(
        message=_FakeMessage(
            tool_calls=[_FakeToolCall('{"point_estimate": 0.5, "quantiles": {}}')]
        ),
        usage={"prompt_tokens": 10, "completion_tokens": 20, "total_tokens": 30},
    )
    fake_litellm = _FakeLiteLLM(response)
    monkeypatch.setattr(
        "llm_econ_beliefs.providers._import_litellm",
        lambda: fake_litellm,
    )

    run_litellm_prompt_logged("hello", model_name="grok-4.3")

    assert fake_litellm.kwargs["max_tokens"] == 4000
    assert fake_litellm.kwargs["model"] == "xai/grok-4.3"


def test_run_openai_prompt_batch_logged_default_cap_is_model_specific(monkeypatch):
    captured = {}

    class _StopAfterPayload(Exception):
        pass

    def fake_build_payload(prompt, *, model_name, json_schema, n, temperature, max_completion_tokens):
        captured[model_name] = max_completion_tokens
        raise _StopAfterPayload

    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setattr(
        "llm_econ_beliefs.providers.build_openai_chat_payload", fake_build_payload
    )

    from llm_econ_beliefs.providers import run_openai_prompt_batch_logged

    for model_name in ("gpt-5.5", "gpt-5.4-mini"):
        with pytest.raises(_StopAfterPayload):
            run_openai_prompt_batch_logged("hello", model_name=model_name, n=1)
    assert captured["gpt-5.5"] == 8000
    assert captured["gpt-5.4-mini"] == 1200
