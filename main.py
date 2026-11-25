"""One-Liner Marathon entry.

Writes one single-line joke to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
Python 3.13 stdlib-only (only `os`).
"""

import os

TEXT = "The museum audio guide spent three minutes on the painting and two on the frame, then described my reflection in the glass as an early work, unfinished."

MAX_CHARS = 280


def check_gate(text):
    """Enforce the RULES.txt gate only: 1-280 chars, one line, not
    whitespace-only, no control chars, ASCII-only. The ASCII-only rule is
    a tie-break safeguard (len in chars equals len in bytes), not a RULES
    gate. The 150-260 concept target is enforced by the test suite (T1),
    not here. Raises SystemExit on the first violation found."""
    if not isinstance(text, str):
        raise SystemExit("gate: text is not str")
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"gate: length {len(text)} outside 1-{MAX_CHARS}")
    if "\n" in text or "\r" in text:
        raise SystemExit("gate: text must be a single line")
    if not text.strip():
        raise SystemExit("gate: text is whitespace-only")
    for char in text:
        code = ord(char)
        if code < 0x20 or code == 0x7F:
            raise SystemExit(f"gate: control character U+{code:04X}")
        if code >= 128:
            raise SystemExit("gate: text is not ASCII-only")


def main():
    check_gate(TEXT)
    output_dir = os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, mode="w", encoding="utf-8") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
