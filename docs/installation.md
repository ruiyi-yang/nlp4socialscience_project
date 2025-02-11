# Installation Guide for `nlp4socialscience`

This document will guide you through the installation of the `nlp4socialscience` package.



### Setting Up a Virtual Environment (Recommended)

A virtual environment helps isolate dependencies and avoid conflicts with other projects on your system.

#### 1. On Linux/macOS:
```bash
python3 -m venv nlp_env
source nlp_env/bin/activate
```

#### 2. On Windows:
```bash
python -m venv nlp_env
nlp_env\Scripts\activate
```

Once activated, your terminal prompt should display the virtual environment name, e.g., `(nlp_env)`.

> **Tip:** To deactivate the virtual environment, simply run:
>
> ```bash
> deactivate
> ```



### Install the Package Using `pip`

To install the latest version of the package from PyPI:
```bash
pip install nlp4socialscience
```

Alternatively, if you have the source code locally and want to install it from there:
```bash
git clone https://github.com/ruiyi-yang/nlp4socialscience.git
cd nlp4socialscience
pip install .
```

> **Note:** Running the installation locally will also install all necessary dependencies listed in `setup.py` or `requirements.txt`.



### Installing Dependencies 

The package requires several dependencies for various NLP tasks. If they are not installed automatically, you can manually install them using:
```bash
pip install -r requirements.txt
```

The following libraries are required to run various components of the package:

- `numpy` – Numerical computations
- `pandas` – Data handling
- `nltk` – Natural Language Toolkit
- `spacy` – NLP framework for tokenization and NER
- `gensim` – Topic modeling
- `scikit-learn` – Machine learning models
- `matplotlib` – Data visualization
- `wordcloud` – Word cloud generation

You can verify the installation using:

```bash
pip freeze
```



### Download SpaCy Language Models

For **Named Entity Recognition (NER)**, you need SpaCy language models. By default, install the small English model (`en_core_web_sm`):

```bash
python -m spacy download en_core_web_sm
```

> **Tip:** If you need better accuracy or are working with larger datasets, you can use the medium or large models:
>
> ```bash
> python -m spacy download en_core_web_md  # Medium
> python -m spacy download en_core_web_lg  # Large
> ```



### Verifying the Installation

To check if the package has been installed successfully:
```bash
python -c "import nlp4socialscience; print('Installation successful!')"
```

You should see the message:

```nginx
Installation successful!
```



### Optional: Optional - Updating the Package

To keep the package up to date with the latest features and bug fixes:
```bash
pip install --upgrade nlp4socialscience
```



### Troubleshooting Common Issues

1. **Dependency Conflicts:** If you encounter issues related to version conflicts: 

   ```bash
   pip check
   ```
   This command will highlight any problematic dependencies. If conflicts persist, consider creating a new virtual environment.

2. **Missing Language Models (SpaCy):** If you get errors like `"OSError: [E050] Model not found"` while using NER, ensure the correct language model is installed:

   ```bash
   python -m spacy download en_core_web_sm
   ```

3. **Permission Issues:** If you encounter permission errors, try running the installation with elevated privileges:

   ```bash
   sudo pip install nlp4socialscience   ## for Linux/macOS
   ```



### Next Steps

- 📄 [**Quickstart Guide**](./quickstart.md) – Start using the package with examples for text preprocessing, sentiment analysis, and topic modeling.
- 🔧 [**API Reference**](./api_reference.md) – Explore the detailed API documentation for available functions.

For any issues or feature requests, please visit [**GitHub Issues**](https://github.com/ruiyi-yang/NLP4SocialScience/issues).

 
