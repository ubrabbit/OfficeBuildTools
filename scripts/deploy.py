#!/usr/bin/env python

import config
import base
import deploy_desktop
import deploy_builder
import deploy_server
import deploy_develop
import deploy_core

def make():
  if config.check_option("module", "desktop"):
    deploy_desktop.make()
  if config.check_option("module", "builder"):
    deploy_builder.make()
  if config.check_option("module", "server"):
    deploy_server.make()
  if config.check_option("module", "develop"):
    deploy_develop.make()
  if config.check_option("module", "core"):
    deploy_core.make()
  return
