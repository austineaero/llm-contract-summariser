# LLM Contract Summariser & Key Info Extractor

A small, production-ready LLM-based pipeline for extracting and summarising key fields from contract text—built with modular code and MLOps best practices. Easily deployable on Databricks or any cloud platform.

---

## Table of Contents

- [Project Description](#project-description)
- [Repository Structure](#repository-structure)
- [Instructions (How to Run)](#instructions-how-to-run)
- [Technical Approach](#technical-approach)
- [Results & Performance](#results--performance)
- [Challenges & Mitigations](#challenges--mitigations)
- [Next Steps](#next-steps)
- [Credits](#credits)

---

## Project Description

This project demonstrates an advanced LLM-powered pipeline for **automatically extracting structured information and generating concise summaries from legal contracts or business documents**. The solution is tailored for organizations (like CCS or public sector) seeking reliable, auditable, and explainable document analytics using Large Language Models, while ensuring modularity, reproducibility, and ease of deployment.

---

## Repository Structure

```

llm-contract-extractor-demo/
├── data/
│   ├── contract1.txt          # Example contract document
│   ├── contract1.json         # Ground truth labels
├── output/
│   ├── result.json            # Model output for inspection
│   ├── evaluation.txt         # Metrics/results for evaluation
├── src/
│   ├── data_loader.py         # Data loading utilities
│   ├── prompt_engineering.py  # Prompt construction logic
│   ├── llm_inference.py       # LLM pipeline code
│   ├── metrics.py             # Evaluation functions
├── 01_explore_data.ipynb      # EDA & input inspection
├── 02_llm_extract_eval.ipynb  # LLM pipeline & evaluation notebook
├── requirements.txt
├── environment.yml
├── README.md

```

---

## Instructions (How to Run)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/llm-contract-summariser.git
   cd llm-contract-summariser
   ```

2. **Set up your environment:**

     ```bash
     pip install -r requirements.txt
     ```

3. **Run the pipeline:**

   * **In Databricks:**
     Upload the repo via “Repos” and open the notebooks.
   * **In Jupyter:**
     Start Jupyter and open the two notebooks in order:

     1. `01_explore_data.ipynb` (to view/inspect inputs)
     2. `02_llm_extract_eval.ipynb` (runs LLM extraction and evaluation)

4. **View results:**

   * Outputs (results, evaluation) are saved in the `output/` folder.

---

## Technical Approach

* **Preprocessing:** Loads plain-text contract and any available ground truth labels for evaluation.
* **Prompt Engineering:** Dynamically generates a schema-driven prompt, instructing the LLM to extract key fields (e.g., supplier, customer, contract\_value, effective\_date, etc.) and generate a summary, with clear output formatting (JSON + summary).
* **LLM Inference:** Uses a HuggingFace pipeline (e.g., `sshleifer/tiny-gpt2` for demo, or `distilbert-base-uncased` for tiny QA) to perform extraction. (API option for OpenAI available if more power needed.)
* **Postprocessing & Evaluation:** Compares the LLM’s output to ground truth for each field, computes per-field and overall extraction accuracy.
* **Outputs:** Saves extracted data, summaries, and evaluation metrics for review.

---

## Results & Performance

* **Extraction accuracy:** Reported per-field and overall (see `output/evaluation.txt`).
* **Sample output:** Model predictions and generated summary saved in `output/result.json`.
* **Qualitative results:** Inspect summaries and extracted fields for interpretability and alignment with ground truth.

*Note: Results will depend on the LLM used. The demo uses tiny models for easy reproducibility in any environment.*

---

## Challenges & Mitigations

* **Model hallucination/mis-extraction:**

  * *Mitigation:* Use clear, schema-driven prompts; few-shot examples can be added for better reliability.
* **Resource limits (cloud/free environments):**

  * *Mitigation:* Default to very small, open-source LLMs (e.g., `sshleifer/tiny-gpt2`) for portability. Provide option for cloud LLM APIs if required.
* **Evaluation subjectivity:**

  * *Mitigation:* Focus on field-level exact match for quantitative evaluation; qualitative review for summaries.

---

## Next Steps

* **API Deployment:** Containerize and serve as a REST API (FastAPI or Databricks Jobs).
* **Model Monitoring:** Add feedback logging, anomaly detection, and retraining triggers.
* **Extend Fields & Schema:** Adapt for more complex contracts, additional fields, or different document types.
* **Enhance Prompt Engineering:** Use advanced in-context/few-shot prompts and output format enforcement for better accuracy.

---