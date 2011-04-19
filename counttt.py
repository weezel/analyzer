#!/usr/bin/env python
# -*- coding: utf-8 -*-

import commands

for year in range(1995, 2011):
    print "Year: %d" % year
    for month in range(2,12):
        runcmd = """git log --since="%d-%d-1" --until="%d-%d-1" --shortstat --oneline | grep 'files changed, ' | awk '{ s1+=$1; s2+=$4; s3+=$6 } END {print s1, s2, s3}'"""\
                % (year, month - 1, year, month)
        runresult = commands.getoutput(runcmd)
        print "Month: %d" % (month - 1),
        print "\t" + runresult


# $ python counttt.py
# Year: 1995
# Month: 1 	  
# Month: 2 	2382 221168 931
# Month: 3 	395 10940 7242
# Month: 4 	198 12165 11172

# git log --since="1995-2-1" --until="1995-3-1" --shortstat --oneline | grep 'files changed, ' | awk '{ s1+=$1; s2+=$4; s3+=$6 } END {print s1, s2, s3}'
# 2382 221168 931

