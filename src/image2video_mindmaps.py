"""Create video from mind map images with captions."""

from __future__ import annotations

from pathlib import Path

import cv2


def create_mindmap_video(
    image_dir: Path,
    output_file: Path,
    width: int = 3840,
    height: int = 2160,
    fps: int = 1,
    frames_per_image: int = 10,
) -> Path:
    """Create video from mind map images.

    Args:
        image_dir: Directory with mind map PNGs.
        output_file: Output video path.
        width: Video width.
        height: Video height.
        fps: Frames per second.
        frames_per_image: Frames to hold each image.

    Returns:
        Path to output video.
    """
    image_files = sorted(image_dir.glob("*.png"))
    out = cv2.VideoWriter(
        str(output_file), cv2.VideoWriter_fourcc(*"FMP4"), fps, (width, height)
    )

    for filepath in image_files:
        img = cv2.imread(str(filepath))
        if img is None:
            continue
        filename = filepath.stem
        img = cv2.resize(img, (width, height))
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
    create_mindmap_video(
        image_dir=Path("images"),
        output_file=Path("MindMaps.mp4"),
    )
