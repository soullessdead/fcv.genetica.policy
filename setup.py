from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='fcv.genetica.policy',
      version=version,
      description="Paquete que aplica configuraciones personalizada para el sitio",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='fcv genetica animal plone luz policy',
      author='Carlos Gonzalez',
      author_email='soulless_dead@hotmail.com',
      url='https://github.com/soullessdead/fcv.genetica.policy',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['fcv', 'fcv.genetica'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'Products.FacultyStaffDirectory',
          'Products.Ploneboard',
          'eea.facetednavigationtaxonomiccheckbox',
          'wildcard.media',
          'collective.portlet.twitter',
          'collective.cover',
          'fcv.genetica.theme',
      ],
      extras_require={
        'test': ['plone.app.testing'],
        },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
