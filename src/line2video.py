"""Convert text file lines to video frames."""

from __future__ import annotations

from pathlib import Path

import cv2
import numpy as np


def text_to_video(
    input_file: Path,
    output_file: Path | None = None,
    width: int = 900,
    height: int = 900,
    fps: int = 1,
    tab_size: int = 1,
) -> Path:
    """Convert a text file to a video where each line becomes frames.

    Args:
        input_file: Path to text file.
        output_file: Output video path. Defaults to input_file + '_.mp4'.
        width: Video width.
        height: Video height.
        fps: Frames per second.
        tab_size: Tab expansion size.

    Returns:
        Path to the output video.
    """
    if output_file is None:
        output_file = input_file.with_suffix(input_file.suffix + "_.mp4")

    font = cv2.FONT_HERSHEY_SIMPLEX
    thickness = 1
    color = (255, 255, 255)

    text_y = 50
    image = np.zeros((height, width, 3), np.uint8)
    fourcc = cv2.VideoWriter_fourcc(*"MJPG")
    video = cv2.VideoWriter(str(output_file), fourcc, fps, (width, height))

    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    for line_text in lines:
        line = line_text.expandtabs(tab_size)
        if text_y < height - 100:
            text_y += 50
        else:
            image = np.zeros((height, width, 3), np.uint8)
            text_y = 50
        (w, _), _ = cv2.getTextSize(line, font, 1, thickness)
        w += 200
        scale = min(image.shape[1] / w, 1.0)
        cv2.getTextSize(line, font, scale, thickness)
        cv2.putText(image, line, (5, text_y), font, scale, color, thickness)
        video.write(image)

    video.release()
    return output_file


if __name__ == "__main__":
    import sys
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("input.txt")
    text_to_video(path)
