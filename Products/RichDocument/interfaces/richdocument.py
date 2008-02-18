from Products.ATContentTypes.interface import IATDocument

# This is a marker interface. By having RichDocument declare that it implements
# IRichDocument, we are asserting that it also supports IATDocument and 
# everything that interface declares

class IRichDocument(IATDocument):
    """RichDocument marker interface
    """

