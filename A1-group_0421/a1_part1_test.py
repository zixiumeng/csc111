"""CSC111 Winter 2021 Assignment 1: Linked Lists, Part 1

Instructions (READ THIS FIRST!)
===============================

Please write your tests for Part 1 in this module. Make sure to review the assignment
instructions carefully for this part! You may find it helpful to consult this
section of the Course Notes:
https://www.teach.cs.toronto.edu/~csc110y/fall/notes/B-python-libraries/02-pytest.html

While you must include unit tests, you may also use property-based tests in your test suite.

We will *not* be running PythonTA on this file; however, you should follow good programming
design and style in this file anyway, just like you would for all other work.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 David Liu and Isaac Waller.
"""
import pytest
from a1_part1 import MoveToFrontLinkedList, SwapLinkedList, CountLinkedList

# a test mutation, b test result, c test count


def test_move1a() -> None:
    """Test the first function with empty list"""
    linky = MoveToFrontLinkedList([])
    linky.__contains__(1)
    assert linky.to_list() == []


def test_move1b() -> None:
    """Test the first function with empty list"""
    linky = MoveToFrontLinkedList([])
    result = linky.__contains__(1)
    assert result is False


def test_move2a() -> None:
    """Test the first function with list of length onw"""
    linky = MoveToFrontLinkedList([1])
    linky.__contains__(1)
    assert linky.to_list() == [1]


def test_move2b() -> None:
    """Test the first function with list of length onw"""
    linky = MoveToFrontLinkedList([1])
    result = linky.__contains__(1)
    assert result is True


def test_move3a() -> None:
    """Test the first function with list of length 3 and doesnt mutate"""
    linky = MoveToFrontLinkedList([1, 2, 3])
    linky.__contains__(1)
    assert linky.to_list() == [1, 2, 3]


def test_move3b() -> None:
    """Test the first function with list of length 3 and doesnt mutate"""
    linky = MoveToFrontLinkedList([1, 2, 3])
    result = linky.__contains__(1)
    assert result is True


def test_move4a() -> None:
    """Test the first function with list of length 3 mutate"""
    linky = MoveToFrontLinkedList([1, 2, 3])
    linky.__contains__(2)
    assert linky.to_list() == [2, 1, 3]


def test_move4b() -> None:
    """Test the first function with list of length 3 mutate"""
    linky = MoveToFrontLinkedList([1, 2, 3])
    result = linky.__contains__(2)
    assert result is True


def test_move5a() -> None:
    """Test the first function with list of length 3 and doesnt mutate and does not contain item"""
    linky = MoveToFrontLinkedList([1, 2, 3])
    linky.__contains__(4)
    assert linky.to_list() == [1, 2, 3]


def test_move5b() -> None:
    """Test the first function with list of length 3 and doesnt mutate and does not contain item"""
    linky = MoveToFrontLinkedList([1, 2, 3])
    result = linky.__contains__(4)
    assert result is False


def test_swap1a() -> None:
    """Test the second function with empty list"""
    linky = SwapLinkedList([])
    linky.__contains__(1)
    assert linky.to_list() == []


def test_swap1b() -> None:
    """Test the second function with empty list"""
    linky = SwapLinkedList([])
    result = linky.__contains__(1)
    assert result is False


def test_swap2a() -> None:
    """Test the second function with list of length 2 and doesnt mutate"""
    linky = SwapLinkedList([1, 2])
    linky.__contains__(1)
    assert linky.to_list() == [1, 2]


def test_swap2b() -> None:
    """Test the second function with list of length 2 and doesnt mutate"""
    linky = SwapLinkedList([1, 2])
    result = linky.__contains__(1)
    assert result is True


def test_swap3a() -> None:
    """Test the second function with list of length 3 and mutate"""
    linky = SwapLinkedList([1, 2, 3])
    linky.__contains__(3)
    assert linky.to_list() == [1, 3, 2]


def test_swap3b() -> None:
    """Test the second function with list of length 3 and mutate"""
    linky = SwapLinkedList([1, 2, 3])
    result = linky.__contains__(3)
    assert result is True


def test_swap4a() -> None:
    """Test the second function with list of length 3 and doesnt mutate and does not contain item"""
    linky = SwapLinkedList([1, 2, 3])
    linky.__contains__(4)
    assert linky.to_list() == [1, 2, 3]


def test_swap4b() -> None:
    """Test the second function with list of length 3 and doesnt mutate and does not contain item"""
    linky = SwapLinkedList([1, 2, 3])
    result = linky.__contains__(4)
    assert result is False


def test_swap5a() -> None:
    """Test the second function with list of length 1 and doesnt mutate"""
    linky = SwapLinkedList([1])
    linky.__contains__(1)
    assert linky.to_list() == [1]


def test_swap5b() -> None:
    """Test the second function with list of length 1 and doesnt mutate"""
    linky = SwapLinkedList([1])
    result = linky.__contains__(1)
    assert result is True


def test_count1a() -> None:
    """Test the third function with empty list"""
    linky = CountLinkedList([])
    linky.__contains__(1)
    assert linky.to_list() == []


def test_count1b() -> None:
    """Test the third function with empty list"""
    linky = CountLinkedList([])
    result = linky.__contains__(1)
    assert result is False


def test_count2a() -> None:
    """Test the third function with empty list"""
    linky = CountLinkedList([1, 2, 3])
    linky.__contains__(1)
    assert linky.to_list() == [1, 2, 3]


def test_count2b() -> None:
    """Test the third function with empty list"""
    linky = CountLinkedList([1, 2, 3])
    result = linky.__contains__(1)
    assert result is True


def test_count2c() -> None:
    """Test the third function with empty list"""
    linky = CountLinkedList([1, 2, 3])
    linky.__contains__(1)
    assert linky._first.access_count == 1


def test_count3a() -> None:
    """Test the third function with list of length 3 and mutate"""
    linky = CountLinkedList([1, 2, 3])
    linky.__contains__(3)
    assert linky.to_list() == [3, 1, 2]


def test_count3b() -> None:
    """Test the third function with list of length 3 and mutate"""
    linky = CountLinkedList([1, 2, 3])
    result = linky.__contains__(3)
    assert result is True


def test_count3c() -> None:
    """Test the third function with list of length 3 and mutate"""
    linky = CountLinkedList([1, 2, 3])
    linky.__contains__(3)
    assert linky._first.access_count == 1 and linky._first.next.access_count == 0


def test_count4a() -> None:
    """Test the third function with list of length 3 and item no contain"""
    linky = CountLinkedList([1, 2, 3])
    linky.__contains__(4)
    assert linky.to_list() == [1, 2, 3]


def test_count4b() -> None:
    """Test the third function with list of length 3 and item no contain"""
    linky = CountLinkedList([1, 2, 3])
    result = linky.__contains__(4)
    assert result is False


def test_count4c() -> None:
    """Test the third function with list of length 3 and item no contain"""
    linky = CountLinkedList([1, 2, 3])
    linky.__contains__(4)
    assert linky._first.access_count == 0 and \
           linky._first.next.access_count == 0 and \
           linky._first.next.next.access_count == 0


def test_count5a() -> None:
    """Test the third function with list of length 3 and item is in linked list but same order"""
    linky = CountLinkedList([1, 2, 3])
    linky._first.access_count = 100
    linky.__contains__(2)
    assert linky.to_list() == [1, 2, 3]


def test_count5b() -> None:
    """Test the third function with list of length 3 and item no contain"""
    linky = CountLinkedList([1, 2, 3])
    linky._first.access_count = 100
    result = linky.__contains__(2)
    assert result is True


def test_count5c() -> None:
    """Test the third function with list of length 3 and item no contain"""
    linky = CountLinkedList([1, 2, 3])
    linky._first.access_count = 100
    linky.__contains__(2)
    assert linky._first.next.access_count == 1


if __name__ == '__main__':
    pytest.main(['a1_part1_test.py', '-v'])
