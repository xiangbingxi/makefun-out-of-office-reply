"""Write the out-of-office reply to /output/entry.txt, exactly as given.

Writes the text with no trailing newline, then reads the file back and
verifies it byte for byte against the entry text before exiting.
"""

import os
import sys

ENTRY = "I'm out of office until Monday, but if it's urgent, my replacement can confidently tell you I'll be back on Thursday."


def main():
    if not 1 <= len(ENTRY) <= 160:
        print(f"entry is {len(ENTRY)} characters, must be 1-160", file=sys.stderr)
        sys.exit(1)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        print("entry.txt does not match ENTRY exactly", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
