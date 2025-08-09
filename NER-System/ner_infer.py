import spacy

# Load the pre-trained spaCy model
nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)
    return [(ent.text, ent.label_, ent.start_char, ent.end_char) for ent in doc.ents]

if __name__ == "__main__":
    sample = "Sundar Pichai is the CEO of Google, headquartered in California."
    ents = extract_entities(sample)
    for text, label, start, end in ents:
        print(f"{text} → {label} [{start}:{end}]")
