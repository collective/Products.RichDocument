"""A document type which may contain directly uploaded images and attachments"""

__author__  = 'Martin Aspeli <optilude@gmx.net>'
__docformat__ = 'plaintext'

from zope.interface import implements

from AccessControl import ClassSecurityInfo

try:
  from Products.LinguaPlone.public import *
except ImportError:
  # No multilingual support
  from Products.Archetypes.public import *

from Products.RichDocument.interfaces import IRichDocument

from Products.SimpleAttachment.widget import AttachmentsManagerWidget
from Products.SimpleAttachment.widget import ImagesManagerWidget

from Products.ATContentTypes.content.document import ATDocument
from Products.ATContentTypes.content.document import finalizeATCTSchema

from Products.CMFPlone.interfaces import INonStructuralFolder

# Copy the ATDocument schema (to avoid modifying the original) and append our
# own fields for the images and attachments manager widgets.
RichDocumentSchema = ATDocument.schema.copy() + Schema((

        BooleanField('displayImages',
            default=False,
            languageIndependent=0,
            widget=ImagesManagerWidget(
                description="If selected, a list of uploaded images will be "
                             "presented at the bottom of the document to allow "
                             "them to be easily downloaded.",
                description_msgid='RichDocument_help_displayImages',
                i18n_domain='richdocument',
                label="""Display images download box""",
                label_msgid='RichDocument_label_displayImages',
            ),
        ),

        BooleanField('displayAttachments',
            default=True,
            languageIndependent=0,
            widget=AttachmentsManagerWidget(
                description="If selected, a list of uploaded attachments will be "
                             "presented at the bottom of the document to allow "
                             "them to be easily downloaded",
                description_msgid='RichDocument_help_displayAttachments',
                i18n_domain='richdocument',
                label="""Display attachments download box""",
                label_msgid='RichDocument_label_displayAttachments',
            ),
        ),

    ),)

# Finalise the schema according to ATContentTypes standards. This basically
# moves the Related items and Allow discussion fields to the bottom of the
# form. See ATContentTypes.content.schemata for details.
finalizeATCTSchema(RichDocumentSchema)

# Declare our class to be first a folderish object, and second get all the
# fields from ATDocument.

## class RichDocument(ATDocument, OrderedBaseFolder):
class RichDocument(OrderedBaseFolder, ATDocument):
    """A document which may contain directly uploaded images and attachments."""

    implements(INonStructuralFolder, IRichDocument)

    # Standard content type setup
    portal_type = meta_type = 'RichDocument'
    schema = RichDocumentSchema

    # Make sure we get title-to-id generation when an object is created
    _at_rename_after_creation = True

    # This method, from ISelectableBrowserDefault, is used to check whether
    # the "Choose content item to use as deafult view" option will be
    # presented. This makes sense for folders, but not for RichDocument, so
    # always disallow
    def canSetDefaultPage(self):
        return False

    # enable FTP/WebDAV and friends
    PUT = ATDocument.PUT

    def processForm(self, data=1, metadata=0, REQUEST=None, values=None):
        ATDocument.processForm(self, data=data, metadata=metadata,
               REQUEST=REQUEST, values=values)

        request = REQUEST or self.REQUEST
        if values:
            form = values
        else:
            form = request.form

        if "attachmentFile" in form and form["attachmentFile"]:
            self.widget_attachmentsmanager_upload(state=None)
        if "imageFile" in form and form["imageFile"]:
            self.widget_imagesmanager_upload(state=None)

registerType(RichDocument)
