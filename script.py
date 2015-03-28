# -*- coding: utf-8 -*-
#!/usr/bin/python

mod_file = open('new_handling.cfg', 'r')
old_file = open('handling.cfg', 'r')

new_file = open('mod_handling.cfg', 'w')

for mod_line in mod_file:
	for old_line in old_file:
		print old_line.split(" ")[0] + "\r\n"
		if old_line.split(" ")[0] == mod_line.split(" ")[0]:
			pass