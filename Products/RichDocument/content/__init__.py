
# This statement makes RichDocument available to import via:
#   from Products.RichDocument.content import RichDocument
# Without it, you would have to use:
#   from Products.RichDocument.content.RichDocument import RichDocument

from richdocument import RichDocument

# Do the same for images and attachments

from Products.SimpleAttachment.content import FileAttachment, ImageAttachment