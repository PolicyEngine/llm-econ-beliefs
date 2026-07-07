import type { Metadata } from "next";
import { Inter, JetBrains_Mono } from "next/font/google";
import Script from "next/script";
import "./globals.css";

// Matches the GA4 property used by policyengine-app-v2/website so
// page_view events from this multizone land in the same account as the
// rest of policyengine.org traffic.
const GA_MEASUREMENT_ID = "G-2YHG89FY0N";

const inter = Inter({
  variable: "--font-sans",
  subsets: ["latin"],
  display: "swap",
});

const jetbrains = JetBrains_Mono({
  variable: "--font-mono",
  subsets: ["latin"],
  weight: ["400", "500", "600"],
  display: "swap",
});

const basePath = process.env.NEXT_PUBLIC_BASE_PATH ?? "";

export const metadata: Metadata = {
  metadataBase: new URL("https://policyengine.org"),
  title: "AI beliefs · PolicyEngine",
  description:
    "How 17 frontier language models answer when asked for their beliefs about economic elasticities: point estimates, uncertainty bands, and run-level responses.",
  alternates: { canonical: basePath || "/" },
  openGraph: {
    title: "AI beliefs about economic parameters",
    description:
      "Elicited beliefs from 17 frontier models on 26 economic quantities, with pooled, REML, and Bayesian uncertainty bands.",
    url: basePath || "/",
    siteName: "PolicyEngine",
  },
  icons: { icon: `${basePath}/favicon.svg` },
};

const themeInitScript = `(function(){try{var t=localStorage.getItem("eba-theme");var d=t?t==="dark":window.matchMedia("(prefers-color-scheme: dark)").matches;if(d)document.documentElement.classList.add("dark");}catch(e){}})();`;

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="en"
      suppressHydrationWarning
      className={`${inter.variable} ${jetbrains.variable} h-full antialiased`}
    >
      <head>
        <Script
          src={`https://www.googletagmanager.com/gtag/js?id=${GA_MEASUREMENT_ID}`}
          strategy="afterInteractive"
        />
        <Script id="google-analytics" strategy="afterInteractive">
          {`
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            window.gtag = gtag;
            gtag('js', new Date());
            gtag('config', '${GA_MEASUREMENT_ID}');
          `}
        </Script>
      </head>
      <body className="min-h-full flex flex-col">
        <script dangerouslySetInnerHTML={{ __html: themeInitScript }} />
        <div className="flex-1">{children}</div>
        <footer
          className="border-t px-5 py-4 text-xs"
          style={{
            borderColor: "var(--border)",
            color: "var(--muted-foreground)",
          }}
        >
          <div className="mx-auto flex max-w-[1400px] flex-wrap items-center justify-between gap-2">
            <span>
              A{" "}
              <a
                href="https://policyengine.org"
                className="font-medium underline-offset-2 hover:underline"
                style={{ color: "var(--primary)" }}
              >
                PolicyEngine
              </a>{" "}
              research project
            </span>
            <span className="flex items-center gap-4">
              <a
                href="https://github.com/PolicyEngine/llm-econ-beliefs"
                className="underline-offset-2 hover:underline"
              >
                Code and data
              </a>
              <span>
                Elicited April and July 2026 · 17 models · v4 prompts
              </span>
            </span>
          </div>
        </footer>
      </body>
    </html>
  );
}
