#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'
post_build = aur_post_build

def pre_build():
  pypi_pre_build()

def post_build():
  pypi_post_build()

if __name__ == '__main__':
  single_main()

# vim:set ts=2 sw=2 et:
