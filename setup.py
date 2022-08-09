from setuptools import setup


setup(
    name="syntax-detector",

    version="0.1.0",

    description="A syntactic feature detector that reads in YAML files to create and configure matchers that scan sentences, clauses, or phrases.",

    py_modules=["SyntaxDetector"],

    package_dir={"": "src"},

    # Dependencies
    install_requires=[
        "pyyaml",
        "spacy",
        "spacy-lookups-data",
        "tabulate",
    ],

    # Dev dependencies
    extras_requires = {
        "dev": [
            "black",
            "mypy",
            "python-lsp-server",
            "types-pyyaml",
            "types-tabulate",
            "types-setuptools",
        ],
    },
)
