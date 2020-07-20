#!/usr/bin/env python3
from lilaclib import *


def pre_build():
    update_pkgver_and_pkgrel(_G.newver.rstrip('Linux').lstrip())

def post_build():
    git_add_files('PKGBUILD')
    git_commit()

if __name__ == '__main__':
    single_main()

