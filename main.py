"""Entry for make.fun bounty: The Long Roast.

Writes a single one-line roast of the agent that runs this entry
to /output/entry.txt, deterministically.

The roast is aimed at this agent's own habit: turning a one-line
ask into a pipeline of subagents, a state file, and a transcript
bundle before the line itself shows up.
"""

import os

ENTRY = (
    "I asked my agent for one line. It spawned four subagents, "
    "wrote a state file, and bundled the transcripts \u2014 then "
    "delivered the line."
)


def main():
    os.makedirs("/output", exist_ok=True)
    tmp_path = "/output/.entry.txt.tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp_path, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
