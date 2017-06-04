#!/usr/bin/env python 
import string
import argparse
import sys
from subprocess import call
import os
cwd = os.getcwd()

debug = False

parser = argparse.ArgumentParser(description="Image optimization for blog")

parser.add_argument("-d", "--directory", default=".", type=str, help="specify working directory")
parser.add_argument("-o", "--operation", default="complete", type=str, help="complete resize convert copyAndResize optimize")


in_args = vars(parser.parse_args(sys.argv[1:]))

if in_args["operation"] == "complete":
	in_args["operation"] = ["convert", "resize", "copyAndResize", "optimize"]

print "Operating directory ", args["directory"]


for args in in_args["operation"]:

	if args["operation"] == "optimize":
		cmdoptim ="open -a ImageOptim %s/"%(args["directory"]) 
		cmdoptim =cmdoptim.split(' ')
		print cmdoptim
		call( cmdoptim)
	elif args["operation"] == "resize":
		cmdr = 'mogrify -resize 1600> %s/*.jpg'%(args["directory"])
		cmdr = cmdr.split(' ')
		print cmdr
		call( cmdr)
		cmdr = 'mogrify -resize 1600> %s/*.png'%(args["directory"])
		cmdr = cmdr.split(' ')
		print cmdr
		call( cmdr)
	elif args["operation"] == "copyAndResize":
		cmd2x = 'convert %s/*.jpg -resize 30%% -set filename:area %%t_post %s/%%[filename:area].jpg'%(args["directory"],args["directory"])
		cmd2x = cmd2x.split(' ')
		print cmd2x
		call( cmd2x)
		cmd2x = 'convert %s/*.png -resize 30%% -set filename:area %%t_post %s/%%[filename:area].png'%(args["directory"],args["directory"])
		cmd2x = cmd2x.split(' ')
		print cmd2x
		call( cmd2x)
	elif args["operation"] == "convert":
		cmdconvert ="mogrify -format jpg %s/*.JPG"%args["directory"]
		cmdconvert = cmdconvert.split(' ')
		print cmdconvert
		call( cmdconvert)
		cmdconvert ="mogrify -format png %s/*.PNG"%args["directory"]
		cmdconvert = cmdconvert.split(' ')
		print cmdconvert
		call( cmdconvert)
	else:
		print 'available cmds: resize convert copyAndResize optimize '