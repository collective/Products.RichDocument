from Products.CMFCore.permissions import setDefaultRoles

PROJECTNAME = "RichDocument"
DEFAULT_ADD_CONTENT_PERMISSION = "Add RichDocument"

setDefaultRoles(DEFAULT_ADD_CONTENT_PERMISSION, ('Manager', 'Owner',))
