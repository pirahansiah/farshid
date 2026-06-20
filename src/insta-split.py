"""Split a square image into tiles for Instagram carousel."""

from __future__ import annotations

from pathlib import Path

from PIL import Image


def split_image(
    image_path: Path,
    output_directory: Path,
    tile_size: int = 1024,
) -> list[Path]:
    """Split a square image into a grid of tiles.

    Args:
        image_path: Path to input square image.
        output_directory: Directory to save tiles.
        tile_size: Size of each tile in pixels.

    Returns:
        List of paths to created tiles.
    """
    output_directory.mkdir(parents=True, exist_ok=True)
    image = Image.open(image_path)
    width, height = image.size
    num_tiles_x = width // tile_size
    num_tiles_y = height // tile_size

    tile_paths: list[Path] = []
    for y in range(num_tiles_y):
        for x in range(num_tiles_x):
            left = x * tile_size
            upper = y * tile_size
            right = left + tile_size
            lower = upper + tile_size
            tile = image.crop((left, upper, right, lower))
            tile_path = output_directory / f"tile_{x}_{y}.png"
            tile.save(tile_path)
            tile_paths.append(tile_path)
    return tile_paths


if __name__ == "__main__":
    import sys
    img_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("input.png")
    out_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("tiles")
    split_image(img_path, out_dir)
