#################################################################################
# FindDuplicateFiles
# Copyright (C) 2015 Lars Nielsen
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#################################################################################

import sys
from os import listdir
from os.path import isfile, join

sname = ""
duplicates = 0




def main(path):
    ##
    print('Loading files')
    files = filesFromDir(path)
    print('Files loaded')
    print('Checking for dublicates')
    walkFiles(files)
    printEndInfo(path)

def filesFromDir(path):
    return [f for f in listdir(path) if isfile(join(path, f))]

def compareName(fname):
    return fname == sname

def walkFiles(list):
    for f in list:
        if compareName(f):
            global duplicates
            duplicates =  duplicates + 1

def printEndInfo(path):
    print('Number of duplicates found in {}: {}'.format(path, duplicates))

def printHelp():
    print('fdf dir file_name_extension')
    print('fdf -h: prints help')


if sys.argv[1] == '-h':
    printHelp()
else:
    if len(sys.argv) < 3:
        print('Enter all arguments')
    else:
        global snam
        sname = sys.argv[2]
        print(sname)
        main(sys.argv[1])
