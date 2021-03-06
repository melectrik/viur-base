# -*- coding: utf-8 -*-
#
# This is the ViUR default skeleton importer;
# If any other importing logic is wanted, please switch to manual import calls in this file, and remove
# the dynamic code provided below.
#

import os, logging

for skelModule in os.listdir(os.path.dirname(__file__)):
	if skelModule == "__init__.py" or not skelModule.endswith(".py"):
		continue

	try:
		__import__(skelModule[:-3], globals(), locals())
	except ImportError:
		logging.error("Unable to import skeleton %s" % skelModule[:-3])

	except:
		raise

del skelModule
