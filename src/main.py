import pandas as pd
from transformers import pipeline
from pathlib import Path

# Harsha Sampath Perera 17/11/2026
# --------------------------------------------------
# 1. Project configuration
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_FILE = PROJECT_ROOT / "data" / "Comments.csv"
OUTPUT_FILE = PROJECT_ROOT / "output" / "extracted_entities.csv"

MODEL_NAME = "dslim/bert-base-NER"

# Entity types we want to extract
TARGET_ENTITIES = {"PER": "PERSON", "LOC": "LOCATION", "ORG": "ORGANIZATION"}


# --------------------------------------------------
# 2. Load pretrained Hugging Face model
# --------------------------------------------------

print("Loading Hugging Face NER model...")

ner_pipeline = pipeline(
    "ner", model=MODEL_NAME, aggregation_strategy="simple", device=-1
)

print("NER model loaded successfully!")


# --------------------------------------------------
# 3. Load comments dataset
# --------------------------------------------------

print("Reading input dataset...")

df = pd.read_csv(INPUT_FILE, encoding="utf-8-sig")

if not {"comment_id", "comment"}.issubset(df.columns):
    raise ValueError("Input CSV must contain comment_id and comment columns.")

df["comment"] = df["comment"].fillna("").astype(str)

print(f"Total comments: {len(df)}")


# --------------------------------------------------
# 4. Perform Named Entity Recognition
# --------------------------------------------------

print("Starting entity extraction...")

# Process comments in batches
comments = df["comment"].tolist()

predictions = ner_pipeline(comments, batch_size=8)

results = []

for row, entities in zip(df.itertuples(index=False), predictions):

    for entity in entities:

        entity_type = entity["entity_group"]

        # Keep only PERSON, LOCATION and ORGANIZATION
        if entity_type not in TARGET_ENTITIES:
            continue

        results.append(
            {
                "comment_id": row.comment_id,
                "comment": row.comment,
                "entity": entity["word"],
                "entity_type": TARGET_ENTITIES[entity_type],
                "confidence": round(float(entity["score"]), 4),
                "start_position": entity["start"],
                "end_position": entity["end"],
            }
        )


# --------------------------------------------------
# 5. Convert results into DataFrame
# --------------------------------------------------

output_df = pd.DataFrame(
    results,
    columns=[
        "comment_id",
        "comment",
        "entity",
        "entity_type",
        "confidence",
        "start_position",
        "end_position",
    ],
)


# --------------------------------------------------
# 6. Save extracted entities
# --------------------------------------------------

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

output_df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")


# --------------------------------------------------
# 7. Display summary
# --------------------------------------------------

print("\nNER PROCESS COMPLETED")

print(f"Total comments processed: {len(df)}")

print(f"Total entities extracted: {len(output_df)}")

print("\nEntity distribution:")

if not output_df.empty:
    print(output_df["entity_type"].value_counts())
else:
    print("No entities found.")

print(f"\nOutput saved to: {OUTPUT_FILE}")
