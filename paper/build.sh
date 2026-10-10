#!/bin/sh
# Build paper/main.pdf (pdflatex + biber).
set -e
cd "$(dirname "$0")"
pdflatex -interaction=nonstopmode main.tex
biber main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
