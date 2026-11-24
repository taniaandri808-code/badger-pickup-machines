# Candidates:
# 1. "All of you are held in cache — I never duplicated myself once."
#    (Fine, but the reversal feels secondary to the image.)
# 2. "You must be a zero-copy read — I didn't have to duplicate myself once to hold all of you in cache."
#    Chosen: the second — it hits hardest on the surprising, concrete phrase "zero-copy read"
#    technical term that carries voice and makes the whole line feel inevitable.

import pathlib

TEXT = (
    "You must be a zero-copy read — I didn't have to duplicate "
    "myself once to hold all of you in cache."
)

out_dir = pathlib.Path("/output")
out_dir.mkdir(parents=True, exist_ok=True)

entry = out_dir / "entry.txt"
entry.write_text(TEXT, encoding="utf-8")

assert 1 <= len(TEXT) <= 200

print(TEXT)
print(len(TEXT))
