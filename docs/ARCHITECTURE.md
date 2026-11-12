# Adb Spark Performance Agent architecture

Find a skewed Spark task from stage timing summaries.

```mermaid
flowchart LR
    N0["example.json"]
    N1["agent.py"]
    N2["Compare task duration against the stage median to find skew."]
    N3["Result for operator review"]
    N0 --> N1 --> N2 --> N3
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
