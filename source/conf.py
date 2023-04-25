# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

import os
import sys
from shutil import copyfile
from pathlib import Path

sys.path.insert(0, os.path.abspath("../../"))
print(sys.path)
f = os.popen("make -f diagrams_source.mk")
for item in f.readlines():
    print(f)
print("diagrams is OK")
# -- Project information -----------------------------------------------------

project = "OpenRL"
copyright = "2023, OpenRL Contributors"
author = "OpenRL Contributors"

# The short X.Y version
version = ""
# The full version, including alpha/beta/rc tags
release = "0.0.2"

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "enum_tools.autoenum",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"


master_doc = "index"
print("READTHEDOCS:", os.environ.get("READTHEDOCS"))
print("READTHEDOCS_LANGUAGE:", os.environ.get("READTHEDOCS_LANGUAGE"))
# exit()

all_lang = ["en", "zh"]


def copy_files(lang):
    file_types = ("rst", "jpg", "png", "gif")

    source_file_dir = Path("../source_files")
    current_dir = Path("./")

    all_files = []
    for file_type in file_types:
        all_files.extend(source_file_dir.glob("**/*.{}".format(file_type)))

    for file in all_files:
        if file.is_file():
            need_exclude = False
            for exclude_lang in all_lang:
                if exclude_lang == lang:
                    continue
                if "_{}.rst".format(exclude_lang) in str(file):
                    need_exclude = True
                    break
            if need_exclude:
                continue
            file_abs_path = str(file.resolve())
            file_name = file_abs_path.split("source_files/")[-1]
            if "/" in file_name:
                file_directory = current_dir / "/".join(file_name.split("/")[:-1])
                if not file_directory.exists():
                    file_directory.mkdir(parents=True)

            if "_{}.rst".format(lang) in file_name:
                copyfile(file, current_dir / file_name.replace("_{}".format(lang), ""))
            else:
                copyfile(file, current_dir / file_name)


if (
    os.environ.get("READTHEDOCS") == "True"
    or os.environ.get("READTHEDOCS_LOC") == "True"
):
    lang = os.environ.get("READTHEDOCS_LANGUAGE")
    lang = lang.split("_")[0] if lang else None

    if lang in ["zh"]:
        copy_files(lang)
        # copyfile("index_{}.rst".format(lang), "index.rst")
    else:
        # copyfile("index_en.rst", "index.rst")
        copy_files("en")
    print("Copy files done!")


# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None

# -- Options for HTML output -------------------------------------------------
# en or zh_CN
rtd_lang = os.environ.get("READTHEDOCS_LANGUAGE") or "en"

import pytorch_sphinx_theme

html_theme = "pytorch_sphinx_theme"
html_theme_path = [pytorch_sphinx_theme.get_html_theme_path()]
html_theme_options = {
    "logo_url": "https://openrl-docs.readthedocs.io/{}/latest/".format(rtd_lang),
    "menu": [
        {"name": "GitHub", "url": "https://github.com/OpenRL-Lab/openrl"},
    ],
    # Specify the language of shared menu
    "menu_lang": rtd_lang,
}
html_static_path = ["_static"]
html_css_files = ["css/style.css"]

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "OpenRLdoc"

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, "OpenRL.tex", "OpenRL Documentation", "bao", "manual"),
]

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "OpenRL", "OpenRL Documentation", [author], 1)]

# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "OpenRL",
        "OpenRL Documentation",
        author,
        "OpenRL",
        "One line description of project.",
        "Miscellaneous",
    ),
]

# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]

# -- Extension configuration -------------------------------------------------
