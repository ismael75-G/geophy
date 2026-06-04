import os
import sys

# Indique à Sphinx de chercher votre code un dossier plus haut (dans la racine du projet)
sys.path.insert(0, os.path.abspath("../../"))

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",  # Optionnel : recommandé si vous écrivez des commentaires au format Google ou NumPy
    "sphinx_rtd_theme",  # Votre thème Read the Docs fraîchement installé
]

html_theme = "sphinx_rtd_theme"

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'geophy'
copyright = '2026, ismael'
author = 'ismael'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
