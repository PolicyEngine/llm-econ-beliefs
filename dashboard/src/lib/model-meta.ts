export type ProviderKey =
  | "anthropic"
  | "google"
  | "openai"
  | "xai"
  | "independent";

interface ClientModelMetadata {
  modelId: string;
  displayLabel: string;
  organization: string;
}

const CLIENT_MODEL_REGISTRY = parseClientModelRegistry(
  process.env.NEXT_PUBLIC_MODEL_REGISTRY_JSON,
);
const CLIENT_MODEL_BY_ID = new Map(
  CLIENT_MODEL_REGISTRY.map((model) => [model.modelId, model]),
);
const MODEL_ORDER_INDEX = new Map(
  CLIENT_MODEL_REGISTRY.map((model, index) => [model.modelId, index]),
);

function parseClientModelRegistry(raw: string | undefined): ClientModelMetadata[] {
  if (!raw) return [];
  const parsed: unknown = JSON.parse(raw);
  if (!Array.isArray(parsed)) {
    throw new Error("NEXT_PUBLIC_MODEL_REGISTRY_JSON must be an array");
  }
  return parsed.map((value) => {
    if (
      typeof value !== "object" ||
      value === null ||
      !("modelId" in value) ||
      !("displayLabel" in value) ||
      !("organization" in value) ||
      typeof value.modelId !== "string" ||
      typeof value.displayLabel !== "string" ||
      typeof value.organization !== "string"
    ) {
      throw new Error("NEXT_PUBLIC_MODEL_REGISTRY_JSON has an invalid row");
    }
    return {
      modelId: value.modelId,
      displayLabel: value.displayLabel,
      organization: value.organization,
    };
  });
}

export function getProviderForModel(model: string): ProviderKey | null {
  const organization = CLIENT_MODEL_BY_ID.get(model)?.organization;
  if (!organization) return null;
  if (
    organization === "anthropic" ||
    organization === "google" ||
    organization === "openai" ||
    organization === "xai"
  ) {
    return organization;
  }
  return "independent";
}

export function getModelLabel(model: string): string {
  return CLIENT_MODEL_BY_ID.get(model)?.displayLabel ?? model;
}

export function compareModelNames(left: string, right: string): number {
  const leftIndex = MODEL_ORDER_INDEX.get(left) ?? -1;
  const rightIndex = MODEL_ORDER_INDEX.get(right) ?? -1;

  if (leftIndex >= 0 || rightIndex >= 0) {
    if (leftIndex === -1) return 1;
    if (rightIndex === -1) return -1;
    return leftIndex - rightIndex;
  }

  return left.localeCompare(right);
}
