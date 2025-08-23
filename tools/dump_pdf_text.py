import sys
from pathlib import Path

try:
    from pypdf import PdfReader
except Exception as e:
    sys.stderr.write("pypdf is required. Install with: pip install pypdf\n")
    raise


def dump_pages(pdf_path: Path, out_dir: Path):
    reader = PdfReader(str(pdf_path))
    total = len(reader.pages)
    out_dir.mkdir(parents=True, exist_ok=True)
    for i in range(total):
        page = reader.pages[i]
        text = page.extract_text() or ""
        (out_dir / f"page_{i+1:03d}.txt").write_text(text, encoding="utf-8")
    return total


def main():
    if len(sys.argv) != 3:
        print("Usage: python dump_pdf_text.py <pdf_path> <output_dir>")
        sys.exit(1)
    pdf_path = Path(sys.argv[1])
    out_dir = Path(sys.argv[2])
    total = dump_pages(pdf_path, out_dir)
    print(f"Wrote {total} pages to {out_dir}")


if __name__ == "__main__":
    main()
