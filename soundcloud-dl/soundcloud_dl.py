#! /usr/bin/env python
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
from parser import init_command_parser
from parser import Config
import os
import sys


function_mapper = {'config_init': Config.init_config,
                   'config_edit': Config.edit_config,
                   }


def main():
    parser = init_command_parser()
    args = parser.parse_args()
    func = args.command + '_' + args.sub_command
    c = Config()
    function_mapper[func](c)


if __name__ == '__main__':
    sys.exit(main())
