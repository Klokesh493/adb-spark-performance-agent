# Adb Spark Performance Agent walkthrough

## Business problem

A small number of slow Spark tasks can delay a stage even when its average runtime looks acceptable.

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
