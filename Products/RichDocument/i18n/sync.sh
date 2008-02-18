#!/bin/bash

PYTHON=/usr/bin/python
I18NDUDE=$INSTANCE_HOME/Products/i18ndude/i18ndude

if [ ! -e $I18NDUDE ]; then
    echo "Unable to locate i18ndude utility!"
    exit 1
fi

cd `dirname $0`

for PO in richdocument-??.po richdocument-??-??.po ; do
    $PYTHON $I18NDUDE sync --pot richdocument.pot $PO
done

for PO in richdocument-plone*.po ; do
    $PYTHON $I18NDUDE sync --pot richdocument-plone.pot $PO
done
