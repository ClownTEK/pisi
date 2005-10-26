# Copyright (C) 2005, TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

import unittest
import os

import pisi.context as ctx
import pisi.api
import pisi.installdb
from pisi import util

class InstallDBTestCase(unittest.TestCase):

    def setUp(self):
        pisi.api.init(database = True, comar = False)


    def testRemoveDummy(self):
        ctx.installdb.remove('installtest')
        self.assert_(not ctx.installdb.is_installed('installtest'))
        pisi.api.finalize()
        
    def testInstall(self):
        ctx.installdb.purge('installtest')
        ctx.installdb.install('installtest', '0.1', '2', '3')
        pisi.api.finalize()

    def testRemovePurge(self):
        ctx.installdb.install('installtest', '0.1', '2', '3')
        self.assert_(ctx.installdb.is_installed('installtest'))
        ctx.installdb.remove('installtest')
        self.assert_(ctx.installdb.is_removed('installtest'))
        ctx.installdb.purge('installtest')
        self.assert_(not ctx.installdb.is_recorded('installtest'))
        pisi.api.finalize()

suite = unittest.makeSuite(InstallDBTestCase)
