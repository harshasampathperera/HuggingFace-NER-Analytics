# Comment Named Entity Recognition (NER) using Hugging Face Transformers

## 1. Project Overview

This project implements a **Named Entity Recognition (NER)** solution using a pretrained BERT model from Hugging Face Transformers to identify and extract important entities from unstructured text comments.

The primary objective is to automatically identify people, geographical locations and organizations mentioned in comments and convert unstructured text into structured, meaningful information.

The project uses Natural Language Processing (NLP) and a pretrained Transformer-based model to perform entity extraction without training a model from scratch.

### Key Objectives

- Extract person names from text comments.
- Identify geographical locations such as countries, cities and provinces.
- Identify organizations, companies and institutions.
- Generate structured entity-level output from unstructured comments.
- Capture confidence scores for extracted entities.
- Save extracted results into CSV files for further analysis.

## 2. Business Use Case

Organizations receive large volumes of unstructured textual data through different channels, including:

- Customer feedback.
- Social media comments.
- Customer reviews.
- Online discussions.
- Surveys and feedback forms.
- Customer service interactions.

Manually identifying names, locations and organizations from thousands of comments can be time-consuming.

This project demonstrates how NLP and pretrained Hugging Face models can automate the entity extraction process.

The extracted information can subsequently be used for:

- Customer feedback analysis.
- Location-based sentiment analysis.
- Organization-level analysis.
- Customer relationship analysis.
- Business intelligence reporting.
- Advanced text analytics and machine learning projects.

## 3. Named Entity Recognition (NER)

Named Entity Recognition is an NLP technique used to identify and classify named entities in unstructured text.

For this project, the following entity categories are considered:

| Entity | Description | Example |
|---|---|---|
| PERSON | Names of individuals | John, Harsha, Elon Musk |
| LOCATION | Geographical locations | Colombo, Sri Lanka, London |
| ORGANIZATION | Companies and institutions | Microsoft, Google, LSEG |

The pretrained model also supports a MISC (Miscellaneous) category, but this project initially focuses on PERSON, LOCATION and ORGANIZATION.

## 4. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Hugging Face Transformers | Pretrained NLP model implementation |
| BERT | Transformer-based NER model |
| PyTorch | Deep learning framework |
| Pandas | Data processing and manipulation |
| VS Code | Development environment |
| PowerShell | Environment setup and command execution |
| Git | Version control |
| GitHub | Source code management |

## 5. Pretrained Model

This project uses the following pretrained Hugging Face model:

**Model:** `dslim/bert-base-NER`

Model URL: https://huggingface.co/dslim/bert-base-NER

### Model Details

- Architecture: BERT (Bidirectional Encoder Representations from Transformers).
- Model type: Token Classification.
- Training dataset: CoNLL-2003.
- Language: English.
- Entity recognition: PER, LOC, ORG and MISC.

The pretrained model is downloaded automatically from Hugging Face when the application is executed for the first time.

There is no requirement to train the model from scratch.

## 6. Project Architecture

The solution follows a simple NLP processing workflow.

```text
              Input Comments
                     |
                     v
              comments.csv
                     |
                     v
             Python Data Loading
                  Pandas
                     |
                     v
             Hugging Face BERT
                NER Pipeline
                     |
                     v
             Entity Recognition
                     |
          +----------+----------+
          |          |          |
          v          v          v
        PERSON      LOCATION    ORGANIZATION
          |          |          |
          +----------+----------+
                     |
                     v
              Entity Extraction
                     |
                     v
              CSV Output File
                     |
                     v
           Further Text Analytics
```

### Processing Steps

1. Read comments from the input CSV file.
2. Load the pretrained Hugging Face BERT NER model.
3. Pass the comments through the NER pipeline.
4. Identify and classify named entities.
5. Extract entity names, categories and confidence scores.
6. Store the results in a structured Pandas DataFrame.
7. Export the extracted entities into a CSV file.

## 7. Project Folder Structure

```text
comment-ner-extraction/
│
├── .venv/
│
├── data/
│   └── comments.csv
│
├── output/
│   ├── extracted_entities.csv
│   └── cleaned_entities.csv
│
├── src/
│   ├── main.py
│   └── postprocess.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

### Folder Description

| Folder/File | Description |
|---|---|
| `.venv/` | Isolated Python virtual environment |
| `data/` | Input comments dataset |
| `output/` | Generated entity extraction results |
| `src/main.py` | Main NER implementation |
| `src/postprocess.py` | Entity consolidation and post-processing |
| `requirements.txt` | Python dependencies |
| `.gitignore` | Files excluded from Git tracking |
| `README.md` | Project documentation |

The virtual environment, input datasets and generated output files should not be committed to the public repository unless they are intentionally included as safe sample data.

## 8. Prerequisites

Before running the project, ensure the following software is installed:

1. Python 3.11 or 3.12.
2. Visual Studio Code.
3. Git.
4. PowerShell.
5. Internet connection for downloading the pretrained model.

### Python Installation

Download Python from:

https://www.python.org/downloads/

Verify the installation:

```powershell
python --version
```

### VS Code Installation

Download VS Code:

https://code.visualstudio.com/

Recommended extensions:

- Python (Microsoft)
- Pylance (Microsoft)

## 9. Project Setup – Step by Step

### Step 1: Clone the GitHub Repository

If you are starting from an existing GitHub repository:

```powershell
git clone https://github.com/YOUR_USERNAME/comment-ner-extraction.git

cd comment-ner-extraction
```

Alternatively, create a new project directory:

```powershell
mkdir comment-ner-extraction

cd comment-ner-extraction

code .
```

### Step 2: Create a Python Virtual Environment

Create an isolated Python environment:

```powershell
python -m venv .venv
```

Activate the environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate the environment again:

```powershell
.\.venv\Scripts\Activate.ps1
```

Once activated, the terminal should display:

```text
(.venv) PS C:\...\comment-ner-extraction>
```

### Step 3: Configure the VS Code Python Interpreter

1. Open VS Code.
2. Press `Ctrl + Shift + P`.
3. Search for `Python: Select Interpreter`.
4. Select the interpreter inside `.venv`.

This ensures that VS Code executes Python using the project-specific environment.

### Step 4: Upgrade pip

```powershell
python -m pip install --upgrade pip
```

### Step 5: Install Required Libraries

Install PyTorch using the CPU version:

```powershell
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

Install Hugging Face Transformers and Pandas:

```powershell
pip install transformers pandas
```

Alternatively, install all project dependencies using:

```powershell
pip install -r requirements.txt
```

### Step 6: Verify the Installation

```powershell
pip list
```

The following main libraries should be available:

- torch
- transformers
- pandas

Other dependencies such as tokenizers, numpy and safetensors are installed automatically.

## 10. Input Dataset Preparation

The input dataset should be provided as a CSV file.

File location:

`data/comments.csv`

### Sample Input Data

```csv
comment_id,comment
1,"John visited Colombo last week."
2,"Microsoft is expanding its operations in Sri Lanka."
3,"Harsha works at LSEG in Colombo."
4,"Google opened a new office in India."
5,"Elon Musk is associated with Tesla."
6,"The government of Sri Lanka announced a new project in Kandy."
7,"Sarah moved from London to Singapore."
8,"Amazon is planning to expand its operations in Australia."
```

### Input Columns

| Column | Description |
|---|---|
| comment_id | Unique identifier for each comment |
| comment | Original unstructured text |

The Python implementation expects these two column names. Modify the input configuration if your source dataset uses different column names.

## 11. Model Implementation

The main implementation is available in:

`src/main.py`

The project uses Hugging Face's `pipeline()` API.

```python
from transformers import pipeline

MODEL_NAME = "dslim/bert-base-NER"

ner_pipeline = pipeline(
    task="ner",
    model=MODEL_NAME,
    aggregation_strategy="simple",
    device=-1
)
```

### Explanation of Parameters

| Parameter | Description |
|---|---|
| task="ner" | Performs Named Entity Recognition |
| model | Specifies the pretrained model |
| aggregation_strategy="simple" | Combines token-level predictions into complete entities |
| device=-1 | Executes the model using CPU |

### Entity Extraction

Each comment is passed to the NER pipeline.

```python
entities = ner_pipeline(
    "Harsha works at LSEG in Colombo."
)
```

Example output:

```text
Harsha   -> PER
LSEG     -> ORG
Colombo  -> LOC
```

The model returns the detected entity, entity category, confidence score and character positions.

The implementation maps the model labels into descriptive categories:

| Hugging Face label | Project output |
|---|---|
| PER | PERSON |
| LOC | LOCATION |
| ORG | ORGANIZATION |

## 12. Execute the Project

Ensure the virtual environment is activated.

Run the main script from the project root:

```powershell
python src/main.py
```

The script performs the following activities:

1. Loads the pretrained NER model.
2. Reads the input CSV file.
3. Processes comments in batches.
4. Identifies named entities.
5. Extracts the relevant entity categories.
6. Generates a structured output.
7. Saves the results to CSV.

### Expected Console Output

```text
Loading Hugging Face NER model...
NER model loaded successfully!

Reading input dataset...
Total comments: 8

Starting entity extraction...

NER PROCESS COMPLETED

Total comments processed: 8
Total entities extracted: [Actual count]

Entity distribution:
PERSON          [Actual count]
LOCATION        [Actual count]
ORGANIZATION    [Actual count]

Output saved to:
output/extracted_entities.csv
```

The first execution downloads the model. Subsequent executions generally use the locally cached model.

## 13. Output Dataset

The extracted entities are saved in:

`output/extracted_entities.csv`

### Output Columns

| Column | Description |
|---|---|
| comment_id | Original comment identifier |
| comment | Original comment |
| entity | Extracted entity name |
| entity_type | PERSON, LOCATION or ORGANIZATION |
| confidence | Model prediction confidence score |
| start_position | Starting character position in the original comment |
| end_position | Ending character position in the original comment |

### Sample Output

```csv
comment_id,entity,entity_type,confidence
1,John,PERSON,0.9991
1,Colombo,LOCATION,0.9996
2,Microsoft,ORGANIZATION,0.9989
2,Sri Lanka,LOCATION,0.9995
3,Harsha,PERSON,0.7508
3,LSEG,ORGANIZATION,0.9979
3,Colombo,LOCATION,0.9994
```

A single comment can contain multiple entities. Therefore, the output dataset contains one row per extracted entity rather than one row per comment.

## 14. Post-Processing and Entity Consolidation

The initial model output may contain fragmented entities or incorrect classifications.

For example, token-level predictions can sometimes produce:

```text
El       PER
##on Musk PER
```

The expected consolidated entity is:

```text
Elon Musk    PERSON
```

The post-processing implementation is available in:

`src/postprocess.py`

It combines adjacent fragments belonging to the same entity category using their original character positions.

Execute the post-processing script:

```powershell
python src/postprocess.py
```

The cleaned output is saved as:

`output/cleaned_entities.csv`

### Confidence-Based Review

The project also supports identifying predictions requiring manual review.

An experimental confidence threshold of 0.80 can be applied:

```python
result["review_required"] = (
    result["confidence"] < 0.80
)
```

Predictions below this threshold are flagged for manual review.

**Note:** Confidence thresholds should be calibrated using manually labelled validation data. Low confidence does not always indicate an incorrect prediction, and high confidence does not guarantee correctness.

Post-processing does not automatically correct semantic classification errors. For example, if Tesla is classified as PERSON instead of ORGANIZATION, the prediction must be validated and addressed through model evaluation or additional techniques.

## 15. Important Considerations and Limitations

### Language Support

The selected pretrained model is designed for English NER.

It may not reliably recognize entities in:

- Sinhala.
- Singlish.
- Mixed Sinhala and English comments.
- Other multilingual content.

For multilingual applications, alternative multilingual models should be evaluated.

### Social Media Comments

The pretrained model was trained using CoNLL-2003 news-domain data. Social media comments may contain:

- Informal language.
- Spelling mistakes.
- Abbreviations.
- Slang.
- Incomplete sentences.
- Unusual entity references.

Consequently, model performance on social media comments may differ from its performance on formal English text.

### Long Comments

BERT has a maximum input sequence length. Long comments may require text chunking with overlapping tokens to avoid losing entities near chunk boundaries.

### Model Accuracy

The confidence score returned by the model is not equivalent to actual prediction accuracy.

For a production-level solution, model performance should be evaluated using manually annotated data.

## 16. Future Enhancements

The following improvements can be considered in future versions:

1. Compare multiple pretrained Hugging Face NER models.
2. Introduce multilingual NER support.
3. Implement model evaluation using precision, recall and F1-score.
4. Improve entity consolidation and duplicate removal.
5. Add configurable confidence thresholds.
6. Process larger datasets using optimized batching.
7. Implement long-text chunking.
8. Develop a Streamlit interface for interactive comment analysis.
9. Integrate sentiment analysis with NER.
10. Build a Power BI dashboard to visualize extracted entities and geographical distributions.
11. Explore fine-tuning pretrained models using manually labelled domain-specific comments.



## 18. Useful References

- Hugging Face Transformers: https://huggingface.co/docs/transformers/
- Hugging Face NER Model: https://huggingface.co/dslim/bert-base-NER
- Hugging Face Token Classification: https://huggingface.co/docs/transformers/tasks/token_classification
- PyTorch: https://pytorch.org/
- Pandas: https://pandas.pydata.org/docs/
- Python Virtual Environments: https://docs.python.org/3/library/venv.html
- VS Code Python Documentation: https://code.visualstudio.com/docs/python/python-tutorial
- Git Documentation: https://git-scm.com/doc

---

## 19. Project Summary

This project demonstrates the practical application of Natural Language Processing and Transformer-based pretrained models for extracting meaningful entities from unstructured text comments.

By combining Python, Hugging Face Transformers, BERT and Pandas, the solution converts unstructured comments into structured entity-level information that can be used for further text analytics, business intelligence and machine learning applications.

**Project:** Comment Named Entity Recognition (NER)

**Model:** dslim/bert-base-NER

**Framework:** Hugging Face Transformers

**Programming Language:** Python

**Output:** Structured CSV containing extracted PERSON, LOCATION and ORGANIZATION entities.
