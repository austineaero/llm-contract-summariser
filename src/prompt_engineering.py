"""Builds in-context prompt for key term extraction and summarization."""

def build_prompt(contract_text, schema):
    """Return LLM prompt for extracting fields and summary."""
    prompt = (
        "Extract the following fields from the contract text below. "
        "Answer in JSON. Then, generate a 2-sentence summary of the contract. "
        "If a field is missing, output null.\n\n"
        f"Fields: {', '.join(schema)}\n"
        "Contract Text:\n"
        f"{contract_text}\n"
        "Your response:\n"
    )
    return prompt