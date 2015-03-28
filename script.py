# -*- coding: utf-8 -*-
#!/usr/bin/python
from os import listdir
from os.path import isfile, join



files = [ f for f in listdir("old") if isfile(join("old",f)) ]

"""for file_name in files:
	with open('mod/'+file_name, 'r') as mod_file:
		with open('old/'+file_name, 'r') as old_file:
			with open('new/'+file_name, 'w') as new_file:
				for mod_line in mod_file:
					print mod_line.replace("\r\n",'').replace("\t",' ').split(" ")
					for old_line in old_file:
						print old_line.replace("\r\n",'').replace("\t",' ').split(" ")
						break
						if old_line.split(" ")[0] == mod_line.split(" ")[0]:
							pass
					break"""

file_name = "handling.cfg"
with open('old/'+file_name, 'r') as old_file:
	with open('new/'+file_name, 'w') as new_file:
		with open('mod/'+file_name, 'r') as mod_file:
			count = 0
			for old_line in old_file:
				old_line_clean = old_line.replace("\r\n",'').replace("\t",' ').split(" ")[0]
				line_to_write = old_line

				for mod_line in mod_file:
					mod_line_clean = mod_line.replace("\r\n",'').replace("\t",' ').split(" ")[0]

					if old_line_clean == mod_line_clean:
						line_to_write = mod_line
						count +=1
						break

				new_file.write(line_to_write)

				mod_file.seek(0)

			print "The script has been able to recognize %d items to change from %s to %s" %(count, mod_file.name, new_file.name)