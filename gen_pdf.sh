# Assumes you have pancoc & tex installed:
pandoc -f rst README.rst -o README.md
pandoc -f rst README.md -o Practical1.pdf
rm README.md
