# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

sys.path.insert(0, os.path.abspath('..'))
sys.path.append(os.path.abspath('extensions'))

project = 'passwordcrypto'
copyright = '2024, Muxutruk'
author = 'Muxutruk'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "builder",
    "sphinx.ext.autodoc", 
    "sphinx.ext.viewcode", 
    "sphinx.ext.todo", 
    "attributetable",
    ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']

html_style = "_static/custom.css"

autodoc_default_options = {
    "members": True,
    "show-inheritance": True,
}
