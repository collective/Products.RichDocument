from Products.CMFCore.utils import getToolByName

from Products.SimpleAttachment.setuphandlers import registerImagesFormControllerActions
from Products.SimpleAttachment.setuphandlers import registerAttachmentsFormControllerActions

def setupRichDocument(context):
    if context.readDataFile('richdocument_various.txt') is None:
        return
    
    portal = context.getSite()
    
    qi = getToolByName(portal, 'portal_quickinstaller')
    if not (qi.isProductInstalled('Products.SimpleAttachment') or qi.isProductInstalled('SimpleAttachment') or qi.isProductInstalled('Attachment support')):
        qi.installProduct('Products.SimpleAttachment')
    
    # Set up form controller actions for the widgets to work
    registerAttachmentsFormControllerActions(portal, contentType = 'RichDocument', template = 'atct_edit')
    registerImagesFormControllerActions(portal, contentType = 'RichDocument', template = 'atct_edit')

    # Register form controller actions for LinguaPlone translate_item
    registerAttachmentsFormControllerActions(portal, contentType = 'RichDocument', template = 'translate_item')
    registerImagesFormControllerActions(portal, contentType = 'RichDocument', template = 'translate_item')
    
    # Make RichDocumnt objects linkable in kupu
    kupuTool = getToolByName(portal, 'kupu_library_tool', None)
    tinyTool = getToolByName(portal, 'portal_tinymce', None)
    
    if kupuTool:
        linkable = list(kupuTool.getPortalTypesForResourceType('linkable'))
        if 'RichDocument' not in linkable:
            linkable.append('RichDocument')
    
        # kupu_library_tool has an idiotic interface, basically written purely to
        # work with its configuration page. :-(
        kupuTool.updateResourceTypes(({'resource_type' : 'linkable',
                                       'old_type'      : 'linkable',
                                       'portal_types'  :  linkable},))

    if tinyTool:
        linkable = tinyTool.linkable.split('\n')
        linkable.append('RichDocument')
        tinyTool.linkable = '\n'.join(set(linkable))