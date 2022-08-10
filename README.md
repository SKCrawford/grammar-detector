# Syntax Detector

A tool for detecting syntactic features in sentences, clauses, and phrases. These features are defined in YAML files called `patternset`s, which means that no additional code is necessary. Instead of writing code for an endless list of new features, these YAML files serve as the basis for expanding the capabilities of the `SyntaxDetector`. The input text to be analyzed is then compared against the patterns defined within the `patternset` YAML files. In other words, `patternset`s allow for supporting new features to detect. Some features are built-in while other features may be added by users. For each `patternset` file, a `Detector` is created using the patterns and configuration options defined within the `patternset` itself. 

This tool offers the ability to **detect for syntactic features without additional code**; patternset YMAL files created manually can easily be added to the `SyntaxDetector`. Detection accuracy is determined by the accuracy of the patterns in these files. *In essence, garbage in garbage out.*

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

* python (>=3.6)
* pyyaml
* spacy
* spacy-lookups-data
* tabulate

Dev dependencies:

* black
* mypy
* python-lsp-server
* types-pyyaml
* types-tabulate
* types-setuptools

## Example usage

### Running the SyntaxDetector

1. Construct the `SyntaxDetector`
1. Call `configure()` then `load()`
1. Run the instance on the input using the `SyntaxDetector.__call__(self, input: str)` method

Sample code:

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

### Using the results

Sample code:

        sentence: str = "The man gave the woman a rose."
        results: dict[str, list[Match]] = syndet(sentence)

        print(results)
        # prints the following:
        {
            'The man gave the woman a rose.': {
                'determiners': [<definite: The man>, <definite: the woman>, <indefinite: a rose>],
                'persons': [<3rd: man>, <3rd: woman>, <3rd: rose>], 
                'tense_aspects': [<past simple: gave>],
                'transitivity': [<ditransitive: man gave the woman a rose>],
                'voices': [<active: gave>]
            }
        }

        feature = "tense_aspects"
        verb_tense = results[sentence][feature][0]
        print(verb_tense)  # prints <past simple: gave>
        print(verb_tense.rulename)  # prints "past simple"
        print(verb_tense.span)  # prints "gave"

## Components of the SyntaxDetector

These components are ordered from smallest to largest.

### Component: Token

The smallest atom in the tool is the `spacy.tokens.Token` class. Each `Token` represents a single word. A `list[Token]` represents a chain of words. Each token contains a `TAG` (tag) and/or a `DEP` (dependency). Optionally, an `OP` (operation) may be included. `TAG`s are broad categories (e.g. 'PUNCT' for punctuation) and `DEP`s are narrow categories (e.g. 'HYPH' for hyphen, 'LS' for list item marker, 'NFP' for superfluous, etc.)

Lists of `Token`s are used in `patternset` YAML files to define syntactic patterns.

#### Examples of Tokens

##### Token: Present Simple Verb

        # This is a single token (i.e. 1 word)
        - {TAG: {IN: ["VBP", "VBZ"]},

##### Token: Passive Auxiliary Verb

        # This is also a single token (i.e. 1 word)
        - {
          TAG: {IN: ["VBP", "VBZ"]},
          DEP: "auxpass",
          LEMMA: "be",
          OP: "+"
        }

##### Token: Future Simple Be-going-to Passive

        # This is a list of 5 tokens (i.e. 5 words)
        - {TAG: {IN: ["VBP", "VBZ"]}, DEP: "aux", OP: "+"}
        - {TAG: "VBG", OP: "+", LEMMA: "go"}
        - {TAG: "TO", DEP: "aux", OP: "+"}
        - {TAG: "VB", DEP: "auxpass", LEMMA: "be"}
        - {TAG: "VBN", OP: "+"}

##### Token: Ditransitive/Trivalency

        # This is a list of 4 tokens minimum with some degree of recursivity
        # OP: "*" indicates possible filler words between the tokens
        - {DEP: "nsubj"}
        - {OP: "*"}
        - {DEP: "ROOT"}
        - {OP: "*"}
        - {DEP: {IN: ["dobj", "iobj", "pobj", "dative"]}}
        - {OP: "*"}
        - {DEP: {IN: ["dobj", "iobj", "pobj", "dative"]}}

### Component: Patterns

Each `Pattern` in `patterns` has two properties: 

1. `rulename: str` -- the name given to the `Pattern` with the corresponding `spacy.tokens.Token` (see above)
1. `span: str` -- the fragment of the input that matches the `Token`s

Here are some example patterns:
TODO - add example patterns

### Component: Patternsets

`Patternsets` are the core of the `SyntaxDetector`. The `patternsets`s are created by loading YAML files containing these three properties: 

1. `patterns: list[Pattern]`    -- a list of named sets of tokens
1. `meta: dict[str, primitive]` -- a configuration dict to modify input/output
1. `tests: list[Test]`          -- a list of tests to validate the accuracy of the `patterns`

Internally, this data from the `patternset` file is converted into a `patterns.PatternSet`.

#### Patternsets: Defining Rules via `patterns`

The `patterns: list[Pattern]` list contains rules and syntactic patterns with the following properties:

* `rulename: str`
* `tokens: list[spacy.tokens.Token]`

#### Patternsets: Configuring via `meta`

The `meta` dict contains several options for modifying the input and/or output:

* `extract_noun_chunks: bool`   -- fragment input into nouns before running the detector (default false)
* `how_many_matches: str`       -- if "all", then get all matches; if "one", then get the best match
* `skip_tests: bool`            -- if true, then skip all tests in the file

#### Patternsets: Testing via `tests`

The `tests` list contains unittests with the following properties:

* `input: list[str]`       -- the sentence, clause, or phrase to be tested
* `rulenames: list[str]`   -- the expected rulenames
* `spans: list[str]`       -- the expected matching text

Each test must contain 1) the input and 2) the rulenames and/or the spans. To run the tests: `$ python -m unittest`. Testing external patternsets is not yet supported but is high priority.

### Component: PatternSetRepository

The `PatternSetRepository` extends the `Repository[Generic[T]]` helper class for creating, caching, and querying. It is responsible for interpreting a `patternset` YAML file and converting the data into an internal `patterns.PatternSet`. The stored `PatternSet`s can be retrieved by referencing its name as the cache key.


### Component: PatternSetMatcher

The `PatternSetMatcher` is a wrapper class that is composed of an inner `spacy.matcher.Matcher` and logic to interpret `PatternSet`s. The patterns defined in the `PatternSet`s are automatically loaded into the inner `Matcher`. The raw matches from the inner `Matcher` are converted into a reader-friendly format.

### Component: Detector

The `Detector` is the entrypoint by which a sentence, clause, or phrase is analyzed. Each `Detector` is bound to a specific syntactic feature, which is in turn bound to a `PatternSet`. After loading the `SyntaxDetector`, its `Detector`s can be accessed via the `detectors` property. This permits running them manually. Since the `SyntaxDetector` and `Detector`s are not bound to its text input to be analyzed, they can be reused.

### Component: DetectorRepository

The `DetectorRepository` extends the `Repository[Generic[T]]` helper class for creating, caching, and querying. It is responsible for creating new `Detector`s. The repository manages the `PatternSetRepository` and loads its `PatternSet`s into the `PatternSetMatcher`s.

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
