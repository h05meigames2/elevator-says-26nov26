"""What the Elevator Would Say — make.fun entry.

Writes one original line, the funniest thing an elevator would say
in its own voice, to /output/entry.txt (single line, at most 120
characters). Deterministic, stdlib only, no network, no input.
"""

import os

# The angle: the elevator is a petty, observant doorman — it notices
# exactly who gets the door held and who gets it shut in their face,
# and it remembers. Elevator-specific (its doors), lands on the punch.
LINE = (
    "You hold the door for your crush and let it close on your boss "
    "\u2014 I keep the receipts."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
