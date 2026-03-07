"""Tests for LeetCode 721 - Accounts Merge."""

import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from lc_721_accounts_merge import Solution


def normalize(accounts: list[list[str]]) -> list[list[str]]:
    """Sort merged accounts for stable test comparisons."""
    return sorted([[account[0]] + sorted(account[1:]) for account in accounts])


def test_accounts_merge_example_case():
    solution = Solution()
    accounts = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]

    result = solution.accountsMerge(accounts)
    expected = [
        ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]

    assert normalize(result) == normalize(expected)


def test_accounts_merge_multiple_accounts_same_person():
    solution = Solution()
    accounts = [
        ["Gabe", "gabe0@m.co", "gabe3@m.co", "gabe1@m.co"],
        ["Gabe", "gabe3@m.co", "gabe4@m.co"],
        ["Gabe", "gabe4@m.co", "gabe2@m.co"],
    ]

    result = solution.accountsMerge(accounts)
    expected = [["Gabe", "gabe0@m.co", "gabe1@m.co", "gabe2@m.co", "gabe3@m.co", "gabe4@m.co"]]

    assert normalize(result) == normalize(expected)


def test_accounts_merge_no_shared_emails():
    solution = Solution()
    accounts = [
        ["Alex", "alex1@mail.com"],
        ["Alex", "alex2@mail.com"],
    ]

    result = solution.accountsMerge(accounts)
    expected = [
        ["Alex", "alex1@mail.com"],
        ["Alex", "alex2@mail.com"],
    ]

    assert normalize(result) == normalize(expected)
