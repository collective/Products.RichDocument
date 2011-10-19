from Products.RichDocument.tests import base

class TestInstallation(base.RichDocumentTestCase):
    """Ensure product is properly installed"""

    def afterSetUp(self):
        self.css        = self.portal.portal_css
        self.tiny       = self.portal.portal_tinymce
        self.skins      = self.portal.portal_skins
        self.types      = self.portal.portal_types
        self.factory    = self.portal.portal_factory
        self.workflow   = self.portal.portal_workflow
        self.properties = self.portal.portal_properties

        self.metaTypes = ('RichDocument',)

    def testSkinLayersInstalled(self):
        self.failUnless('richdocument' in self.skins.objectIds())
        
    def testTypesInstalled(self):
        for t in self.metaTypes:
            self.failUnless(t in self.types.objectIds())

    def testPortalFactorySetup(self):
        self.failUnless('RichDocument' in self.factory.getFactoryTypes())

    def testParentMetaTypesNotToQuery(self):
        parentMetaTypesNotToQuery = self.properties.navtree_properties.getProperty('parentMetaTypesNotToQuery')
        self.failUnless('RichDocument' in parentMetaTypesNotToQuery)
    
    def testTinyResources(self):
        linkable = self.tiny.linkable.split('\n')
        self.failUnless('RichDocument' in linkable)
        
    def testSimpleAttachmentInstalled(self):
        self.failUnless('simpleattachment' in self.skins.objectIds())

class TestContentCreation(base.RichDocumentTestCase):
    """Ensure content types can be created and edited"""

    def afterSetUp(self):
        self.folder.invokeFactory('RichDocument', 'rd1')
        self.rd1 = getattr(self.folder, 'rd1')

    def testCreateRichDocument(self):
        self.failUnless('rd1' in self.folder.objectIds())

    def testEditRichDocument(self):
        self.rd1.setTitle('A title')
        self.rd1.setDescription('A description')
        self.rd1.setText('<p>Body text</p>')
        self.rd1.setDisplayImages(True)
        self.rd1.setDisplayAttachments(False)
        
        self.assertEqual(self.rd1.Title(), 'A title')
        self.assertEqual(self.rd1.Description(), 'A description')
        self.assertEqual(self.rd1.getText(), '<p>Body text</p>')
        self.assertEqual(self.rd1.getDisplayImages(), True)
        self.assertEqual(self.rd1.getDisplayAttachments(), False)

    def testCreateFileAttachment(self):
        self.rd1.invokeFactory('FileAttachment', 'f1')
        self.failUnless('f1' in self.rd1.objectIds())
        
    def testEditFileAttachment(self):
        self.rd1.invokeFactory('FileAttachment', 'f1')
        f1 = getattr(self.rd1, 'f1')

        f1.setTitle('File title')
        f1.setDescription('File description')
        f1.setFile('X')
        
        self.assertEqual(f1.Title(), 'File title')
        self.assertEqual(f1.Description(), 'File description')
        self.failIf(f1.getFile() is None)
    
    def testCreateFileAttachmentOutsideRichDocument(self):    
        self.assertRaises(ValueError, self.folder.invokeFactory, 'FileAttachment', 'f1')

    def testCreateImageAttachment(self):
        self.rd1.invokeFactory('ImageAttachment', 'i1')
        self.failUnless('i1' in self.rd1.objectIds())
        
    def testEditImageAttachment(self):
        self.rd1.invokeFactory('ImageAttachment', 'i1')
        i1 = getattr(self.rd1, 'i1')

        i1.setTitle('Image title')
        i1.setDescription('Image description')
        i1.setImage('X')
        
        self.assertEqual(i1.Title(), 'Image title')
        self.assertEqual(i1.Description(), 'Image description')
        self.failIf(i1.getImage() is None)
    
    def testCreateImageAttachmentOutsideRichDocument(self):    
        self.assertRaises(ValueError, self.folder.invokeFactory, 'ImageAttachment', 'i1')

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestInstallation))
    suite.addTest(makeSuite(TestContentCreation))
    return suite
