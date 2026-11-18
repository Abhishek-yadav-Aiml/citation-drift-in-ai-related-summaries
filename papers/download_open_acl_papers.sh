#!/usr/bin/env bash
set -euo pipefail

# Run this script from the repository root.
ROOT="$(pwd)"
OUT="$ROOT/papers/pdfs"
mkdir -p "$OUT"

download_pdf() {
  local url="$1"
  local filename="$2"
  local target="$OUT/$filename"
  local temp="$target.part"

  echo "Downloading $filename"
  curl --fail --location --retry 3 --connect-timeout 20 --max-time 180 \
    --output "$temp" "$url"

  if ! head -c 5 "$temp" | grep -q '%PDF-'; then
    rm -f "$temp"
    echo "ERROR: $filename does not look like a PDF." >&2
    exit 1
  fi

  mv "$temp" "$target"
  sha256sum "$target"
}

download_pdf \
  "https://aclanthology.org/2020.emnlp-main.609.pdf" \
  "Wadden_2020_Fact_or_Fiction.pdf"

download_pdf \
  "https://aclanthology.org/D15-1075.pdf" \
  "Bowman_2015_SNLI.pdf"

download_pdf \
  "https://aclanthology.org/N18-1101.pdf" \
  "Williams_2018_MultiNLI.pdf"

echo
echo "PDFs saved under papers/pdfs/"
echo "Review papers/pdfs/README.md for each file's license and attribution."
