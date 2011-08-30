from Products.CMFCore import utils, DirectoryView
from Products.Archetypes.atapi import listTypes, process_types

import sys, content

from Products.SimpleAttachment import content as attachment_content
from Products.SimpleAttachment import widget

# Module aliases - we don't always get it right on the first try, but and we
# can't move modules around because things are stored in the ZODB with the
# full module path. However, we can create aliases for backwards compatability.

sys.modules['Products.RichDocument.RichDocument'] = content.richdocument
sys.modules['Products.RichDocument.FileAttachment'] = attachment_content.file
sys.modules['Products.RichDocument.ImageAttachment'] = attachment_content.image
sys.modules['Products.RichDocument.widgets'] = widget
sys.modules['Products.RichDocument.widget'] = widget
sys.modules['Products.RichDocument.ImagesManagerWidget'] = widget.images
sys.modules['Products.RichDocument.AttachmentsManagerWidget'] = widget.attachments

# Get configuration data, permissions
from Products.RichDocument.config import *

# Register skin directories so they can be added to portal_skins
DirectoryView.registerDirectory('skins', globals())

# Register the TinyMCE Upload adpater if TinyMCE is present
try:
    from Products.RichDocument import tinymce
except ImportError:
    pass

def initialize(context):

    # Import the type, which results in registerType() being called
    from content import RichDocument

    # initialize the content, including types and add permissions
    content_types, constructors, ftis = process_types(
        listTypes(PROJECTNAME),
        PROJECTNAME)

    utils.ContentInit(
        PROJECTNAME + ' Content',
        content_types      = content_types,
        permission         = DEFAULT_ADD_CONTENT_PERMISSION,
        extra_constructors = constructors,
        fti                = ftis,
        ).initialize(context)
