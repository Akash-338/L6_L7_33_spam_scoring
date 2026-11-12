
def sender_domain(email):
    # Check whether input is a valid string
    if not isinstance(email, str):
        return ""

    email = email.strip()

    # Check whether exactly one @ symbol exists
    parts = email.split("@")

    if len(parts) != 2:
        return ""

    # Check whether both parts are non-empty
    if not parts[0].strip() or not parts[1].strip():
        return ""

    return parts[1].strip().lower()


def first_link(text):
    # Check whether input is a string
    if not isinstance(text, str):
        return ""

    # Find the first occurrence of http (case-insensitive)
    start = text.lower().find("http")

    # Return empty string if no link is found
    if start == -1:
        return ""

    # Extract the link
    return text[start:].split()[0]


def shout_ratio(text):
    # Check whether input is a string
    if not isinstance(text, str):
        return 0.0

    # Get all alphabetic characters
    letters = [c for c in text if c.isalpha()]

    # Avoid division by zero
    if len(letters) == 0:
        return 0.0

    # Count uppercase characters
    upper = [c for c in letters if c.isupper()]

    return len(upper) / len(letters)


def main():
    print("==== Running sender_domain ====")
    user_input = input("Enter a sender email (e.g. offers@Deals.com): ")
    result = sender_domain(user_input)
    print("Sender Domain:", result)

    print("\n==== Running first_link ====")
    user_input = input("Enter a message containing a link: ")
    result = first_link(user_input)
    print("First Link:", result)

    print("\n==== Running shout_ratio ====")
    user_input = input("Enter a message (e.g. FREE prize NOW): ")
    result = shout_ratio(user_input)
    print("Uppercase Ratio:", result)


if __name__ == "__main__":
    main()
