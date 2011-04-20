#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import commands

for year in range(1995, 2012):
    for month in range(1, 13):
        nextmonth = month + 1
        # No commits before February
        if year == 1995 and nextmonth <= 2:
            continue
        # There is no data after these dates
        if year == 2011 and month >= 5:
            break
        # December makes difference for us
        if month == 12:
            runcmd = """git log --since="%d-%d-1 00:00:00" --until="%d-%d-31 23:59:59" --shortstat --oneline -C |\
                    grep 'files changed, ' |\
                    awk '{ s1+=$1; s2+=$4; s3+=$6 } END {print s1, s2, s3}'"""\
                    % (year, month, year, month)
        else:
            runcmd = """git log --since="%d-%d-1 00:00:00" --until="%d-%d-1 00:00:00" --shortstat --oneline -C |\
                    grep 'files changed, ' |\
                    awk '{ s1+=$1; s2+=$4; s3+=$6 } END {print s1, s2, s3}'"""\
                    % (year, month, year, nextmonth)
        runresult = commands.getoutput(runcmd)
        date = datetime(year, month, 1)
        print "%s %s" % (date.strftime("%Y-%m-%d"), runresult)


# Some tests:

# $ python counttt.py
# 1995-02-01 2382 221043 1074 <--.
# 1995-03-01 388 8144 4683        `.
# 1995-04-01 198 12144 11181       |
# 1995-05-01 174 15746 1285        |
# 1995-06-01 58 512 140            |
# 1995-07-01 120 1796 800          |
# 1995-08-01 118 1413 840          |
# 1995-09-01 463 10178 3289        |
# 1995-10-01 383 12405 1825        |
# 1995-11-01 240 8361 1791       ,´
# 1995-12-01 149 12764 1200 <---+.
# 1996-01-01 561 16228 5901       `.
# 1996-02-01 328 6282 1573         |
#                                  |
#                                   \ Proves below
#
# $ git log --since="1995-2-1 00:00:00" --until="1995-3-1 00:00:00" --shortstat --oneline -C | grep 'files changed, ' | awk '{ s1+=$1; s2+=$4; s3+=$6 } END {print s1, s2, s3}'
# 2382 221043 1074
#
# $ git log --since="1995-12-1 00:00:00" --until="1996-1-1 00:00:00" --shortstat --oneline -C | grep 'files changed, ' | awk '{ s1+=$1; s2+=$4; s3+=$6 } END {print s1, s2, s3}'
# 149 12764 1200


