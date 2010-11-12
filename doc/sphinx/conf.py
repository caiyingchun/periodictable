# -*- coding: utf-8 -*-
#
# Periodic Table documentation build configuration file, created by
# sphinx-quickstart on Tue Jun  2 11:16:08 2009.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.append(os.path.abspath('_extensions'+(os.path.dirname('../../periodictable'))))

import glob
sys.path.insert(0, os.path.abspath('.')) # needed for extension tests
#buildpath = glob.glob('../../build/lib*')[0]
#sys.path.insert(0, os.path.abspath(buildpath))
sys.path.insert(0, os.path.abspath('../..'))
sys.path.insert(0, os.path.abspath('_extensions'))


# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest',
              'sphinx.ext.coverage', 
              #'sphinx.ext.pngmath',
              'sphinx.ext.jsmath',
              #'only_directives',
              #'matplotlib.sphinxext.mathmpl',
              'matplotlib.sphinxext.only_directives',
              'matplotlib.sphinxext.plot_directive',
              'inheritance_diagram',
              'dollarmath',
             ]
jsmath_path = 'MathJax/MathJax.js'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Periodic Table'
copyright = u'2009, Paul Kienzle'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.9'
# The full version, including alpha/beta/rc tags.
release = '0.9'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['_*','build','MathJax','plots',
                 'shelltable','discoverer']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = 'default'
html_theme_options = {
    "rightsidebar":"False",
    "relbarbgcolor": "Gainsboro",
    #"codebgcolor": "Beige",
    "footertextcolor": "orange",
    "relbartextcolor": "Blue",
    "sidebarbgcolor": "white",
    "sidebarlinkcolor": "OrangeRed",
    "sidebartextcolor": "Navy",
    "linkcolor": "Blue",
    "relbarlinkcolor": "Blue"
    #"headtextcolor": "Teal"
    #"headbgcolor": "Oldlace",
}

html_style = 'site.css'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation PaleTurquoise.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "PeriodicTable"

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = "Home"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = '_static/periodic_logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'PeriodicTabledoc'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'PeriodicTable.tex', u'Periodic Table Documentation',
   u'Paul Kienzle', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''
LATEX_PREAMBLE=r"""
\renewcommand{\AA}{\text{\r{A}}} % Allow \AA in math mode
\usepackage[utf8]{inputenc}      % Allow unicode symbols in text
\DeclareUnicodeCharacter {00B7} {\ensuremath{\cdot}}   % cdot
\DeclareUnicodeCharacter {00B0} {\ensuremath{^\circ}}  % degrees
\DeclareUnicodeCharacter {212B} {\AA}                  % Angstrom
"""
latex_elements = {'preamble' : LATEX_PREAMBLE}

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True

# Which class/__init__ docstring to use: class, init, or both
autoclass_content = 'both'

# Autodoc member sort order: by class or by type
autodoc_member_order = 'groupwise'

if os.path.exists('rst_prolog'):
    with open('rst_prolog') as fid:
        rst_prolog = fid.read()
