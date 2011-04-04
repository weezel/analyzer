#!/usr/bin/env python
# -*- coding: utf-8 -*-

from glob import glob
import commands
import mimetypes
import os
import sys

#### Define some variables here. Other changes not needed ####
# Directory which contains all versions of the program. Absolute
# path needed.
#
abspath = "/Users/mepiispa/Downloads/recoder/test/"
####
# Where ccfinder can be found
#
ccfinder_prog = "~/Downloads/ccfx-osx/ccfx"
#
#### No changes needed after this line ####

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
    global abspath
    global ccfinder_prog
    global dirlinecount

    print "Versions",
    for i in allfiles:
        print ",%s" % i,
    print "\n",

    for n, j in enumerate(allfiles):
        print j + (" ," * (n+1)),

        for i in range(n + 1, len(allfiles)):
            # Compare current directory against all version dirs
            os.path.walk(j, visitDir, None) # Cur
            os.path.walk(allfiles[i], visitDir, None) # Other

            # Generate report here
            runcmd = ccfinder_prog + " d java -dn " + abspath + j + "/src/recoder/ -is -dn " + abspath + allfiles[i] + "/src/recoder/ -w f-w-g+"
            outtext = commands.getoutput(runcmd)

            # awk sums up the columns in here
            runcmd = ccfinder_prog + " m a.ccfxd -w | awk '{ s+=$2 } END {print s}'"
            outtext = commands.getoutput(runcmd)

            loc_div = float(outtext) / dirlinecount
            print ",%.3f" % (loc_div),

            dirlinecount = 0
        print "\n",


if __name__ == "__main__":
    main()
