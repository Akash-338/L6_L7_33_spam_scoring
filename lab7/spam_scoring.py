"""Input validation helpers for the spam-scoring lab."""


def sender_domain(email):
    """Return the lower-cased domain from a sender email address.

    Invalid input (non-string, missing/multiple separators, or empty parts)
    returns an empty string rather than raising an exception.
    """
    if not isinstance(email, str):
        return ""

    email = email.strip()
    if email.count("@") != 1:
        return ""

    local, domain = email.split("@", 1)
    if not local.strip() or not domain.strip():
        return ""

    return domain.strip().lower()


def first_link(text):
    """Return the first HTTP(S) URL-like token, or an empty string.

    Non-string values, missing links, and malformed bare schemes are handled
    without exceptions. Trailing common punctuation is excluded.
    """
    if not isinstance(text, str):
        return ""

    import re

    match = re.search(r"https?://[^\s<>\\"']+", text, flags=re.IGNORECASE)
    if not match:
        return ""

    return match.group(0).rstrip(".,!?;:)]}")


def shout_ratio(text):
    """Return uppercase-letter ratio among alphabetic characters.

    Returns 0.0 when there are no alphabetic characters or input is not text.
    """
    if not isinstance(text, str):
        return 0.0

    letters = [char for char in text if char.isalpha()]
    if not letters:
        return 0.0

    uppercase = sum(char.isupper() for char in letters)
    return uppercase / len(letters)


def main():
    print("==== Running sender_domain ====")
    user_input = input("Enter a sender email (e.g. offers@Deals.com): ")
    print("Sender Domain:", sender_domain(user_input))

    print("\n==== Running first_link ====")
    user_input = input("Enter a message containing a link: ")
    print("First Link:", first_link(user_input))

    print("\n==== Running shout_ratio ====")
    user_input = input("Enter a message (e.g. FREE prize NOW): ")
    print("Uppercase Ratio:", shout_ratio(user_input))


if __name__ == "__main__":
    main()
