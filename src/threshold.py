"""Image thresholding utilities with custom PirahanSiah methods."""

from __future__ import annotations

import cv2
import numpy as np


class Thresholding:
    """Apply various thresholding methods to grayscale images."""

    def __init__(self, gray_img: np.ndarray) -> None:
        self.gray_img = gray_img

    def manually_python(self, threshold: int = 128) -> np.ndarray:
        """Fast Python threshold using numpy where."""
        return np.where(
            self.gray_img < threshold, self.gray_img, 0
        ) if threshold < 128 else np.where(self.gray_img > threshold, self.gray_img, 0)

    def manually(self, threshold: int) -> np.ndarray:
        """Manual threshold with explicit loop (educational)."""
        binary = np.zeros_like(self.gray_img)
        for i in range(self.gray_img.shape[0]):
            for j in range(self.gray_img.shape[1]):
                binary[i, j] = 0 if self.gray_img[i, j] < threshold else 1
        return binary

    def pirahansiah_threshold_method_find_threshold_values_2(self) -> int:
        """PSNR-based adaptive threshold (JATIT paper)."""
        assert self.gray_img is not None, "file could not be read, check with os.path.exists()"
        img = self.gray_img
        psnr_values = np.zeros(256)
        psnr_max = 0.0
        best_threshold = 0
        for t in range(0, 256, 5):
            _, binary = cv2.threshold(img, t, 255, cv2.THRESH_BINARY)
            psnr = cv2.PSNR(binary, img)
            psnr_values[t] = psnr
            if psnr_max < psnr:
                psnr_max = psnr
                best_threshold = t
        mean_psnr = np.mean(psnr_values)
        return int(best_threshold / mean_psnr) if mean_psnr > 0 else best_threshold

    def pirahansiah_threshold_method_find_threshold_values_1(self) -> int:
        """Contour-count based threshold (JATIT paper)."""
        assert self.gray_img is not None, "file could not be read, check with os.path.exists()"
        gray = cv2.GaussianBlur(self.gray_img, (3, 3), 0)
        max_contours = 0
        best_threshold = 0
        for t in range(0, 256, 10):
            _, binary = cv2.threshold(gray, t, 255, cv2.THRESH_BINARY)
            contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            if max_contours <= len(contours):
                max_contours = len(contours)
                best_threshold = t
        return best_threshold

    def opencv_th(self) -> None:
        """Display comparison grid of all thresholding methods."""
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 2
        color = (0, 0, 0)
        thickness = 2
        text_x, text_y = 25, 45

        _, binary_img = cv2.threshold(self.gray_img, 128, 255, cv2.THRESH_BINARY)
        _, binary_inv_img = cv2.threshold(self.gray_img, 128, 255, cv2.THRESH_BINARY_INV)
        _, trunc_img = cv2.threshold(self.gray_img, 128, 255, cv2.THRESH_TRUNC)
        _, tozero_img = cv2.threshold(self.gray_img, 128, 255, cv2.THRESH_TOZERO)
        _, tozero_inv_img = cv2.threshold(self.gray_img, 128, 255, cv2.THRESH_TOZERO_INV)
        adaptive_img = cv2.adaptiveThreshold(
            self.gray_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2
        )
        _, image_result = cv2.threshold(
            self.gray_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )

        labels = [
            (binary_img, "Binary"),
            (binary_inv_img, "Binary Inv"),
            (trunc_img, "Trunc"),
            (tozero_img, "To Zero"),
            (tozero_inv_img, "To Zero Inv"),
            (adaptive_img, "Adaptive"),
            (image_result, "Otsu Threshold"),
        ]

        images_with_labels: list[np.ndarray] = []
        for img_label, label in labels:
            img_copy = img_label.copy()
            text_size, _ = cv2.getTextSize(label, font, font_scale, thickness)
            cv2.rectangle(img_copy, (text_x, text_y - text_size[1]), (text_x + text_size[0], text_y), (255, 255, 255), -1)
            cv2.putText(img_copy, label, (text_x, text_y), font, font_scale, color, thickness)
            images_with_labels.append(img_copy)

        threshval = self.pirahansiah_threshold_method_find_threshold_values_1()
        th_img = self.manually(threshval)
        pirahan_img = (th_img * 255).astype(np.uint8)
        text_size, _ = cv2.getTextSize("PirahanSiah Threshold", font, font_scale, thickness)
        cv2.rectangle(pirahan_img, (text_x, text_y - text_size[1]), (text_x + text_size[0], text_y), (255, 255, 255), -1)
        cv2.putText(pirahan_img, "PirahanSiah Threshold", (text_x, text_y), font, font_scale, color, thickness)
        images_with_labels.append(pirahan_img)

        original = self.gray_img.copy()
        text_size, _ = cv2.getTextSize("Original", font, font_scale, thickness)
        cv2.rectangle(original, (text_x, text_y - text_size[1]), (text_x + text_size[0], text_y), (255, 255, 255), -1)
        cv2.putText(original, "Original", (text_x, text_y), font, font_scale, color, thickness)
        images_with_labels.append(original)

        row1 = np.concatenate(images_with_labels[0:3], axis=1)
        row2 = np.concatenate(images_with_labels[3:6], axis=1)
        row3 = np.concatenate(images_with_labels[6:9], axis=1)
        concatenated = np.concatenate((row1, row2, row3), axis=0)

        screen_res = (1720, 880)
        scale_w = screen_res[0] / concatenated.shape[1]
        scale_h = screen_res[1] / concatenated.shape[0]
        scale = min(scale_w, scale_h)
        resized = cv2.resize(concatenated, (int(concatenated.shape[1] * scale), int(concatenated.shape[0] * scale)))
        cv2.imshow("Thresholded Images", resized)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    img = cv2.imread("opencv.png")
    if img is not None:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        th = Thresholding(gray)
        th.opencv_th()
