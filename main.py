#!/usr/bin/env python3
"""Entry program for make-the-ai-judge-feel-brave-20261121-0302.

Writes a short calming text to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt if the variable is unset), UTF-8, deterministic.
"""
import os

TEXT = (
    "The kettle ticks as it cools.\n"
    "Outside, the river takes the light\n"
    "downstream, unhurried, and gives it back\n"
    "as evening on the far bank.\n"
    "\n"
    "The cat is asleep on the rug.\n"
    "The lamp is lit. The chair is warm.\n"
    "Whatever comes next can wait\n"
    "until the tea is gone."
)

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write(TEXT)
print("wrote", path, len(TEXT), "characters")
