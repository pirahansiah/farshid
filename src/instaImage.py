"""Create square images for Instagram from any aspect ratio."""

from __future__ import annotations

from pathlib import Path

from PIL import Image


def make_square_image(
    image_path: Path,
    output_path: Path,
    fill_color: tuple[int, int, int] = (255, 255, 255),
) -> Path:
    """Create a square image by padding with fill color.

    Args:
        image_path: Input image path.
        output_path: Output image path.
        fill_color: Background fill color.

    Returns:
        Path to the output image.
    """
    image = Image.open(image_path)
    width, height = image.size
    max_dim = max(width, height)
    new_image = Image.new("RGB", (max_dim, max_dim), color=fill_color)
    offset = ((max_dim - width) // 2, (max_dim - height) // 2)
    new_image.paste(image, offset)
    new_image.thumbnail((max_dim, max_dim))
    new_image.save(output_path)
    return output_path


if __name__ == "__main__":
    import sys
    in_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("input.png")
    out_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("output_square.jpg")
    make_square_image(in_path, out_path)
