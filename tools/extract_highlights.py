import sys
from pathlib import Path

try:
    import fitz  # PyMuPDF
except Exception as e:
    print("ERROR: PyMuPDF (fitz) not installed. Install with: pip install pymupdf", file=sys.stderr)
    raise


def extract_highlights(pdf_path: Path, page_number: int) -> str:
    doc = fitz.open(str(pdf_path))
    if page_number < 1 or page_number > doc.page_count:
        raise ValueError(f"Page {page_number} out of range (1..{doc.page_count}) for {pdf_path.name}")
    page = doc[page_number - 1]
    out = []
    for annot in page.annots() or []:
        if annot.type[0] == fitz.PDF_ANNOT_HIGHLIGHT:
            quads = annot.vertices
            # Extract text within the highlighted quads
            text = page.get_text("text", clip=fitz.Quad(quads).rect) if quads else ""
            if text:
                out.append(text.strip())
    # Fallback: if no highlights, return the full page text
    if not out:
        out_text = page.get_text("text") or ""
        return out_text.strip()
    return "\n\n".join(out)


def main():
    if len(sys.argv) != 3:
        print("Usage: python extract_highlights.py <pdf_path> <page_number>")
        sys.exit(1)
    pdf_path = Path(sys.argv[1])
    page_number = int(sys.argv[2])
    try:
        text = extract_highlights(pdf_path, page_number)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(2)
    print(text)


if __name__ == "__main__":
    main()