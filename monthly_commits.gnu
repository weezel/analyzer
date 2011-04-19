reset
set logscale y
set terminal png size 1024,768
set output "monthly_commits.png"
set ylabel "Commits"
set grid
set xdata time
set timefmt "%Y-%m-%d"
set format x "%Y-%m"
set xlabel "Date"
set xtics nomirror rotate by -45 scale 0
# Colours
# 1=red 2=grn 3=blue

plot 'monthly_commits.plot' using 1:2 with linespoints lt 3 title "Changes", \
	'' using 1:3 with linespoints lt 2 title "Insertions", \
	'' using 1:4 with linespoints lt 1 title "Deletions"
