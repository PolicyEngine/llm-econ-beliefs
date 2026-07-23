"use client";

import type { ReactNode } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";

/** Section links with the current section highlighted. Client-side so the
 *  active state follows navigation; `usePathname` is basePath-free, matching
 *  the hrefs. */
export function NavLinks({
  items,
}: {
  items: ReadonlyArray<{ href: string; label: string }>;
}): ReactNode {
  const pathname = usePathname();
  return (
    <>
      {items.map((item) => {
        const active =
          item.href === "/"
            ? pathname === "/"
            : pathname === item.href || pathname.startsWith(`${item.href}/`);
        return (
          <Link
            key={item.href}
            href={item.href}
            aria-current={active ? "page" : undefined}
            className={`rounded-md px-2.5 py-1.5 text-sm transition hover:bg-[color:var(--muted)]${
              active ? " font-medium" : ""
            }`}
            style={
              active
                ? { background: "var(--muted)", color: "var(--foreground)" }
                : { color: "var(--muted-foreground)" }
            }
          >
            {item.label}
          </Link>
        );
      })}
    </>
  );
}
