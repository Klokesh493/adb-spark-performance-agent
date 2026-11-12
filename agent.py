import argparse
import json
from pathlib import Path


def evaluate(data):
    from statistics import median
    durations = data["durations_ms"]
    if not durations or min(durations) <= 0 or data["ratio"] <= 1:
        raise ValueError("expected positive durations and a ratio above one")
    baseline = median(durations)
    return {"median_ms": baseline, "skewed_task_indexes":
            [i for i, duration in enumerate(durations) if duration >= baseline * data["ratio"]]}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        print(json.dumps(evaluate(data), indent=2))
    except (KeyError, TypeError, ValueError, OSError) as exc:
        parser.exit(2, f"Invalid input: {exc}\n")


if __name__ == "__main__":
    main()
