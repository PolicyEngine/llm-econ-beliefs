import path from "node:path";
import type { NextConfig } from "next";

// Served as a policyengine.org zone: the host app rewrites
// /ai-beliefs/:path* to this deployment, so every route and asset lives
// under the base path.
const basePath = "/ai-beliefs";

const nextConfig: NextConfig = {
  basePath,
  env: {
    NEXT_PUBLIC_BASE_PATH: basePath,
  },
  // Runtime fs reads of the results artifacts are invisible to Next's
  // static tracer, so include them in the serverless bundle explicitly.
  outputFileTracingIncludes: {
    "/*": ["./results/**/*"],
  },
  ...(process.env.VERCEL
    ? {}
    : { outputFileTracingRoot: path.join(__dirname, "..") }),
};

export default nextConfig;
