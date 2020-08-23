from tabulate import tabulate
from spacy import explain
from src.nlp import nlp


def print_token_table(sentence, pos=True, tag=True, dependency=True):
    """Print the linguistics features of each word in a sentence.
    If pos is True, then print the part-of-speech (POS). Defaults to True.
    If tag is True, then print the tag. Defaults to True.
    If dependency is True, then print the dependencices. Defaults to True.

    Given a string, return None.
    """
    # Create the table headers
    headers = []
    headers.append("Word")
    if pos:
        headers.append("POS")
        headers.append("POS Definition")
    if tag:
        headers.append("Tag")
        headers.append("Tag Definition")
    if dependency:
        headers.append("Dep.")
        headers.append("Dep. Definition")

    # Create the table data
    tagged_words = nlp(sentence)
    data = []
    for word in tagged_words:
        entry = []
        entry.append(word.text)
        if pos:
            entry.append(word.pos_)
            entry.append(explain(word.pos_))
        if tag:
            entry.append(word.tag_)
            entry.append(explain(word.tag_))
        if dependency:
            entry.append(word.dep_)
            entry.append(explain(word.dep_))
        data.append(entry)

    # Print the table
    print(tabulate(data, headers=headers, tablefmt="github"))
