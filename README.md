# Grammar-Detector

A tool for detecting grammatical features in sentences, clauses, and phrases without writing a line of code. This tool is one piece of a larger project to facilitate the creation of reading exercises for language instruction. It is designed to determine if a text contains sentences relevant to the desired grammatical feature.

The patterns for these grammatical features are defined in YAML files called `patternsets` in lieu of writing code. These YAML files expand the capabilities of the `GrammarDetector`. The input text to be analyzed is compared against the patterns in the `patternsets`. In other words, writing more code is unnecessary for supporting new grammatical features. This means that inaccurate results arise from inaccurate patterns and not from the code itself. Unittests can be defined in the `patternsets` to assist with improving pattern accuracy.

For the purposes of this tool, a sentence is roughly defined as:

1. an independent clause with sentence-final punctuation and additional clauses, or 
1. a dependent clause with sentence-final punctuation which may satisfy the concept of a 'complete thought' in the context of surrounding sentences (e.g. "We tried updating it. Which didn't work. Neither did the reinstall.")

## Overview

The core of this tool is the `GrammarDetector`. After construction, it can be used in two different ways:

1. Using the `GrammarDetector.__call__(self, input: str)` method on the input to run **automatically**.
1. Looping through the `detectors: list[Detector]` property and using the `Detector.__call__(self, input: str)` method on the input to run **manually**.

## Dependencies

Dependencies:

* **python** (>=3.9)        -- frequent use of f-strings and type hints
* **pyyaml**                -- loading patternset YAML files
* **spacy**                 -- rule-based grammatical pattern matching
* **spacy-lookups-data**    -- spaCy dependency
* **tabulate**              -- printing token tables to write patterns

Dev dependencies:

* **black**                 -- opinionated code formatter
* **mypy**                  -- type checking
* **python-lsp-server**     -- IDE integration
* **types-pyyaml**          -- type checking
* **types-tabulate**        -- type checking  
* **types-setuptools**      -- type checking

## Grammatical Features Currently Supported

All current patterns are relatively naive, so they do not yet effectively handle recursivity. This problem can be solved by 1) writing recursive patterns or 2) writing alternative patterns and suffixing the `rulename` property with numbers (e.g. ditransitive-1 and ditransitive-2).

* [Determiners](https://en.wikipedia.org/wiki/Determiner):
    * Indefinite
    * Definite
    * Other
    * [None](https://en.wikipedia.org/wiki/Zero-marking_in_English#Zero_article)
* [Persons](https://en.wikipedia.org/wiki/Grammatical_person):
    * 1st
    * 2nd
    * 3rd
* [Tense-Aspects](https://en.wikipedia.org/wiki/Tense%E2%80%93aspect%E2%80%93mood):
    * Present simple
    * Present simple passive
    * Past simple
    * Past simple passive
    * Future simple will
    * Future simple will passive
    * Future simple be-going-to
    * Future simple be-going-to passive
    * Present continuous
    * Present continuous passive
    * Past continuous
    * Past continuous passive
    * Future continuous
    * Future continuous passive
    * Present perfect
    * Present perfect passive
    * Past perfect
    * Past perfect passive
    * Future perfect
    * Future perfect passive
    * Present perfect continuous
    * Present perfect continuous passive
    * Past perfect continuous
    * Past perfect continuous passive
    * Future perfect continuous
    * Future perfect continuous passive
* [Transitivity and Valency](https://en.wikipedia.org/wiki/Valency_\(linguistics\)):
    * Impersonal (valency = 0)
    * Intransitive (valency = 1)
    * Transitive (valency = 2)
    * Ditransitive (valency = 3)
* [Voices](https://en.wikipedia.org/wiki/Voice_\(grammar\)):
    * Active
    * Passive

## How to Install

`$ pip install TODO: add package name`

TODO: update install statement

## Example Usage

### Running the GrammarDetector

1. Import `GrammarDetector` from `TODO: add package name`
1. Construct the `GrammarDetector`
1. Run the `GrammarDetector.__call__(self, input: str)` method on the input

TODO: add import statement

---
    # my_script.py

    # TODO: add import statement

    # Default values
    settings: dict[str, Union[str, bool]] = {  
        "builtins": True,
        "dataset": "en_core_web_lg",
        "features": "all",
        "patternset_path": "",  # Custom patternsets
        "settings_path": "settings.yaml",
        "verbose": False,
        "very_verbose": False,
    }
    grammar_detector = GrammarDetector(**settings)  # Optionally, pass in **settings

    sentence: str = "The dog chased a cat into the house."
    results: dict[str, Union[str, list[Match]]] = grammar_detector(sentence)
---

### Using the Results

---
    # my_script.py

    sentence: str = "The dog chased a cat into the house."
    results: dict[str, Union[str, list[Match]]] = grammar_detector(sentence)

    print(results)
    # Prints the following:
    # {
    #     'input': 'The dog chased a cat into the house.', 
    #     'voices': [<active: chased>], 
    #     'tense_aspects': [<past simple: chased>], 
    #     'persons': [<3rd: dog>, <3rd: cat>, <3rd: house>], 
    #     'determiners': [<definite: The dog>, <indefinite: a cat>, <definite: the house>], 
    #     'transitivity': [<ditransitive: dog chased a cat into the house>]
    # }

    feature: str = "tense_aspects"
    verb_tense: Match = results[feature][0]
    print(verb_tense)  # Prints <past simple: chased>
    print(verb_tense.rulename)  # Prints "past simple"
    print(verb_tense.span)  # Prints "chased"
---

## Components of the GrammarDetector

This section describes the internal components used to build and run `Detectors` inside the `GrammarDetector`. To expand on the built-in features of the `GrammarDetector`, understanding how `patternset` YAML files are created, configured, and loaded is critical. To load your own `patternset` files, pass the file or directory path to the `patternset_path` keyword argument when constructing the `GrammarDetector`.

### What is the GrammarDetector class?

The `GrammarDetector` class is the entrypoint for loading in `patternset` files and evaluating text input. By running `GrammarDetector.__call__(self, sentence)`, the text input will be compared against both the provided `patternsets` (via the `patternset_path` keyword argument) and the built-in `patternsets`. The `DetectorRepository` is contained under the hood, which in turn contains the `Detectors`. Extracting the internal `Detectors` from the `GrammarDetector` is possible but unnecessary.

---
    # my_script.py

    grammar_detector = GrammarDetector(patternset_path="path/to/my/patternsets/")
    sentence = "The dog chased the cat into the house."
    results = grammar_detector(sentence)  # Making use of the __call__ class method
---

### Component: Token

The smallest atom is the [`spacy.tokens.Token`](https://spacy.io/usage/rule-based-matching) class. Each `Token` represents a single word and consists of a single JSON object. A `list[Token]` represents a chain of words. Lists of `Tokens` are used in `patternset` YAML files to define grammatical patterns. Each `Token` contains a `POS` (part-of-speech), a `TAG` (tag), and/or a `DEP` (dependency). Grammatical categories are denoted with `POS` and `TAG` while syntactic categories are denoted with `DEP`. An `OP` (operation) may also be included to denote whether a `Token` is required or optional. A complete list of `POSs`, `TAGs`, and `DEPs` can be found in [the spaCy glossary](https://github.com/explosion/spaCy/blob/master/spacy/glossary.py).

Some examples of `POSs` are "VERB", "AUX", "NOUN", "PROPN", and "SYM" for symbol. 

Some examples of `TAGs` are "VB" for base form verb, "VBD" for past tense verb, "VBG" for gerund/present participle verb, "VBN" for past participle verb, "VBP" for non-3rd person singular present verb, and "VBZ" for 3rd person singular present verb.

Some examples of `DEPs` are "ROOT" for root verb, "aux", "auxpass", "nsubj", and "dobj".

#### Examples of Tokens

##### Token: Present Simple Verb

---
    # my_feature.yaml

    ---
    patterns:
        - rulename: present simple verb
        # This is a single token (i.e. 1 word)
          tokens:  
            - {TAG: {IN: ["VBP", "VBZ"]},
---

##### Token: Passive Auxiliary Verb

---
    # my_feature.yaml
    
    ---
    patterns:
        - rulename: passive auxiliary
        # This is also a single token (i.e. 1 word)
          tokens:  
            - {
              TAG: {IN: ["VBP", "VBZ"]},
              DEP: "auxpass",
              LEMMA: "be",
              OP: "+"
            }
---

##### Token: Future Simple Be-going-to Passive

---
    # my_feature.yaml

    ---
    patterns:
        - rulename: future simple be-going-to passive
        # This is a list of 5 tokens (i.e. 5 words)
          tokens:
            - {TAG: {IN: ["VBP", "VBZ"]}, DEP: "aux", OP: "+"}
            - {TAG: "VBG", OP: "+", LEMMA: "go"}
            - {TAG: "TO", DEP: "aux", OP: "+"}
            - {TAG: "VB", DEP: "auxpass", LEMMA: "be"}
            - {TAG: "VBN", OP: "+"}
---

##### Token: Ditransitive/Trivalency

---
    # my_feature.yaml

    ---
    patterns:
        - rulename: ditransitive
        # This is a list of 4 tokens minimum with some degree of recursivity
          tokens:
            - {DEP: "nsubj"}
            - {OP: "*"}  # Indicates possible filler words between the tokens
            - {DEP: "ROOT"}
            - {OP: "*"}
            - {DEP: {IN: ["dobj", "iobj", "pobj", "dative"]}}
            - {OP: "*"}
            - {DEP: {IN: ["dobj", "iobj", "pobj", "dative"]}}
---

### Component: Patterns

Each `Pattern` in `patterns` has two properties: 

1. `rulename: str`                      -- the name given to the `Pattern` with the corresponding `spacy.tokens.Token` (see above)
1. `tokens: list[spacy.tokens.Token]`   -- the grammatical pattern

---
    # transitivity.yaml

    ---
    meta:
        how_many_matches: one

    patterns:
        - rulename: ditransitive
          tokens:
              - {DEP: "nsubj"}
              - {OP: "*"}
              - {DEP: "ROOT"}
              - {OP: "*"}
              - {DEP: {IN: ["dobj", "iobj", "pobj", "dative"]}}
              - {OP: "*"}
              - {DEP: {IN: ["dobj", "iobj", "pobj", "dative"]}}

        - rulename: transitive
          tokens:
              - {DEP: "nsubj"}
              - {OP: "*"}
              - {DEP: "ROOT"}
              - {OP: "*"}
              - {DEP: "dobj"}

        - rulename: intransitive
          tokens:
              - {DEP: "nsubj", LOWER: {NOT_IN: ["it"]}}
              - {OP: "*"}
              - {DEP: "ROOT"}

        - rulename: impersonal
          tokens:
              - {TAG: "PRP", DEP: "nsubj", LOWER: "it"}
              - {OP: "*"}
              - {DEP: "ROOT"}
---

### Component: Patternset YAML Files

The `patternsets` expand the capabilities of the `GrammarDetector` to detect for new features. The `patternsets` are created by loading YAML files containing these three properties: 

1. `patterns: list[Pattern]`            -- an array of named sets of tokens
1. `meta: dict[str, Union[str, bool]]`  -- a configuration object to modify input/output
1. `tests: list[Test]`                  -- an array of tests to validate the accuracy of the `patterns`

Internally, this data from the `patternset` file is converted into a `PatternSet`.

#### Patternset Files: Example for Active/Passive Voice

---
    # voices.yaml

    ---
    meta:
        how_many_matches: one

    patterns:
        - rulename: active
          tokens:
              - {DEP: "aux", OP: "*"}
              - {DEP: "ROOT"}

        - rulename: passive
          tokens:
              - {DEP: "aux", OP: "*"}
              - {DEP: "auxpass", OP: "+"}
              - {TAG: "VBN", DEP: "ROOT"}

    tests:
        - input: The cat was chased by the dog.
          rulenames:
              - passive
          spans:
              - was chased

        - input: The dog chased the cat.
          rulenames:
              - active
          spans:
              - chased
---

#### Patternset Files: 1) Defining Rules via `patterns`

The `patterns: list[Pattern]` list contains rules and grammatical patterns with the following properties:

* `rulename: str`                       -- the name of the grammatical pattern (e.g. "present simple")
* `tokens: list[spacy.tokens.Token]`    -- the tokens of the grammatical pattern

#### Patternset Files: 2) Configuring via `meta`

The `meta` dict contains several options for modifying the input and/or output:

* `extract_noun_chunks: bool`   -- fragment input into nouns before running the detector (default false)
* `how_many_matches: str`       -- if "all", then get all matches; if "one", then get the best match
* `skip_tests: bool`            -- if true, then skip all tests in the file when running the unittests

#### Patternset Files: 3) Testing via `tests`

The `tests` list contains unittests with the following properties:

* `input: list[str]`        -- the sentence, clause, or phrase to be tested
* `rulenames: list[str]`    -- the expected rulenames
* `spans: list[str]`        -- the expected matching text
* `skip: bool`              -- if true, then skip this test (but not the others)

Each test must contain 1) the `input` and 2) the `rulenames` and/or the `spans`. Execute the following to run the tests: `$ python -m unittest`. Testing external patternsets is not yet supported but is a high priority.

### Component: PatternSetRepository

The `PatternSetRepository` reads a `patternset` YAML file and converts it into an internal `PatternSet`. The stored `PatternSets` can be retrieved individually by referencing its name as the cache key or retrieved collectively as a `list[PatternSet]`. The `PatternSetRepository` extends the `Repository[Generic[T]]` helper class for creating, caching, and querying.

### Component: PatternSetMatcher

The `PatternSetMatcher` is a wrapper class that is composed of an inner `spacy.matcher.Matcher` and logic to interpret `PatternSets`. The patterns defined in the `PatternSets` are automatically loaded into the inner `Matcher`. The raw matches from the inner `Matcher` are then converted into a reader-friendly format.

### Component: Detector

The `Detector` is the internal entrypoint by which a sentence, clause, or phrase is analyzed. A `Detector` contains one `PatternSet` and one `PatternSetMatcher`. Each `Detector` is bound to the specific grammatical feature of the `PatternSet`. After loading the `GrammarDetector`, its `Detectors` can be accessed via the `detectors` property. This permits running them manually and reusing them. Since the `GrammarDetector` and `Detectors` are not bound to its text input to be analyzed, they can be reused.  

### Component: DetectorRepository

The `DetectorRepository` is responsible for creating and storing `Detectors`. It is wrapped by the `GrammarDetector` class, the main entrypoint. The repository manages the `PatternSetRepository` and loads its `PatternSets` into the `PatternSetMatchers`. The `DetectorRepository` extends the `Repository[Generic[T]]` helper class for creating, caching, and querying.

## Contributing

This tool is only as good as the `patternset` YAML files that support it. The primary ways to contribute to this project:

* Creating and improving `patterns` in new/existing `patternset` YAML files
* Adding `tests` to existing `patternset` YAML files
* Adding new `meta` configuration options and features to the codebase

Cloning the repository: 
    `$ git clone TODO: add github URL`

Running the `GrammarDetector` from the repository: 
    `$ python -m src "The dog chased the cat into the house."`

Running the `patternset` unittests from the repository: 
    `$ python -m unittest`

To add new grammatical features or improve existing features, focus your efforts on the `patternsets` directory and its YAML files. You may find the token tables included in the info-level logs (exposed by setting `verbose` to `True`) to be helpful when creating or expanding patterns. Submissions of `patternset` files will be rejected if they do not include tests for each pattern.

TODO: add the github URL to the instructions for cloning the repository

## Authors

Steven Kyle Crawford

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the GNU General Public License V3. See the LICENSE.txt file for details.

## Acknowledgments

* [spaCy](https://spacy.io/) - free open-source library for Natural Language Processing in Python ([license](https://github.com/explosion/spaCy/blob/master/LICENSE))
