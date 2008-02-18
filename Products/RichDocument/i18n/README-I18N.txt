RichDocument i18n Instructions

  First, make sure you have a copy of i18ndude[1] in your Products
  directory. You also can change the script files to use different
  paths that match your setup.

  Manual msgids from 'richdocument' i18n domain should be inserted into
  the manual.pot file. Manual msgids from 'plone' i18n domain should be
  inserted into the richdocument-plone.pot file.

  To rebuild the richdocument.pot file, looking for new msgids in all
  templates and python scripts files and merge them with manual.pot
  run::

    ./rebuild.sh

  To sync all the PO files from both 'richdocument' and 'plone' i18n
  domains run::

    ./sync.sh

  Note: you can run the commands above from any place. You aren't
  required to be inside the i18n directory.

.. [1] https://svn.plone.org/svn/collective/i18ndude/trunk
