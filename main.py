"""The Best Meal You Ever Had — one sentence, written to /output/entry.txt."""

import os

# The memory: the best meal was not a banquet but instant noodles on a
# rainy night, eaten on the floor beside grandma — and the whole secret,
# she swore, was the soft egg. Humble dish, one person, one small
# detail no one else could have written. One sentence, no explaining it.
LINE = "The best meal I ever had was instant noodles on a rainy night, eaten cross-legged on the floor beside my grandma, who swore the soft egg was the whole secret."


# Gate: 1-200 UTF-8 characters, single line, no trailing newline.
# This line is 158 characters — well inside the gate.
def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
