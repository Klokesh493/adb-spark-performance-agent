# Adb Spark Performance Agent walkthrough

## Business problem

Find a skewed Spark task from stage timing summaries.

## Reproduce the workflow

Run `python3 agent.py example.json` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
{
  "median_ms": 105.0,
  "skewed_task_indexes": [
    3
  ]
}
```

The sample supplies these fields. `durations_ms`, `ratio`.

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.

## Regression scenario

A balanced stage emits no skewed task indexes.

`make verify` runs this scenario and compares the result with the checked-in expected JSON.
