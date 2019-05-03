#!/usr/bin/python
import realog.debug as debug
import lutin.tools as tools
import os


def get_type():
	return "LIBRARY"

def get_desc():
	return "sqlite: SQL lite interface"

def get_licence():
	return "sqlite"

def get_compagny_type():
	return "org"

def get_compagny_name():
	return "sqlite"

def get_maintainer():
	return ["unknown <unknown@sqlite.org>"]

def get_version():
	return [3,23,1]

def configure(target, my_module):
	my_module.add_src_file([
		'sqlite/sqlite3.c'
		])
	
	my_module.add_header_file([
		'sqlite/sqlite3.h',
		'sqlite/sqlite3ext.h'
		], destination_path='sqlite')
	
	my_module.compile_version('c++', 1999)
	
	my_module.add_depend([
	    'm',
	    'pthread'
	    ])
	my_module.add_flag('c', [
		"-DSQLITE_ENABLE_FTS5",
		"-DSQLITE_ENABLE_RTREE",
		"-DSQLITE_ENABLE_EXPLAIN_COMMENTS"
		], export=True)
	
	return True



