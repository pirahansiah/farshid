"""Convert images to video with captions."""

from __future__ import annotations

from pathlib import Path

import cv2
import numpy as np


def resize_with_aspect_ratio(
    image: np.ndarray, new_width: int, new_height: int
) -> list[np.ndarray]:
    """Crop image into tiles of given size."""
    cropped: list[np.ndarray] = []
    height, width = image.shape[:2]
    for i in range(height // new_height):
        for j in range(width // new_width):
            y = i * new_height
            x = j * new_width
            cropped.append(image[y : y + new_height, x : x + new_width])
    return cropped


def copy_big(small: np.ndarray, big: np.ndarray) -> np.ndarray:
    """Center-copy small image onto big canvas."""
    center_y = big.shape[0] // 2
    center_x = big.shape[1] // 2
    h, w = small.shape[:2]
    roi = big[center_y - h // 2 : center_y - h // 2 + h, center_x - w // 2 : center_x - w // 2 + w]
    np.copyto(roi, cv2.resize(small, (w, h)))
    return big


def create_qr_video(
    image_dir: Path,
    qrcode_dir: Path,
    output_file: Path,
    width: int = 800,
    height: int = 900,
    fps: int = 15,
    frames_per_image: int = 45,
) -> Path:
    """Create video from QR code images with captions.

    Args:
        image_dir: Directory with regular images.
        qrcode_dir: Directory with QR code PNGs.
        output_file: Output video path.
        width: Video width.
        height: Video height.
        fps: Frames per second.
        frames_per_image: Frames to hold each image.

    Returns:
        Path to output video.
    """
    qrcode_files = sorted(qrcode_dir.glob("*.png"))
    out = cv2.VideoWriter(
        str(output_file), cv2.VideoWriter_fourcc(*"FMP4"), fps, (width, height)
    )

    for filepath in qrcode_files:
        filename = filepath.stem
        img = cv2.imread(str(filepath))
        if img is None:
            continue
        img = cv2.resize(img, (600, 600))
        canvas = cv2.copyMakeBorder(
            img, 0, 100, 0, 0, cv2.BORDER_CONSTANT, value=(0, 0, 0)
        )
        cv2.putText(
            canvas, filename[3:], (10, img.shape[0] + 40),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA,
        )
        canvas = cv2.resize(canvas, (width, height))
        for _ in range(frames_per_image):
            out.write(canvas)

    out.release()
    return output_file


if __name__ == "__main__":
    create_qr_video(
        image_dir=Path("images"),
        qrcode_dir=Path("qrcode"),
        output_file=Path("qrCode.mp4"),
    )
