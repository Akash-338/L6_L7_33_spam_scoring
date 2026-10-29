
from spam_scoring import (
    score_message,
    classify,
    filter_inbox,
    inbox_status,
)


def test_score_message_basic():
    assert score_message("hello there", False, 0) == 0


def test_score_message_spam_words():
    assert score_message("free winner", False, 0) == 4


def test_score_message_uppercase_word():
    assert score_message("ALERT", False, 0) == 1


def test_score_message_links():
    assert score_message("hello", False, 1) == 1
    assert score_message("hello", False, 4) == 4


def test_score_message_known_sender():
    assert score_message("free winner", True, 0) == 1


def test_score_message_score_cannot_be_negative():
    assert score_message("free", True, 0) == 0


def test_classify_all_categories():
    assert classify(8) == "spam"
    assert classify(4) == "suspicious"
    assert classify(0) == "clean"


def test_filter_inbox():
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


def test_filter_inbox_empty():
    assert filter_inbox([]) == {
        "spam": 0,
        "suspicious": 0,
        "clean": 0,
    }


def test_inbox_status_empty():
    assert inbox_status({}) == "empty"


def test_inbox_status_flooded():
    assert inbox_status({
        "spam": 6,
        "suspicious": 2,
        "clean": 2,
    }) == "flooded"


def test_inbox_status_noisy():
    assert inbox_status({
        "spam": 3,
        "suspicious": 2,
        "clean": 5,
    }) == "noisy"


def test_inbox_status_healthy():
    assert inbox_status({
        "spam": 2,
        "suspicious": 2,
        "clean": 6,
    }) == "healthy"
