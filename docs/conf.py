project = 'django-email-from-template'
version = ''
release = ''
copyright = '2016 Chris Lamb'

html_theme = 'nature'
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx']
html_title = "%s documentation" % project
master_doc = 'index'
exclude_trees = ['_build']
templates_path = ['_templates']
latex_documents = [
  ('index', '%s.tex' % project, html_title, u'Chris Lamb', 'manual'),
]
intersphinx_mapping = {'http://docs.python.org/': None}
