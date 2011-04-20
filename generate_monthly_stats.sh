#!/bin/sh
echo "This will take some time. Please be patient.."
echo ""
echo "Generating unique monthly committers.."
python monthly_distinct_developers.py > monthly_devs.plot
echo "Generating unique monthly files.."
python monthly_distinct_files.py > monthly_files.plot

echo "Plotting.."
gnuplot monthly_devs.gnu
gnuplot monthly_files.gnu

echo "Adore graphs of monthly_uniq_devs.png and monthly_uniq_files.png"
