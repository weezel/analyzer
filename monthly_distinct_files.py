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
            runcmd = """git log --since="%d-%d-1 00:00:00" --until="%d-%d-31 23:59:59" -C --raw |\
                    grep -E "^:"|\
                    awk '{print $6}'|\
                    sort |\
                    uniq |\
                    wc -l"""\
                    % (year, month, year, month)
        else:
          runcmd = """git log --since="%d-%d-1 00:00:00" --until="%d-%d-1 00:00:00" -C --raw |\
                    grep -E "^:"|\
                    awk '{print $6}'|\
                    sort |\
                    uniq |\
                    wc -l"""\
                    % (year, month, year, nextmonth)
        runresult = commands.getoutput(runcmd)
        date = datetime(year, month, 1)
        print "%s %s" % (date.strftime("%Y-%m-%d"), runresult)


# Count distinct file changes per month
# git log --since="2010-1-1" --until="2010-2-1" --raw | grep -E "^:"|awk '{print $5, $6}'| grep -E "^[A-Z]\s"
# git log --since="2010-1-1" --until="2010-2-1" --raw | grep -E "^:"|awk '{print $5, $6}'| sort -k 2  | uniq | wc -l

