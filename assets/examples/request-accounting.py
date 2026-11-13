"""Print the six fictional requests in the guide as counts; no external dependencies."""

from typing import NamedTuple, Optional


class Request(NamedTuple):
    key: str
    status: str
    correct: Optional[bool]
    returned_ms: Optional[int]
    calls: int


REQUESTS = (
    Request("A", "answer", True, 55, 1),
    Request("B", "answer", True, 100, 2),
    Request("C", "answer", True, 135, 1),
    Request("D", "answer", False, 60, 1),
    Request("E", "timeout", None, None, 2),
    Request("F", "handoff", None, None, 0),
)


def counts(requests, deadline_ms):
    if len({r.key for r in requests}) != len(requests):
        raise ValueError("Count one row per request, not per attempt")
    answered = [r for r in requests if r.status == "answer"]
    for r in requests:
        if (r.status not in {"answer", "timeout", "handoff"} or r.calls < 0 or
                (r.status == "answer" and (r.returned_ms is None or r.returned_ms < 0 or
                                           type(r.correct) is not bool)) or
                (r.status != "answer" and (r.correct is not None or r.returned_ms is not None))):
            raise ValueError("This fixture requires verified automatic answers and explicit nonanswers")
    return {
        "returned-answer accuracy": (sum(r.correct for r in answered), len(answered)),
        "automatic answer coverage": (len(answered), len(requests)),
        "timely correct delivery": (sum(r.correct and r.returned_ms <= deadline_ms for r in answered),
                                    len(requests)),
    }


if __name__ == "__main__":
    print("Fictional requests, inclusive deadline: 100 ms")
    for label, (numerator, denominator) in counts(REQUESTS, 100).items():
        print(f"{label}: {numerator}/{denominator}")
