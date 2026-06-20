"""Tests for image2pdf module."""

from __future__ import annotations

from pathlib import Path

import cv2
import numpy as np

from src.image2pdf import create_pdf_from_images


def test_create_pdf_empty_folder(tmp_path: Path) -> None:
    output = tmp_path / "output.pdf"
    result = create_pdf_from_images(tmp_path, output)
    assert result.exists()


def test_create_pdf_with_images(tmp_path: Path) -> None:
    for i in range(3):
        img = np.zeros((100, 100, 3), dtype=np.uint8)
        cv2.imwrite(str(tmp_path / f"img_{i}.png"), img)
    output = tmp_path / "output.pdf"
    result = create_pdf_from_images(tmp_path, output)
    assert result.exists()
    assert result.stat().st_size > 0
