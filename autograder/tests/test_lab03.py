# tests/test_lab03.py
# Lab 03 — Hash Tables (20 points total)
#
# Scoring: 4 questions × 5 points each = 20
# - Q1 char_frequency:            5
# - Q2 insert_chaining:           5
# - Q3 insert_linear_probing:     5
# - Q4 insert_quadratic_probing:  5
#
# This test file loads the student's code from:
#   STUDENT_DIR/lab03.py

from __future__ import annotations

import importlib.util
import os
from pathlib import Path

import pytest


def load_lab03():
    student_dir = os.environ.get("STUDENT_DIR")
    assert student_dir, "STUDENT_DIR env var not set"

    lab_path = Path(student_dir) / "lab03.py"
    assert lab_path.exists(), f"Missing file: {lab_path}"

    spec = importlib.util.spec_from_file_location("student_lab03", lab_path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.mark.points(5)
def test_q1_char_frequency():
    m = load_lab03()
    assert hasattr(m, "char_frequency"), "Missing function: char_frequency(s)"

    f = m.char_frequency
    assert f("") == {}
    assert f("a") == {"a": 1}
    assert f("banana") == {"b": 1, "a": 3, "n": 2}
    assert f("AaA") == {"A": 2, "a": 1}
    assert f("1122") == {"1": 2, "2": 2}


@pytest.mark.points(5)
def test_q2_insert_chaining():
    m = load_lab03()
    assert hasattr(m, "insert_chaining"), "Missing function: insert_chaining(table, key, size)"

    f = m.insert_chaining

    table = [[], [], []]
    out = f([b.copy() for b in table], 5, 3)
    assert out == [[], [], [5]]

    table = [[3], [], [5]]
    out = f([b.copy() for b in table], 8, 3)  # 8 % 3 = 2
    assert out == [[3], [], [5, 8]]

    table = [[], [1, 4], []]
    out = f([b.copy() for b in table], 10, 3)  # 10 % 3 = 1
    assert out == [[], [1, 4, 10], []]


@pytest.mark.points(5)
def test_q3_insert_linear_probing():
    m = load_lab03()
    assert hasattr(m, "insert_linear_probing"), "Missing function: insert_linear_probing(table, key)"

    f = m.insert_linear_probing

    t = [None, 4, None, None]
    out = f(t.copy(), 8)  # 8%4=0
    assert out == [8, 4, None, None]

    t = [4, None, None, None]
    out = f(t.copy(), 8)  # 8%4=0 occupied -> 1
    assert out == [4, 8, None, None]

    t = [4, 8, None, None]
    out = f(t.copy(), 12)  # 12%4=0 occupied -> 1 occupied -> 2
    assert out == [4, 8, 12, None]

    t = [4, 8, 12, None]
    out = f(t.copy(), 16)  # 16%4=0 -> 3 eventually
    assert out == [4, 8, 12, 16]

    # table full: should remain unchanged (per our spec choice)
    t = [1, 2, 3]
    out = f(t.copy(), 4)
    assert out == [1, 2, 3]


@pytest.mark.points(5)
def test_q4_insert_quadratic_probing():
    m = load_lab03()
    assert hasattr(m, "insert_quadratic_probing"), "Missing function: insert_quadratic_probing(table, key)"

    f = m.insert_quadratic_probing

    t = [None, 7, None, None]
    out = f(t.copy(), 11)  # 11%4=3 -> slot 3 empty
    assert out == [None, 7, None, 11]

    # collision resolved by quadratic steps: i^2
    # table size 5, key 1 -> h=1 (occupied), try 1+1=2, then 1+4=0, etc.
    t = [None, 99, None, None, None]
    out = f(t.copy(), 1)   # h=1 occupied -> i=1 idx=2
    assert out == [None, 99, 1, None, None]

    t = [None, 99, 1, None, None]
    out = f(t.copy(), 6)   # 6%5=1 occupied -> i=1 idx=2 occupied -> i=2 idx=0
    assert out == [6, 99, 1, None, None]

    # wrap-around check
    t = [None, None, None, None, 20]
    out = f(t.copy(), 9)   # 9%5=4 occupied -> i=1 idx=(4+1)%5=0
    assert out == [9, None, None, None, 20]

    # full table: should remain unchanged (per our spec choice)
    t = [1, 2, 3, 4]
    out = f(t.copy(), 5)
    assert out == [1, 2, 3, 4]
