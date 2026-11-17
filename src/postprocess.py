import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_FILE = PROJECT_ROOT / "output" / "extracted_entities.csv"
OUTPUT_FILE = PROJECT_ROOT / "output" / "cleaned_entities.csv"

# Load extracted entities
df = pd.read_csv(INPUT_FILE)

# Sort entities by comment and character position
df = df.sort_values(["comment_id", "start_position", "end_position"]).reset_index(
    drop=True
)

cleaned = []

for comment_id, group in df.groupby("comment_id"):

    group = group.sort_values("start_position")

    current = None

    for row in group.to_dict("records"):

        if current is None:
            current = row.copy()
            continue

        # Merge adjacent fragments belonging to same entity type
        if (
            current["entity_type"] == row["entity_type"]
            and current["end_position"] == row["start_position"]
        ):

            current["end_position"] = row["end_position"]

            current["entity"] = current["comment"][
                int(current["start_position"]) : int(current["end_position"])
            ]

            current["confidence"] = min(current["confidence"], row["confidence"])

        else:

            cleaned.append(current)
            current = row.copy()

    if current is not None:
        cleaned.append(current)


# Create final DataFrame
result = pd.DataFrame(cleaned)

result.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")

print("Entity consolidation completed!")

print(result[["comment_id", "entity", "entity_type", "confidence"]])

print(f"\nSaved to: {OUTPUT_FILE}")
