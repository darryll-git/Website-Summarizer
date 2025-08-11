# summarizer.py
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def summarize_text(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    prompt = f"Summarize the following webpage content in a concise way:\n\n{text}"

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Or gpt-4
        messages=[
            {"role": "system", "content": "You are a helpful summarization assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=500
    )

    summary = response.choices[0].message.content

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(summary)

if __name__ == "__main__":
    summarize_text("cleaned_page.md", "summary.md")
    print("✅ Summary saved to summary.md")
