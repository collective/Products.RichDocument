from plone.outputfilters.browser.resolveuid import uuidFor
from Products.TinyMCE import TMCEMessageFactory as _
from Products.RichDocument.interfaces import IRichDocument
from Products.TinyMCE.adapters.Upload import Upload as BaseUpload
from Products.TinyMCE.adapters.interfaces.Upload import IUpload
from Products.TinyMCE.interfaces.utility import ITinyMCE
from Products.CMFCore.utils import getToolByName
from zope.interface import implements
from zope.component import adapts
from zope.component import getUtility
from zope.component import getGlobalSiteManager


class Upload(BaseUpload):
    implements(IUpload)
    adapts(IRichDocument)

    def upload(self):
        """Adds uploaded file"""

        context = self.context
        request = context.REQUEST
        ctr_tool = getToolByName(self.context, 'content_type_registry')
        id = request['uploadfile'].filename

        content_type = request['uploadfile'].headers["Content-Type"]
        typename = ctr_tool.findTypeName(id, content_type, "")

        # Because this is a RichDocument, the contained types are Attachments
        if typename in ('File', 'Image'):
            typename = typename + 'Attachment'

        # Permission checks based on code by Danny Bloemendaal

        # 1) check if we are allowed to create an Image in folder
        if not typename in [t.id for t in context.getAllowedTypes()]:
            return self.errorMessage(_("Not allowed to upload a file of this type to this folder"))

        # 2) check if the current user has permissions to add stuff
        if not context.portal_membership.checkPermission('Add portal content', context):
            return self.errorMessage(_("You do not have permission to upload files in this folder"))

        # Get an unused filename without path
        id = self.cleanupFilename(id)

        title = request['uploadtitle']
        description = request['uploaddescription']

        newid = context.invokeFactory(type_name=typename, id=id)

        if newid is None or newid == '':
            newid = id

        obj = getattr(context, newid, None)

        # Set title + description.
        # Attempt to use Archetypes mutator if there is one, in case it uses a custom storage

        if title:
            try:
                obj.setTitle(title)
            except AttributeError:
                obj.title = title

        if description:
            try:
                obj.setDescription(description)
            except AttributeError:
                obj.description = description

        # set primary field
        pf = obj.getPrimaryField()
        pf.set(obj, request['uploadfile'])

        if not obj:
            return self.errorMessage(_("Could not upload the file"))

        obj.reindexObject()

        utility = getUtility(ITinyMCE)
        if utility.link_using_uids:
            return self.okMessage("resolveuid/%s" % (uuidFor(obj)))
        return self.okMessage("%s" % (obj.absolute_url()))

gsm = getGlobalSiteManager()
gsm.registerAdapter(Upload)
