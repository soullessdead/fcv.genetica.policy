# -*- coding: utf-8 -*-
import logging
from plone import api
from Products.ATContentTypes.lib import constraintypes
from fcv.genetica.policy.config import PROJECTNAME

logger = logging.getLogger(PROJECTNAME)

def constrain_types(folder, allowed_types):
    '''Constrain addable types in folder.
    '''

    folder.setConstrainTypesMode(constraintypes.ENABLED)
    folder.setImmediatelyAddableTypes(allowed_types)
    folder.setLocallyAllowedTypes(allowed_types)

def remove_defaults_nav(portal):
    '''Remove defaults navegations and contents'''

    items_removable = ['front-page']
    for item in items_removable:
      if hasattr(portal, item):
        try:
          api.content.delete(obj=portal[item])
          logger.info("Deleted {0} item".format(item))
        except AttributeError:
          logger.info("No {0} item detected. Hmm... strange. Continuing....".format(item))

def create_defaults_contents(portal):
    '''create defaults contents'''

    # Create "Articulos Veterinarios Venezolanos" section (crear carpetas)
    title = u'Articulos Veterinarios Venezolanos'
    obj = api.content.create(type='Folder', title=title, container=portal)
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj_contrain_types = ['Folder', 'Document', 'File', 'Image', 'collective.cover.content']
    constrain_types(obj, obj_contrain_types)
    api.content.transition(obj,'publish')
    logger.info("Created the {0} item".format(obj))

    # Create "Genetica Animal" section (crear carpetas)
    title = u'Genetica Animal'
    obj = api.content.create(type='Folder', title=title, container=portal)
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj_contrain_types = ['Folder', 'Document', 'File', 'Image', 'collective.cover.content']
    constrain_types(obj, obj_contrain_types)
    api.content.transition(obj,'publish')
    logger.info("Created the {0} item".format(obj))

    # Create "Documentales" section (crear carpetas)
    title = u'Documentales'
    obj = api.content.create(type='Folder', title=title, container=portal)
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj_contrain_types = ['Folder', 'Document', 'File', 'Image', 'collective.cover.content']
    constrain_types(obj, obj_contrain_types)
    api.content.transition(obj,'publish')
    logger.info("Created the {0} item".format(obj))

    # Rename "Agenda" section (renombrar objeto en plone)
    obj = portal['events']
    api.content.rename(obj=obj, new_id="agenda")
    title = u'Agenda'
    obj.setTitle(title)
    obj.reindexObject('Title')
    logger.info("Renamed the {0} item".format(obj))

    #Create Products.CMFBibliographyAT section
    title = u'Bibliografias'
    obj = api.content.create(type='BibliographyFolder', title=title, container=portal)
    obj.setTitle(title)
    obj.reindexObject('Title')
    #obj_contrain_types = ['', '', '', '', '', '', '']
    #constrain_types(obj, obj_contrain_types)
    api.content.transition(obj,'publish')
    logger.info("Created the {0} item".format(obj))
    
    #Create FacultyStaffDirectory section
    title = u'Personal'
    obj = api.content.create(type='FSDFacultyStaffDirectory', title=title, container=portal)
    obj.setTitle(title)
    obj.reindexObject('Title')
    #obj_contrain_types = ['FSDCommittessFolder', 'FSDSpecialtiesFolder', 'FSDClassification', 'Topic', 'FSDDepartament', 'FSDPerson', 'Document']
    #constrain_types(obj, obj_contrain_types)
    api.content.transition(obj,'publish')
    logger.info("Created the {0} item".format(obj))

def create_admin_user(portal):
    """Create admin user """
    properties = dict(
      fullname='Webmaster',
      location='Maracaibo, Zulia',
    )

    user = api.user.create(
      username='administrador',
      email='administrador@fcv.luz.edu.ve',
      properties=properties,
      password='administrador'
    )
    logger.info("Create the {0} user".format(user))

    api.user.grant_roles(username='administrador',
      roles=['Manager']
    )
    logger.info("Granted the Manager rol to user created")

def setupVarious(context):
    """ miscellaneous import steps for setup """
    if context.readDataFile('fcv.genetica.policy_various.txt') is None:
        return

    portal = api.portal.get()
    # aquí va el código particular
    remove_defaults_nav(portal)
    create_defaults_contents(portal)
    create_admin_user(portal)