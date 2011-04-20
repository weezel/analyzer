reset
set logscale y
set terminal png size 800,600
set output "monthly_uniq_files.png"
set ylabel "Files"
set grid
set xdata time
set timefmt "%Y-%m-%d"
set format x "%Y-%m"
set xlabel "Date"
set xtics nomirror rotate by -45 scale 0
# Colours
# 1=red 2=grn 3=blue

plot 'monthly_files.plot' using 1:2 with linespoints lt 1 title "uniq files"

