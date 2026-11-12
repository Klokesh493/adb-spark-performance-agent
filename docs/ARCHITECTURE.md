# Adb Spark Performance Agent architecture

Find a skewed Spark task from stage timing summaries.

```mermaid
flowchart LR
    A["Spark task duration export"]
    B["Calculate stage median"]
    C{"Task meets configured skew ratio?"}
    D["Report task index"]
    E["Return median with no matching index"]
    A --> B --> C
    C -->|Yes| D
    C -->|No| E
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
