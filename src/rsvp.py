from collections import Counter


def dedupe_emails_case_preserve_order(emails):
    """Remove duplicates ignoring case, preserve first occurrence and order."""
    seen = set()
    result = []
    for email in emails:
        if "@" not in email:
            continue
        key = email.casefold()
        if key not in seen:
            seen.add(key)
            result.append(email)
    return result


def first_with_domain(emails, domain):
    """Return index of first email with given domain (case-insensitive)."""
    target = domain.casefold()
    for i, email in enumerate(emails):
        if "@" not in email:
            continue
        _, _, dom = email.partition("@")
        if dom.casefold() == target:
            return i
    return None


def domain_counts(emails):
    """Return list of (domain, count) sorted alphabetically, ignore invalid emails."""
    domains = [
        email.split("@", 1)[1].casefold()
        for email in emails
        if "@" in email
    ]
    counts = Counter(domains)
    return sorted(counts.items())
