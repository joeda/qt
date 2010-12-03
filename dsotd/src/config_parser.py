#!/usr/bin/env python

import os
import json

CONFIG_FILE = "config.json"

class ConfigParser():

	def __init__(self, config_dir=None):
		self.config_dir = config_dir

	def setup_config(self):

		# The directories follow the freedesktop.org standards, except that
		# custom applets go to XDG_CONFIG_HOME/dsotd/applets
		if not self.config_dir:
			if os.environ.has_key("XDG_CONFIG_HOME"):
				self.config_dir = os.path.join(os.environ["XDG_CONFIG_HOME"], "dsotd")
			else:
				self.config_dir = os.path.join(os.environ["HOME"], ".config/dsotd")
		if not os.access(os.path.join(self.config_dir, CONFIG_FILE), os.R_OK):
			raise IOError("No configuration file found!")

		conffile = open(os.path.join(self.config_dir, CONFIG_FILE))
		self.config = json.load(conffile)
		return self.config
