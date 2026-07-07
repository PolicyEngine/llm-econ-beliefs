"use client";

import { useEffect, useState } from "react";

const STORAGE_KEY = "eba-theme";

function applyTheme(dark: boolean) {
  document.documentElement.classList.toggle("dark", dark);
}

export function ThemeToggle() {
  const [dark, setDark] = useState<boolean | null>(null);

  useEffect(() => {
    setDark(document.documentElement.classList.contains("dark"));
  }, []);

  function toggle() {
    const next = !(dark ?? false);
    setDark(next);
    applyTheme(next);
    try {
      window.localStorage.setItem(STORAGE_KEY, next ? "dark" : "light");
    } catch {
      /* private browsing */
    }
  }

  return (
    <button
      type="button"
      onClick={toggle}
      aria-label={dark ? "Switch to light mode" : "Switch to dark mode"}
      title={dark ? "Switch to light mode" : "Switch to dark mode"}
      className="flex h-8 w-8 items-center justify-center rounded-md border transition-colors hover:bg-[color:var(--muted)]"
      style={{ borderColor: "var(--border)", color: "var(--muted-foreground)" }}
    >
      {dark ? (
        <svg width="14" height="14" viewBox="0 0 16 16" fill="none" aria-hidden="true">
          <circle cx="8" cy="8" r="3.5" fill="currentColor" />
          {[0, 45, 90, 135, 180, 225, 270, 315].map((angle) => (
            <line
              key={angle}
              x1="8"
              y1="1"
              x2="8"
              y2="3"
              stroke="currentColor"
              strokeWidth="1.4"
              strokeLinecap="round"
              transform={`rotate(${angle} 8 8)`}
            />
          ))}
        </svg>
      ) : (
        <svg width="14" height="14" viewBox="0 0 16 16" fill="none" aria-hidden="true">
          <path
            d="M13.5 9.5A5.7 5.7 0 0 1 6.5 2.5a5.7 5.7 0 1 0 7 7Z"
            stroke="currentColor"
            strokeWidth="1.4"
            strokeLinejoin="round"
            fill="none"
          />
        </svg>
      )}
    </button>
  );
}
