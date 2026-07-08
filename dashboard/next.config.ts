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
  // Every page is statically generated at build time; results/ and
  // tables/ are read only during the build, so nothing needs runtime
  // file tracing.
  ...(process.env.VERCEL
    ? {}
    : { outputFileTracingRoot: path.join(__dirname, "..") }),
};

export default nextConfig;
