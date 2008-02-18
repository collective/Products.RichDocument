# BBB for CMF 1.4
try:
    from Products.CMFCore.permissions import setDefaultRoles
except ImportError:
    from Products.CMFCore.CMFCorePermissions import setDefaultRoles

PROJECTNAME = "RichDocument"
DEFAULT_ADD_CONTENT_PERMISSION = "Add RichDocument"

setDefaultRoles(DEFAULT_ADD_CONTENT_PERMISSION, ('Manager', 'Owner',))