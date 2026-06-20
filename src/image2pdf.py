"""Convert images folder to PDF."""

from __future__ import annotations

from pathlib import Path

from fpdf import FPDF


def create_pdf_from_images(
    image_folder: Path,
    output_pdf: Path,
    extensions: tuple[str, ...] = (".png", ".jpg", ".jpeg"),
) -> Path:
    """Create PDF from all images in a folder.

    Args:
        image_folder: Directory containing images.
        output_pdf: Output PDF path.
        extensions: Image file extensions to include.

    Returns:
        Path to output PDF.
    """
    pdf = FPDF()
    image_files = sorted(
        f for f in image_folder.iterdir() if f.suffix.lower() in extensions
    )
    for image_file in image_files:
        pdf.add_page()
        pdf.image(str(image_file))
        pdf.set_font("Arial", "B", 12)
        pdf.set_text_color(255, 255, 255)
        pdf.set_fill_color(0, 0, 0)
        pdf.cell(190, 10, image_file.name, ln=True, align="C", fill=True)

    pdf.output(str(output_pdf))
    return output_pdf


if __name__ == "__main__":
    create_pdf_from_images(Path("images"), Path("images.pdf"))
