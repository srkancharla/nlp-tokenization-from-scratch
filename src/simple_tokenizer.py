class SimpleTokenizer:
    """A minimal whitespace tokenizer."""

    def __init__(self, lowercase=True):
        self.lowercase = lowercase

    def tokenize(self, text):
        if self.lowercase:
            text = text.lower()
        return text.strip().split()

    def detokenize(self, tokens):
        return " ".join(tokens)


if __name__ == "__main__":
    text = "The quick brown fox jumps over the lazy dog."
    tokenizer = SimpleTokenizer()
    tokens = tokenizer.tokenize(text)
    print(tokens)
    print(tokenizer.detokenize(tokens))
