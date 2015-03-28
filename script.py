# -*- coding: utf-8 -*-
#!/usr/bin/python
from os import listdir
from os.path import isfile, join


mod_files = [ f for f in listdir("mod") if isfile(join("mod",f)) ]
old_files = [ f for f in listdir("old") if isfile(join("old",f)) ]

print mod_files

for mod_file in mod_files:
	mod_file = open('mod/'+mod_file, 'r')

	for old_file in old_files:
		new_file = open('new/'+old_file, 'w')
		old_file = open('mod/'+old_file, 'r')