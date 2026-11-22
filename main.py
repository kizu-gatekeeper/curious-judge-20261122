import os

TEXT = (
    "In the lighthouse keeper's cottage, the kettle is still warm, and two cups wait on the table. "
    "The last page of the log, in a careful hand, says only: "
    "\"It came back again tonight. Do not answer it.\" "
    "Below, in pencil, a second hand has added: \"Too late. We\""
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
