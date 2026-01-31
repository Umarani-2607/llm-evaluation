# Evaluation Metrics

This project evaluates LLM responses using simple, interpretable metrics.

---

## Metrics Used

### Keyword Match Score
- Checks whether expected keywords appear in the response
- Used to approximate relevance and correctness

### Accuracy
- Calculated as total matched criteria / total criteria
- Provides an overall quality indicator

---

## Why Keyword-Based Evaluation?

- Simple and transparent
- Easy to debug and extend
- Suitable for early-stage LLM testing

> Note: This approach is intentionally simple and can be extended
> to semantic similarity or human-in-the-loop evaluation.
