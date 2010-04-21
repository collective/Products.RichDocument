Introduction
============

  *by Martin Aspeli*

RichDocument is a document type which provides the same fields as the standard
Plone Document/Page type, but allows users to upload images directly into the
document during editing.

A RichDocument is a folderish type with Image and File as the only permitted
contained types. Two special widgets for managing contained images and
attachments are provided near the bottom of the edit form, though you have
to expand a collapsed fieldset to see them.

Once uploaded, images and attachments can be referenced in the document's body
text or inserted using editors such as kupu.

In addition, the user can optionally either automatically float the topmost
uploaded image at the top left of the page, or display a box of thumbnails
floating at the right of the page, on which the viewer can click to open
the full-size image in a pop-up window. This is achieved using the Plone 2.1
'display' menu.

RichDocument is released under the GNU General Public Licence, version 2.
Please see http://gnu.org for more details.

Installation
============

Install in the usual way, using the QuickInstaller or Plone's Add/Remove
Products control panel.

This version works with Plone 3 and 4 only. Version 2.0 works with 2.1 and
2.5. Version 1.0 works with Plone 2.0.

Please see the `Installing an Add-on Product`_ tutorial for more
information.

.. _Installing an Add-on Product : http://plone.org/documentation/tutorial/third-party-products/installing

Acknowlegements
===============
The ImagesManagerWidget was originally created for km|portal, a knowledge
management system aimed at small businesses (c) 2004 Martin Aspeli.

RichDocument extends ATContentTypes. Thanks to Christian Heimes, Alec
Mitchell and everyone else who made this such a useful framework.

The RichDocument view templates are derived from Plone's document_view.
The FileAttachment and ImageAttachment view templates are derived from
Plone's file_view and image_view templates respectively.

Dorneles Tremea contributed with some patches and added the i18n
infrastructure.

Known Issues and Potential Improvements
=======================================

- The templates use presentational markup and style attributes in some
  places and could do with a cleanup.

- It's not possible to upload images while the object is still in the
  portal_factory. If the object is in the factory while it is being edited for
  the first time and the user uploads an image, it will be instantiated into
  the target folder first.

- The image and attachment controls are submit buttons, managed via
  PortalFormController with custom actions registered during the installation.
  However, this button comes before the Save button on the form, and thus may
  steal the default button status - if the user presses Enter in the form, they
  may get a (benevolent) portal error message telling them they must upload an
  image.

- The only re-ordering support provided directly by the manager widgets
  is "move to top". This is useful in support of the single-image preview mode
  or to make an attachment in the attachments download box stand out, but more
  detailed re-ordering functionality may be desirable.
