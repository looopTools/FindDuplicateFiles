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
import os
from os import listdir
from os.path import isfile, join, basename, isdir

#sname = ""
#duplicates = 0

## Main method
def main(path, sname, duplicates, rec):
    duplicates = commonMain(path, sname, duplicates)
    if rec:
        main_rec(path, sname, duplicates, rec)

    printEndInfo(path, sname, duplicates)

def commonMain(path, sname, duplicates):
    print('Searching in dir: {}'.format(path))
    print('Loading files')
    files = filesFromDir(path)
    print('Files loaded')
    print('Checking for dublicates')
    return walkFiles(files, sname,  duplicates)


def main_rec(path, sname, duplicates, rec):
    dirs = dirsFromDir(path)
    walkDirs(dirs, path, sname, duplicates, rec)


# Generates a list of fiels from a directory
def filesFromDir(path):
    return [f for f in listdir(path) if isfile(join(path, f))]

# Generates a list of sub directories from a directory
def dirsFromDir(path):
    return [d for d in listdir(path) if isdir(join(path, d))]


# Checks the name of a file with out file extension
def compareName(fname, sname):
    baseName = os.path.splitext(fname)[0]
    return baseName == sname

def walkFiles(list, sname, duplicates):
    for f in list:
        if compareName(f, sname):
            duplicates =  duplicates + 1
    return duplicates

def walkDirs(list, path, sname, duplicates, rec):
    for d in list:
        newPath = join(path, d)
        main(newPath, sname, duplicates, rec)




def printEndInfo(path, sname, duplicates):
    if duplicates == 1:
        print('Single file found in {}'.format(path))
    elif duplicates == 0:
        print('No file with the name {} has been found'.format(sname))
    else:
        print('Number of duplicates found in {}: {}'.format(path, duplicates))

def printHelp():
    print('fdf dir file_name_out_extension')
    print('fdf -r dir file_name_out_extension - for recursive traversal')
    print('fdf -h: prints help')




## Scripting for running the program

if sys.argv[1] == '-h':
    printHelp()
else:
    if len(sys.argv) < 3:
        print('Enter all arguments')
    else:
        if '-r' in sys.argv:
            main(sys.argv[2], sys.argv[3], 0, True)
        else:
            main(sys.argv[1], sys.argv[2], 0, False)
