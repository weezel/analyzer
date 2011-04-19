#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import commands

for year in range(1995, 2011):
    #print "Year: %d" % year
    for month in range(1,13):
        # No commits before February
        if year == 1995 and month == 1:
            continue
        runcmd = """git log --since="%d-%d-1" --until="%d-%d-31" --shortstat --oneline -C | grep 'files changed, ' | awk '{ s1+=$1; s2+=$4; s3+=$6 } END {print s1, s2, s3}'"""\
                % (year, month, year, month)
        runresult = commands.getoutput(runcmd)
        #print "Month: %d" % (month - 1),
        #print "\t" + runresult
        date = datetime(year, month, 1)
        print "%s %s" % (date.strftime("%Y-%m-%d"), runresult)


# $ python counttt.py
# Year: 1995
# Month: 1 	  
# Month: 2 	2382 221168 931
# Month: 3 	395 10940 7242
# Month: 4 	198 12165 11172

# git log --since="1995-2-1" --until="1995-3-1" --shortstat --oneline | grep 'files changed, ' | awk '{ s1+=$1; s2+=$4; s3+=$6 } END {print s1, s2, s3}'
# 2382 221168 931

#### FIX THIS #########
# $ git log --since="1995-2-1" --until="1995-2-28" --shortstat --oneline | grep 'files changed, ' | awk '{ s1+=$1; s2+=$4; s3+=$6 } END {print s1, s2, s3}'
# 2382 221168 931
#
# $ git log --since="1995-2-1" --until="1995-2-31" --shortstat --oneline | grep 'files changed, ' | awk '{ s1+=$1; s2+=$4; s3+=$6 } END {print s1, s2, s3}'
# 2391 221328 1001
#
# $ git log --since="1995-2-1" --until="1995-3-1" --shortstat --oneline | grep 'files changed, ' | awk '{ s1+=$1; s2+=$4; s3+=$6 } END {print s1, s2, s3}'
# 2386 221227 940

# 1995-02-01 2391 221174 1170

