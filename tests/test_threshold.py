"""Tests for threshold module."""

from __future__ import annotations

import numpy as np

from src.threshold import Thresholding


def test_manually_python_below_threshold() -> None:
    img = np.full((10, 10), 100, dtype=np.uint8)
    th = Thresholding(img)
    result = th.manually_python(128)
    assert np.all(result == 0)


def test_manually_python_above_threshold() -> None:
    img = np.full((10, 10), 200, dtype=np.uint8)
    th = Thresholding(img)
    result = th.manually_python(128)
    assert np.all(result == 200)


def test_manually_binary_output() -> None:
    img = np.full((10, 10), 200, dtype=np.uint8)
    th = Thresholding(img)
    result = th.manually(128)
    assert result.shape == img.shape
    assert set(np.unique(result)).issubset({0, 1})


def test_pirahansiah_method_1_returns_int() -> None:
    img = np.random.randint(0, 256, (50, 50), dtype=np.uint8)
    th = Thresholding(img)
    result = th.pirahansiah_threshold_method_find_threshold_values_1()
    assert isinstance(result, int)
    assert 0 <= result <= 255


def test_pirahansiah_method_2_returns_int() -> None:
    img = np.random.randint(0, 256, (50, 50), dtype=np.uint8)
    th = Thresholding(img)
    result = th.pirahansiah_threshold_method_find_threshold_values_2()
    assert isinstance(result, int)
    assert 0 <= result <= 255
