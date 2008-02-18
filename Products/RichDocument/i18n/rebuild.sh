#!/bin/bash

PYTHON=/usr/bin/python
I18NDUDE=$INSTANCE_HOME/Products/i18ndude/i18ndude

if [ ! -e $I18NDUDE ]; then
    echo "Unable to locate i18ndude utility!"
    exit 1
fi

cd `dirname $0`

PRODUCT_DIR=`dirname $PWD`
PRODUCT=`basename $PRODUCT_DIR`
I18NDOMAIN=richdocument
POT=$I18NDOMAIN.pot
LOG=rebuild.log

echo -n "Rebuilding to $POT, this can take a while..."

# Using --merge the resulting file is kept sorted by msgid
$PYTHON $I18NDUDE rebuild-pot \
  --pot $POT \
  --create $I18NDOMAIN \
  --merge manual.pot \
  $PRODUCT_DIR/skins/ >$LOG 2>&1

# Made paths relative to the Product directory
sed -ri "s,$PRODUCT_DIR,\.,g" $POT

echo " done. Full report at $LOG."

exit 0
