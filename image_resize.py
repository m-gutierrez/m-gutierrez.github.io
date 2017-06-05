#!/usr/bin/env python 
import string
import argparse
import sys
from subprocess import call
import os

debug = False

parser = argparse.ArgumentParser(description="Image optimization for blog")

parser.add_argument("-d", "--directory", default=".", type=str, help="specify working directory")
parser.add_argument("-o", "--operation", default="complete", type=str, help="complete resize convert copyAndResize optimize")


in_args = vars(parser.parse_args(sys.argv[1:]))

if in_args["operation"] == "complete":
	in_args["operation"] = ["convert", "resize", "copyAndResize", "optimize"]
else:
	in_args["operation"] = [in_args["operation"]]
print "Operating directory ", in_args["directory"]


for args in in_args["operation"]:

	if args == "optimize":
		cmdoptim ="open -a ImageOptim %s/"%(in_args["directory"]) 
		print cmdoptim
		os.system( cmdoptim)
	elif args == "resize":
		cmdr = 'mogrify -resize 1600> %s/*.jpg'%(in_args["directory"])
		cmdr = cmdr.split(' ')
		print cmdr
		call( cmdr)
		cmdr = 'mogrify -resize 1600> %s/*.png'%(in_args["directory"])
		cmdr = cmdr.split(' ')
		print cmdr
		call( cmdr)
	elif args == "copyAndResize":
		ignorepost = 'find %s/*.jpg \! -name "*_post.jpg" | xargs -J %% '%in_args["directory"]
		cmd2x = ignorepost+'convert %% -resize 30%% -set filename:area %%t_post %s/%%[filename:area].jpg'%(in_args["directory"])
		print cmd2x
		os.system(cmd2x)
		ignorepost = 'find %s/*.png \! -name "*_post.png" | xargs -J %% '%in_args["directory"]
		cmd2x = ignorepost+'convert %% -resize 30%% -set filename:area %%t_post %s/%%[filename:area].png'%(in_args["directory"])
		print cmd2x
		os.system(cmd2x)

	elif args == "convert":
		cmdconvert ="mogrify -format jpg %s/*.JPG"%in_args["directory"]
		print cmdconvert
		os.system( cmdconvert)
		cmdconvert ="mogrify -format png %s/*.PNG"%in_args["directory"]
		print cmdconvert
		os.system( cmdconvert)
	else:
		print 'available cmds: resize convert copyAndResize optimize '