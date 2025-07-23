from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk
import string

nltk.download('punkt')
nltk.download('stopwords')


# Step 1: Text preprocessing
def preprocess(text):
    print("\n[INFO] Starting preprocessing...")
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Tokenize into words
    words = nltk.word_tokenize(text)

    # Remove stopwords
    stopwords = nltk.corpus.stopwords.words("english")
    filtered_words = [word for word in words if word not in stopwords]

    # Reconstruct cleaned text
    cleaned_text = " ".join(filtered_words)
    print("Preprocessing complete.\n")
    return cleaned_text

# Step 2: Summarize the text
def summarize(text, num_sentences=3):
    print("Starting summarization...")
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()  # Latent Semantic Analysis summarizer
    summary = summarizer(parser.document, num_sentences)

    summary_sentences = [str(sentence) for sentence in summary]
    print("Summarization complete.\n")
    return summary_sentences

# Step 3: Main function to run the tool
def main():
    print("=== Text Summarizer ===")
    input_text = input("Enter a paragraph:\n\n")

    summary = summarize(input_text)

    print("\nSummary:")
    for i, sentence in enumerate(summary, 1):
        print(f"{i}. {sentence}")

if __name__ == "__main__":
    main()
