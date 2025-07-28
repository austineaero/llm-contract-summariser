"""Functions to load contract text and labels."""
import json

def load_contract(path):
    """Load contract text file."""
    with open(path) as f:
        return f.read()

def load_labels(path):
    """Load ground truth labels from JSON."""
    with open(path) as f:
        return json.load(f)