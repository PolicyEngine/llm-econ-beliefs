"use client";

import { useEffect } from "react";

const STORAGE_KEY = "eba-theme";

/**
 * Re-applies the persisted theme after hydration. The inline pre-paint
 * script in the root layout handles the fast path; this covers the case
 * where React falls back to a full client render (which recreates the
 * script tag without executing it) and drops the class.
 */
export function ThemeInit() {
  useEffect(() => {
    try {
      const stored = window.localStorage.getItem(STORAGE_KEY);
      const dark = stored
        ? stored === "dark"
        : window.matchMedia("(prefers-color-scheme: dark)").matches;
      document.documentElement.classList.toggle("dark", dark);
    } catch {
      /* private browsing */
    }
  }, []);

  return null;
}
