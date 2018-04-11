#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os


def get_type():
	return "BINARY"

def get_desc():
	return "sqlite shell interface"

def get_licence():
	return "sqlite"

def get_compagny_type():
	return "org"

def get_compagny_name():
	return "sqlite-shell"

def get_maintainer():
	return ["unknown <unknown@sqlite.org>"]

def get_version():
	return [3,23,1]

def configure(target, my_module):
	my_module.add_src_file([
		'sqlite/shell.c'
		])
	
	my_module.compile_version('c++', 1999)
	
	my_module.add_depend([
	    'sqlite'
	    ])
	
	return True
