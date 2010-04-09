# this import alias is necessary to provide backwards compatibility with earlier
# versions of RichDocument which created their own attachment content types
# in this location.

from Products.SimpleAttachment.content import FileAttachment, ImageAttachment
