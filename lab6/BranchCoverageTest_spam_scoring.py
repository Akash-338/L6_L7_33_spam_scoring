
from spam_scoring import (
    score_message,
    classify,
    filter_inbox,
    inbox_status,
)


# score_message: spam word, uppercase word and ordinary word
def test_word_decision_branches():
    assert score_message("free", False, 0) == 2
    assert score_message("ALERT", False, 0) == 1
    assert score_message("hello", False, 0) == 0


# Link count: greater than 3, between 1 and 3, and zero
def test_link_count_branches():
    assert score_message("hello", False, 4) == 4
    assert score_message("hello", False, 2) == 1
    assert score_message("hello", False, 0) == 0


# Known sender: clamp a negative score and preserve a positive score
def test_known_sender_branches():
    assert score_message("free", True, 0) == 0
    assert score_message("free winner", True, 0) == 1
    assert score_message("hello", False, 0) == 0


# Classifier boundaries: 8, 4 and below 4
def test_classification_branches():
    assert classify(8) == "spam"
    assert classify(7) == "suspicious"
    assert classify(4) == "suspicious"
    assert classify(3) == "clean"


# Inbox loop: empty input and populated input
def test_filter_inbox_branches():
    assert filter_inbox([]) == {
        "spam": 0,
        "suspicious": 0,
        "clean": 0,
    }

    messages = [
        ("free winner urgent", False, 4),
        ("free winner", False, 0),
        ("hello", False, 0),
    ]

    assert filter_inbox(messages) == {
        "spam": 1,
        "suspicious": 1,
        "clean": 1,
    }


# Inbox status: empty, flooded, noisy and healthy
def test_inbox_status_branches():
    assert inbox_status({}) == "empty"

    assert inbox_status({
        "spam": 6,
        "suspicious": 2,
        "clean": 2,
    }) == "flooded"

    assert inbox_status({
        "spam": 3,
        "suspicious": 2,
        "clean": 5,
    }) == "noisy"

    assert inbox_status({
        "spam": 2,
        "suspicious": 2,
        "clean": 6,
    }) == "healthy"


# Exact threshold boundaries: ratio must be strictly greater
def test_inbox_status_threshold_boundaries():
    assert inbox_status({
        "spam": 5,
        "suspicious": 0,
        "clean": 5,
    }) == "noisy"

    assert inbox_status({
        "spam": 2,
        "suspicious": 0,
        "clean": 8,
    }) == "healthy"
