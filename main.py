import nltk
from nltk.translate.bleu_score import sentence_bleu
from nltk.translate.bleu_score import SmoothingFunction
def main():

    # Example reference texts and a candidate text from a generative model
    reference1 = "Discovering new skills is both enjoyable and thrilling".split()
    reference2 = "It's exciting and enjoyable to learn new things".split()
    reference3 = "Gaining new knowledge can be fun and exhilarating".split()
    candidate = "Learning new stuff is fun and exciting".split()

    # List of references
    references = [reference1, reference2, reference3]

    # Calculate BLEU score
    bleu_score = sentence_bleu(references, candidate, smoothing_function=SmoothingFunction().method1)

    print("BLEU score:", bleu_score)


if __name__ == "__main__":
    main()
