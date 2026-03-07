"""Tests for LeetCode 146 - LRU Cache."""

import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from lc_146_lru import LRUCache


def test_basic_operations():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)  # evicts key 2
    assert cache.get(2) == -1
    assert cache.get(3) == 3
    cache.put(4, 4)  # evicts key 1
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4


def test_update_moves_to_mru():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(1, 10)  # update moves 1 to MRU
    cache.put(3, 3)  # evicts 2, not 1
    assert cache.get(1) == 10
    assert cache.get(2) == -1
    assert cache.get(3) == 3


def test_get_moves_to_mru():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1  # 1 is now MRU
    cache.put(3, 3)  # evicts 2
    assert cache.get(2) == -1
    assert cache.get(1) == 1


def test_capacity_one():
    cache = LRUCache(1)
    cache.put(1, 1)
    assert cache.get(1) == 1
    cache.put(2, 2)
    assert cache.get(1) == -1
    assert cache.get(2) == 2


if __name__ == "__main__":
    test_basic_operations()
    test_update_moves_to_mru()
    test_get_moves_to_mru()
    test_capacity_one()
    print("All tests passed!")
