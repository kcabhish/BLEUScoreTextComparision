## Bilingual Evaluation Understudy (BLEU)

- Metric used to evaluate text models.
- For example, you are using a Model to translate a poem from one language to another.

### BLEU Score

- Determines how well machine-translated text matches one or more human reference translations.
- Metric can be between zero and one.
    -   One = Perfect Match
    -   Zero = no overlap between the machine and human reference translations.

### About this project

This is a simple python application build to compare the generated text to the original text for evaluation.

To run the application:
`uv run python main.py`

If the references are exact match with the candidate, the score will be perfect 1 else it will generate value based on the difference between the reference and the original candidate.

This can be used to validate the responses when switching model, we can compare the response of the geenrated text to the expected test to evaluate the response type between different models.

It uses the following python library for evaluation.

| Package Name      | Description |
|-------------------|-------------|
| nltk              | The Natural Language Toolkit, a library for working with human language data, providing tools for text processing, tokenization, parsing, classification, and semantic reasoning. |