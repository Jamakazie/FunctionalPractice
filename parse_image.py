import os
from os.path import join, isdir, isfile

def find_files(directory='\\', file_types=['*'], recurse=False):
	files = map(lambda x: join(directory, x), 
			filter(lambda x: isfile(join(directory, x)), os.listdir(directory)))
	#files = []
	return files

def recurse(directory):
	""" Returns a list of files and directories that are under the parent directory"""
	if not filter(lambda x: isdir(join(directory, x)), os.listdir(directory)):
		return map(lambda x: join(directory, x),
				filter(lambda x: isfile(join(directory,x)), os.listdir(directory)))
					 
	return map(lambda x: recurse(join(directory, x)), 
			filter(lambda x: isdir(join(directory, x)), os.listdir(directory)))

print recurse(direct)
