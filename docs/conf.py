import re

project = u'Sidings Media Documentation'
slug = re.sub(r'\W+', '-', project.lower())
author = u'Sidings Media'
copyright = author

latex_documents = [
  ('index', '{0}.tex'.format(slug), project, author, 'manual'),
]

man_pages = [
    ('index', slug, project, [author], 1)
]

texinfo_documents = [
  ('index', slug, project, author, slug, project, 'Miscellaneous'),
]