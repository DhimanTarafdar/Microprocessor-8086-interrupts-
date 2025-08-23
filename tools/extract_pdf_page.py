import sys
from pathlib import Path

# Prefer pypdf for Python 3.13 compatibility
try:
    from pypdf import PdfReader
except Exception:
    print("ERROR: pypdf not installed. Install with: pip install pypdf", file=sys.stderr)
    sys.exit(2)


def extract_page_text(pdf_path: Path, page_number: int) -> str:
    reader = PdfReader(str(pdf_path))
    total = len(reader.pages)
    if page_number < 1 or page_number > total:
        raise ValueError(f"Page {page_number} out of range (1..{total}) for {pdf_path.name}")
    page = reader.pages[page_number - 1]
    return page.extract_text() or ""


def main():
    if len(sys.argv) != 3:
        print("Usage: python extract_pdf_page.py <pdf_path> <page_number>")
        sys.exit(1)
    pdf_path = Path(sys.argv[1])
    page_number = int(sys.argv[2])
    text = extract_page_text(pdf_path, page_number)
    print(text)


if __name__ == "__main__":
    main()
