#!/usr/bin/bash

sed -e 's| #print| print|g' -i ./coarse_grained_cellulose_post_processing.py

sed -e 's| print| #print|g' -i ./coarse_grained_cellulose_computation.py
sed -e 's|echo|#echo|g' -i ../test_only/modify_random_seed.sh
sed -e 's|cat|#cat|g' -i ../test_only/modify_random_seed.sh

for i in {0..10};do

cd $(pwd)
bash ../test_only/modify_random_seed.sh $i
python3 ./coarse_grained_cellulose_computation.py debug
#tail -n 1 ./debug/physics_computation_5/results/cl_average_direction_angle_relaxation.txt
#tail -n 1 ./debug/physics_computation_5/results/cl_average_direction_angle_stretch.txt

rm -rf ./debug_$i/
cp -r ./debug/ ./debug_$i/

done


