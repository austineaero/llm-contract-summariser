"""LLM inference wrapper using HuggingFace pipeline."""
from transformers import pipeline
import re
import json

def get_llm_pipe(model_name="sshleifer/tiny-gpt2", max_length=512):
    """Return a text-generation pipeline."""
    return pipeline("text-generation", model=model_name, max_length=max_length)

def extract_fields_and_summary(llm, prompt):
    """Get JSON output and summary from LLM."""
    outputs = llm(prompt)
    text = outputs[0]['generated_text']
    # Try to extract JSON block from output
    try:
        json_str = re.search(r'\{.*\}', text, re.DOTALL).group(0)
        result = json.loads(json_str)
    except Exception:
        result = {}
    # Extract summary (last paragraph, after JSON)
    summary = None
    after_json = text.split('}', 1)[-1].strip()
    if after_json:
        summary = after_json.replace('\n', ' ').strip()
    return result, summary