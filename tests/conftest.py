"""Shared test fixtures."""

from __future__ import annotations

from pathlib import Path

import cv2
import numpy as np
import pytest


@pytest.fixture
def sample_image() -> np.ndarray:
    """100x100 BGR test image."""
    return np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)


@pytest.fixture
def sample_grayscale() -> np.ndarray:
    """100x100 grayscale test image."""
    return np.random.randint(0, 256, (100, 100), dtype=np.uint8)


@pytest.fixture
def tmp_image(tmp_path: Path) -> Path:
    """Create a temporary test image."""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    path = tmp_path / "test.png"
    cv2.imwrite(str(path), img)
    return path
