#!/bin/sh
echo "This will take some time. Plese be patient.."
python monthly_commits.py > monthly_commits.plot
echo "Plotting.."
gnuplot monthly_commits.gnu
echo "Adore monthly_commits.png"
