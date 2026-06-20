"""Tests for instaImage and insta-split modules."""

from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image

from src.instaImage import make_square_image
from src.insta_split import split_image


def test_make_square_image(tmp_path: Path) -> None:
    img = Image.fromarray(np.zeros((50, 100, 3), dtype=np.uint8))
    input_path = tmp_path / "rect.png"
    img.save(input_path)
    output_path = tmp_path / "square.jpg"
    make_square_image(input_path, output_path)
    assert output_path.exists()
    result = Image.open(output_path)
    assert result.size[0] == result.size[1]


def test_split_image(tmp_path: Path) -> None:
    img = Image.fromarray(np.zeros((1024, 1024, 3), dtype=np.uint8))
    input_path = tmp_path / "square.png"
    img.save(input_path)
    out_dir = tmp_path / "tiles"
    tiles = split_image(input_path, out_dir, tile_size=512)
    assert len(tiles) == 4
    for tile in tiles:
        assert tile.exists()
