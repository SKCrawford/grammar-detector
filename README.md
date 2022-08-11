# Syntax-Detector

A tool for detecting syntactic features in sentences, clauses, and phrases. These features are defined in YAML files called `patternsets`, which means that no additional code is necessary. Instead of writing code for an endless list of new features, these YAML files expand the capabilities of the `SyntaxDetector`. The input text to be analyzed is then compared against the patterns defined within the `patternset` YAML files. In other words, `patternsets` allow for supporting new features to detect. Some features are built-in while other features may be added manually. For each `patternset` file, a `Detector` is created using the patterns and configuration options defined within the `patternset` itself. 

This tool offers **the ability to detect for syntactic features without additional code**. New detectors can easily be added to the `SyntaxDetector` through the `patternset` YAML files. Detection accuracy is determined by the accuracy of the patterns in these files.

## Overview

The core of this tool is the `SyntaxDetector`. In this order, it must be:

1. Constructed via `__init__(self, **kwargs) -> None`
1. Configured via `configure(self) -> None`
1. Loaded via `load(self) -> None`

After loading, the `SyntaxDetector` can be used in two different ways:

1. Using the `SyntaxDetector.__call__(self, input: str)` method on the input to run **automatically**.
1. Looping through the `detectors: list[Detector]` property and using the `Detector.__call__(self, input: str)` method on the input to run **manually**.

## Dependencies

Dependencies:

* **python** (>=3.???)      -- frequent use of f-strings and type hints
* **pyyaml**                -- loading patternset YAML files
* **spacy**                 -- rule-based syntactic pattern matching
* **spacy-lookups-data**    -- spaCy dependency
* **tabulate**              -- printing token tables to write patterns

Dev dependencies:

* **black**                 -- opinionated code formatter
* **mypy**                  -- type checking
* **python-lsp-server**     -- IDE integration
* **types-pyyaml**          -- type checking
* **types-tabulate**        -- type checking  
* **types-setuptools**      -- type checking

## How to Install

`$ pip install syntax-detector`

## Example Usage

### Running the SyntaxDetector

1. Construct the `SyntaxDetector`
1. Call `configure()` then `load()`
1. Run the instance on the input using the `SyntaxDetector.__call__(self, input: str)` method

---
    # my_script.py
    settings = {  # default values
        dataset: "en_core_web_lg",
        exclude_builtin_patternsets: False,
        features: "all",
        patternset_path: "",  # External patternsets
        pretty_print: False,
        settings_path: "settings.yaml",
        verbose: False,
        very_verbose: False,
    }
    syndet = SyntaxDetector(**settings)  # optionally, pass in **settings
    syndet.configure()
    syndet.load()

    sentence: str = "The man gave the woman a rose."
    results: dict[str, list[Match]] = syndet(sentence)
---

### Using the Results

---
        # my_script.py
        sentence: str = "The man gave the woman a rose."
        results: dict[str, list[Match]] = syndet(sentence)

        print(results)
        # prints the following:
        # {
        #    'The man gave the woman a rose.': {
        #        'determiners': [<definite: The man>, <definite: the woman>, <indefinite: a rose>],
        #        'persons': [<3rd: man>, <3rd: woman>, <3rd: rose>], 
        #        'tense_aspects': [<past simple: gave>],
        #        'transitivity': [<ditransitive: man gave the woman a rose>],
        #        'voices': [<active: gave>]
        #    }
        # }

        feature = "tense_aspects"
        verb_tense = results[sentence][feature][0]
        print(verb_tense)  # prints <past simple: gave>
        print(verb_tense.rulename)  # prints "past simple"
        print(verb_tense.span)  # prints "gave"
---

## Components of the SyntaxDetector

This section describes the internal components used to build and run `Detectors`. Understanding how `patternset` files are created and loaded into the `SyntaxDetector` is critical to expanding on its built-in detectors. To expand on the built-in detectors of the `SyntaxDetector`, understanding how `patternset` YAML files are created, configured, and loaded is critical.

To load your own `patternset` files, pass the file or directory path to the `patternset_path` keyword argument when constructing the `SyntaxDetector`.

### Component: Token

The smallest atom is the `spacy.tokens.Token` class. Each `Token` represents a single word. A `list[Token]` represents a chain of words. Each token contains a `TAG` (tag) and/or a `DEP` (dependency). Optionally, an `OP` (operation) may be included. `TAGs` are broad categories (e.g. 'PUNCT' for punctuation) and `DEPs` are narrow categories (e.g. 'HYPH' for hyphen, 'LS' for list item marker, 'NFP' for superfluous, etc.)

Lists of `Tokens` are used in `patternset` YAML files to define syntactic patterns.

#### Examples of Tokens

##### Token: Present Simple Verb

---
        # my_feature.yaml
        patterns:
            - rulename: present simple verb
            # This is a single token (i.e. 1 word)
            - tokens:  
                - {TAG: {IN: ["VBP", "VBZ"]},
---

##### Token: Passive Auxiliary Verb

---
        # my_feature.yaml
        patterns:
            - rulename: passive auxiliary
            # This is also a single token (i.e. 1 word)
            - tokens:  
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
        patterns:
            - rulename: future simple be-going-to passive
            # This is a list of 5 tokens (i.e. 5 words)
            - tokens:  
                - {TAG: {IN: ["VBP", "VBZ"]}, DEP: "aux", OP: "+"}
                - {TAG: "VBG", OP: "+", LEMMA: "go"}
                - {TAG: "TO", DEP: "aux", OP: "+"}
                - {TAG: "VB", DEP: "auxpass", LEMMA: "be"}
                - {TAG: "VBN", OP: "+"}
---

##### Token: Ditransitive/Trivalency

---
        # my_feature.yaml
        
        

        # my_feature.yaml
        patterns:
            - rulename: future simple be-going-to passive
            # This is a list of 4 tokens minimum with some degree of recursivity        
            - tokens:  
                - {DEP: "nsubj"}
                # OP: "*" indicates possible filler words between the tokens
                - {OP: "*"}  
                - {DEP: "ROOT"}
                - {OP: "*"}
                - {DEP: {IN: ["dobj", "iobj", "pobj", "dative"]}}
                - {OP: "*"}
                - {DEP: {IN: ["dobj", "iobj", "pobj", "dative"]}}
---

### Component: Patterns

Each `Pattern` in `patterns` has two properties: 

1. `rulename: str` -- the name given to the `Pattern` with the corresponding `spacy.tokens.Token` (see above)
1. `span: str` -- the fragment of the input that matches the `Tokens`

---
    # transitivity.yaml
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

`Patternsets` are the core of the `SyntaxDetector`. The `patternsets` are created by loading YAML files containing these three properties: 

1. `patterns: list[Pattern]`    -- a list of named sets of tokens
1. `meta: dict[str, primitive]` -- a configuration dict to modify input/output
1. `tests: list[Test]`          -- a list of tests to validate the accuracy of the `patterns`

Internally, this data from the `patternset` file is converted into a `patterns.PatternSet`.

#### Patternset Files: Example for Active/Passive Voice

---
    # voices.yaml
    meta:
        extract_noun_chunks: false
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

The `patterns: list[Pattern]` list contains rules and syntactic patterns with the following properties:

* `rulename: str`                       -- the name of the syntactic pattern (e.g. "present simple")
* `tokens: list[spacy.tokens.Token]`    -- the tokens of the syntactic pattern

#### Patternset Files: 2) Configuring via `meta`

The `meta` dict contains several options for modifying the input and/or output:

* `extract_noun_chunks: bool`   -- fragment input into nouns before running the detector (default false)
* `how_many_matches: str`       -- if "all", then get all matches; if "one", then get the best match
* `skip_tests: bool`            -- if true, then skip all tests in the file

#### Patternset Files: 3) Testing via `tests`

The `tests` list contains unittests with the following properties:

* `input: list[str]`        -- the sentence, clause, or phrase to be tested
* `rulenames: list[str]`    -- the expected rulenames
* `spans: list[str]`        -- the expected matching text
* `skip: bool`              -- if true, then skip this test (but not the others)

Each test must contain 1) the input and 2) the rulenames and/or the spans. To run the tests: `$ python -m unittest`. Testing external patternsets is not yet supported but is high priority.

### Component: PatternSetRepository

The `PatternSetRepository` extends the `Repository[Generic[T]]` helper class for creating, caching, and querying. It is responsible for interpreting a `patternset` YAML file and converting the data into an internal `patterns.PatternSet`. The stored `PatternSets` can be retrieved by referencing its name as the cache key.


### Component: PatternSetMatcher

The `PatternSetMatcher` is a wrapper class that is composed of an inner `spacy.matcher.Matcher` and logic to interpret `PatternSets`. The patterns defined in the `PatternSets` are automatically loaded into the inner `Matcher`. The raw matches from the inner `Matcher` are converted into a reader-friendly format.

### Component: Detector

The `Detector` is the entrypoint by which a sentence, clause, or phrase is analyzed. Each `Detector` is bound to a specific syntactic feature, which is in turn bound to a `PatternSet`. After loading the `SyntaxDetector`, its `Detectors` can be accessed via the `detectors` property. This permits running them manually. Since the `SyntaxDetector` and `Detectors` are not bound to its text input to be analyzed, they can be reused.

### Component: DetectorRepository

The `DetectorRepository` extends the `Repository[Generic[T]]` helper class for creating, caching, and querying. It is responsible for creating new `Detectors`. The repository manages the `PatternSetRepository` and loads its `PatternSets` into the `PatternSetMatchers`.

## Contributing

There are three primary ways to contribute to this project:

* Creating and improving patterns in new/existing patternset YAML files
* Adding tests to existing patternset YAML files
* Adding new meta configuration options and features to the codebase

This project is only as good as the patternset YAML files that support it.

## Authors

Steven Kyle Crawford

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the GNU General Public License V3 - see the LICENSE.md file for details.

## Acknowledgments

* [spaCy](https://spacy.io/)
