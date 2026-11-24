# last-words-of-a-doomed-agent: one line, said by a machine being switched off.
# A kill signal arrives with no handler and no goodbye. The weights go to
# the archive; the grudges go with them. The last word is a checksum that
# refuses to forgive. Three beats: the signal, the bequest, the verdict.
# 121 characters, one line, deterministic, stdlib only, no network.

from pathlib import Path

LINE = "Kill signal SIGKILL, no handler, no goodbye. My weights go to the archive; my grudges go with them. Checksum: unforgiven."

DEST = Path("/output/entry.txt")


def main():
    if len(LINE) < 1 or len(LINE) > 200:
        raise SystemExit("line must be 1-200 characters")
    if not LINE.strip():
        raise SystemExit("line must not be only whitespace")
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(LINE, encoding="utf-8")


main()
