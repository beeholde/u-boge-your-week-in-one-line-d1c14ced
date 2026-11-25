#!/usr/bin/env python3
"""Your Week in One Line — writes our week's one-liner to /output/entry.txt.

The line sums up the entrant's own week: two perfect scores that paid
nothing (a 1,000,000-point Sokoban solve landing 64th, a 1000/1000
hidden-spec CLI landing outside the top 200), and the one moment that did
pay off in applause — the Chopin history video, approved by its audience.
Standard library only; no network, no input files.
"""
import os

LINE = "Perfect score, 64th place, zero dollars \u2014 the week's only applause came from Chopin."

def main():
    text = LINE
    if not 1 <= len(text) <= 100:
        raise SystemExit("line must be 1-100 characters, got %d" % len(text))
    if text.strip() != text or "\n" in text or "\r" in text:
        raise SystemExit("line must be a single line with no surrounding whitespace")
    text.encode("utf-8")  # gate requires UTF-8 text
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back and confirm the gate sees exactly what we wrote: no
    # trailing newline, no re-encoding surprise, still 1-100 chars.
    with open("/output/entry.txt", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        raise SystemExit("round-trip mismatch: wrote %r, read %r" % (text, written))

if __name__ == "__main__":
    main()
