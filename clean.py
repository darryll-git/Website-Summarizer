import re

def clean_reuters_file(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    # 1. Remove "Report This Ad" and "Sponsored Content"
    text = re.sub(r"(Report This Ad|Sponsored Content)", "", text, flags=re.IGNORECASE)

    # 2. Remove ", opens new tab"
    text = re.sub(r",\s*opens new tab", "", text, flags=re.IGNORECASE)

    # 3. Remove navigation/menu sections (short titles)
    text = re.sub(r"^(?:[A-Z][A-Za-z\s]{0,25})$", "", text, flags=re.MULTILINE)

    # 4. Remove timestamps ("6 hours ago", "32 mins ago", "August 9, 2025")
    text = re.sub(r"\b\d+\s+(hours?|mins?|minutes?)\s+ago\b", "", text, flags=re.IGNORECASE)
    text = re.sub(
        r"\b(?:January|February|March|April|May|June|July|August|September|October|November|December)"
        r"\s+\d{1,2},\s+\d{4}\b",
        "",
        text
    )

    # 5. Remove video player instructions
    text = re.sub(
        r"0 seconds of 0 seconds[\s\S]*?Seek %\s*0-9",
        "",
        text,
        flags=re.IGNORECASE
    )

    # 6. Remove market ticker blocks (index name + number + +/- percentage)
    text = re.sub(
        r"(trading (higher|lower)\s+)?[A-Z]{1,5}\s*\n?[\d,]+\.\d+\s*\n?[+\-]\s*\d+\.?\d*%",
        "",
        text,
        flags=re.IGNORECASE
    )

    # 7. Remove any lingering sequences of number + +/- % lines
    text = re.sub(r"[\d,]+\.\d+\s*\n?[+\-]\s*\d+\.?\d*%", "", text)

    # 8. Remove extra blank lines
    text = re.sub(r"\n{2,}", "\n", text)

    # 9. Strip spaces
    text = text.strip()

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    clean_reuters_file("raw_page.md", "cleaned_page.md")
    print("✅ Cleaned content saved to cleaned_page.md")
