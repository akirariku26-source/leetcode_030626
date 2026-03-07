from collections import defaultdict
from typing import List


class UnionFind:
    """Disjoint-set structure with path compression and union by rank."""

    def __init__(self) -> None:
        self.parent: dict[str, str] = {}
        self.rank: dict[str, int] = {}

    def find(self, x: str) -> str:
        """Return the representative root for x."""
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: str, y: str) -> None:
        """Merge the sets containing x and y."""
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """Merge accounts that share at least one email address."""
        uf = UnionFind()
        email_to_name: dict[str, str] = {}

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                email_to_name[email] = name
                uf.union(email, account[1])

        root_to_emails: defaultdict[str, list[str]] = defaultdict(list)
        for email in email_to_name:
            root = uf.find(email)
            root_to_emails[root].append(email)

        return [[email_to_name[root]] + sorted(emails) for root, emails in root_to_emails.items()]