"""Canonical provider tags stored in run and request artifacts."""

from __future__ import annotations


CLAUDE_CLI_PROVIDER = "claude_cli"
OPENAI_CHAT_COMPLETIONS_PROVIDER = "openai_chat_completions"
OPENAI_RESPONSES_PROVIDER = "openai_responses"
LITELLM_COMPLETION_PROVIDER = "litellm_completion"
ANTHROPIC_PROVIDER = "anthropic"

PROVIDER_TAG_BY_RUNNER = {
    "openai": OPENAI_CHAT_COMPLETIONS_PROVIDER,
    "anthropic": ANTHROPIC_PROVIDER,
    "litellm": LITELLM_COMPLETION_PROVIDER,
}


def provider_tag_for_runner(provider: str) -> str:
    """Translate a runner/provider key to its canonical artifact tag."""
    try:
        return PROVIDER_TAG_BY_RUNNER[provider]
    except KeyError as exc:
        raise ValueError(f"Unknown provider runner: {provider}") from exc
