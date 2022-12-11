import sys
import os

# Configuration file for the Sphinx documentation builder.
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'EconExplain'
copyright = '2022, Kenneth Lew'
author = 'Kenneth Lew'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

sys.path.insert(0, os.path.abspath('..'))

extensions = [
    "sphinx_design",
    "sphinx.ext.mathjax",
    "hoverxref.extension"
]

templates_path = ['_templates']
exclude_patterns = []

source_suffix = ".rst"
master_doc = "index"

hoverxref_roles = ["term"]
hoverxref_role_types = {
    "term": "tooltip",
}
# Required to display LaTeX in hover content
hoverxref_mathjax = True
# Use MathJax3 for better page loading times
mathjax_path = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = "EconExplain"
html_theme = 'furo'
html_static_path = ['_static']

html_logo = "_static/icon.png"
html_favicon = "_static/favicon.ico"
html_css_files = [
    "custom.css",
]

html_theme_options = {

}
