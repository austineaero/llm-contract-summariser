"""Evaluation functions for field accuracy."""

def compare_fields(pred, gt, fields):
    """Return per-field exact match scores."""
    return {f: int(str(pred.get(f, '')).lower() == str(gt.get(f, '')).lower()) for f in fields}

def summary_word_overlap(summary, ref_summary):
    """Compute word overlap (Jaccard index) as summary similarity."""
    s1 = set(summary.lower().split())
    s2 = set(ref_summary.lower().split())
    return len(s1 & s2) / len(s1 | s2) if s1 | s2 else 0.0