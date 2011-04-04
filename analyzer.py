#!/usr/bin/env python
# -*- coding: utf-8 -*-

from glob import glob
import commands
import mimetypes
import os
import sys


allfiles = glob("RECODER*")
allfiles.sort()

mimetypes.init()
mimetypes.add_type("text/java", ".java")

dirlinecount = 0


def visitDir(args, dirname, filenames):
    global mimetypes
    global dirlinecount

    # Do not process .git directory
    if ".cvs" in dirname or ".git" in dirname or ".svn" in dirname:
        return

    for f in filenames:
        ff = os.path.join(dirname, f)
        m = mimetypes.guess_type(ff)[0]

        # Check whether the file is .java file
        if os.path.isfile(ff) and \
                m is not None and \
                "text/java" in m:
            #print "%s  filetype: %s" % (ff, m)
            try:
                with open(ff) as fh:
                    linecount = 0
                    for line in fh:
                        linecount += 1
                    #print "%s: %d" % (ff, linecount)
                    dirlinecount += linecount
            except:
                print "Could not open file: %s" % os.path.join(dirname, f)


def main():
    global dirlinecount

    for j in allfiles:
        print "Comparing against: %s" % (j)
        for i in allfiles:
            if i == j:
                continue
            #print "%s" % i

            # Generate report here
            outtext = commands.getoutput("" + i)
            print "------- %s --------" % outtext

        # Visit directory and count count of lines from .java files
        os.path.walk(j, visitDir, None)
        print "Loc: %d" % dirlinecount
        dirlinecount = 0

        print ""


if __name__ == "__main__":
    main()
