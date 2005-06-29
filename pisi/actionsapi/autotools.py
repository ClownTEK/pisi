#!/usr/bin/python
# -*- coding: utf-8 -*-

# standard python modules
import os

# actions api modules
from config import config

def configure(parameters = ''):
    ''' FIXME: Düzgün hale getirilecek '''
    ''' parameters = '--with-nls --with-libusb --with-something-usefull '''
    dirs = config.dirs
    flags = config.flags

    configure_string = './configure --prefix=%s \
                --host=%s \
                --mandir=%s \
                --infodir=%s \
                --datadir=%s \
                --sysconfdir=%s \
                --localstatedir=%s \
                %s' % (dirs.defaultprefix,
                       flags.host,
                       dirs.man,
                       dirs.info,
                       dirs.data,
                       dirs.conf,
                       dirs.localstate,
                       parameters)

    os.system(configure_string)

def make():
    ''' FIXME: Düzgün hale getirilecek '''
    os.system('make')

def install():
    ''' FIXME: Düzgün hale getirilecek '''
    ''' dir_suffix = /var/tmp/pisi/ _paket_adı_ /image/ '''
    dirs = config.dirs

    dir_suffix = os.path.dirname(os.path.dirname(os.getcwd())) + \
        config.const.install_dir_suffix

    install_string = 'make prefix=%(prefix)s/%(defaultprefix)s \
                datadir=%(prefix)s/%(data)s \
                infodir=%(prefix)s/%(info)s \
                localstatedir=%(prefix)s/%(localstate)s \
                mandir=%(prefix)s/%(man)s \
                sysconfdir=%(prefix)s/%(conf)s \
                install' % {'prefix': dir_suffix,
                            'defaultprefix': dirs.defaultprefix,
                            'man': dirs.man,
                            'info': dirs.info,
                            'localstate': dirs.localstate,
                            'conf': dirs.conf,
                            'data': dirs.data}

    os.system(install_string)
