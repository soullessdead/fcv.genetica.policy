# -*- coding: utf-8 -*-
import logging
from plone import api
from fcv.genetica.policy.config import PROJECTNAME

logger = logging.getLogger(PROJECTNAME)

def remove_defaults_nav(portal):
    '''Remove defaults navegations and contents'''

    items_removable = ['news', 'events', 'Members', 'front-page']
    for item in items_removable:
      if hasattr(portal, item):
        try:
          api.content.delete(obj=portal[item])
          logger.info("Deleted {0} item".format(item))
        except AttributeError:
          logger.info("No {0} item detected. Hmm... strange. Continuing....".format(item))

def setupVarious(context):
    """ miscellaneous import steps for setup """
    if context.readDataFile('fcv.genetica.policy_various.txt') is None:
        return

    portal = api.portal.get()
    # aquí va el código particular
    remove_defaults_nav(portal)