#example file:
#set datafile separator "\s"
set terminal png size 1024,768
set output "monthly_commits.png"
set ylabel "Commits"
set grid
set xdata time
set timefmt "%Y-%m-%d"
set format x "%Y-%m"
set xlabel "Date"
set xtics nomirror rotate by -45 scale 0
set multiplot
#plot "plotdata.log" using ($2):3 with linespoints title "Additions", "plotdata.log" using ($3) with linespoints title "Changes", "plotdata.log" using ($4) with linespoints title "Deletions"
plot "monthly_commits.data" using 1:3 with linespoints title "Changes", \
"monthly_commits.data" using 2:3 with linespoints title "Insertions", \
"monthly_commits.data" using 3:3 with linespoints title "Deletions"

unset multiplot

