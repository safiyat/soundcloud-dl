################################################################################
# soundcloud-dl - Download tracks from Soundcloud                              #
# Copyright (C) 2017  Md Safiyat Reza                                          #
#                                                                              #
# This program is free software; you can redistribute it and/or modify         #
# it under the terms of the GNU General Public License as published by         #
# the Free Software Foundation; either version 2 of the License, or            #
# (at your option) any later version.                                          #
#                                                                              #
# This program is distributed in the hope that it will be useful,              #
# but WITHOUT ANY WARRANTY; without even the implied warranty of               #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
# GNU General Public License for more details.                                 #
#                                                                              #
# You should have received a copy of the GNU General Public License along      #
# with this program; if not, write to the Free Software Foundation, Inc.,      #
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.                  #
################################################################################

from __future__ import print_function
from ConfigParser import ConfigParser
import argparse
import os
import sys


class Config(object):

    def __init__(self, path=None):
        if not path:
            self.path = os.environ['HOME'] + '/.soundcloud-dl.conf'
        else:
            self.path = path
        self.conf = ConfigParser()

    def _write_conf(self, website, redirect_uri, client_id, client_secret):
        if not self.conf.has_section('credentials'):
            self.conf.add_section('credentials')
        self.conf.set('credentials', 'client-id', client_id)
        self.conf.set('credentials', 'client-secret', client_secret)

        if not self.conf.has_section('websites'):
            self.conf.add_section('websites')
        self.conf.set('websites', 'website', website)
        self.conf.set('websites', 'redirect-uri', redirect_uri)
        with open(self.path, 'w') as configfile:
            self.conf.write(configfile)

    def _read_conf(self):
        info = dict()

        self.conf.read(self.path)
        info['client-id'] = self.conf.get('credentials', 'client-id')
        info['client-secret'] = self.conf.get('credentials', 'client-secret')

        info['website'] = self.conf.get('websites', 'website')
        info['redirect-uri'] = self.conf.get('websites', 'redirect-uri')
        return info

    def get_conf(self):
        if os.path.isfile(self.path):
            return self._read_conf()
        sys.exit('ERROR: Config file not found at %s. Please run `config init` '
                 'first.' % self.path)

    def edit_config(self):
        info = self.get_conf()
        print('Storing configuration at path: %s' % self.path)
        print('Please enter the soundcloud-dl configuration. Hit enter if you '
              'don\'t wish to change some property.')
        website = raw_input('    website [%s]: ' % info['website']) or \
            info['website']
        redirect_uri = raw_input(
            '    redirect-uri [%s]: ' % info['redirect-uri']) or \
            info['redirect-uri']
        client_id = raw_input('    client-id [%s]: ' % info['client-id']) or \
            info['client-id']
        client_secret = raw_input(
            '    client-secret [%s]: ' % info['client-secret']) or \
            info['client-secret']
        self._write_conf(website=website, redirect_uri=redirect_uri,
                         client_id=client_id, client_secret=client_secret)

    def init_config(self):
        print('Storing configuration at path: %s' % self.path)
        print('Please enter the soundcloud-dl configuration...')
        website = raw_input('    website: ')
        redirect_uri = raw_input('    redirect-uri: ')
        client_id = raw_input('    client-id: ')
        client_secret = raw_input('    client-secret: ')
        self._write_conf(website=website, redirect_uri=redirect_uri,
                         client_id=client_id, client_secret=client_secret)


def init_command_parser():

    commands = {'config': ['init', 'edit', 'purge'],
                'download': ['track', 'artist']}

    parser = argparse.ArgumentParser(
        description='A tool to download tracks from soundcloud.com using the '
                    'soundcloud API.')
    base_subparsers = parser.add_subparsers(dest='command')

    for command in commands:
        command_parser = base_subparsers.add_parser(command)
        command_subparsers = command_parser.add_subparsers(dest='sub_command')
        for sub_command in commands[command]:
            command_subparsers.add_parser(sub_command)

    return parser
