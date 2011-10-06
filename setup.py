from setuptools import setup, find_packages
import os

version = '3.4'

setup(name='Products.RichDocument',
      version=version,
      description="Document type for Plone which allows users to upload " 
                  "images directly into the document during editing", 
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        ],
      keywords='Plone RichDocument attachments images files',
      author='Martin Aspeli',
      author_email='optilude@gmx.net',
      url='http://pypi.python.org/pypi/Products.RichDocument',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          "Products.SimpleAttachment>=3.4",
      ],
      )

