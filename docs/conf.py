# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'calculator'
copyright = '2026, kbuzar'
author = 'kbuzar'
release = '0.0.11'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',       # Supports numpy and google style docstrings
    'sphinx_rtd_theme',          # Required for the Read the Docs theme
    'sphinx_autodoc_typehints',  # Uses Python type hints in the docs
    'autoapi.extension'
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Path to your source code directory (relative to conf.py)
autoapi_dirs = ['../calculator']
