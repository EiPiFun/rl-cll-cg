#!/usr/bin/sh

for i in 2 3 4 5;do
for j in 1 3;do

rm ../v"$i$j"_physics/coarse_grained_cellulose_coefficients_env_common.py
rm ../v"$i$j"_physics/coarse_grained_cellulose_post_processing.py
cp ../common/coarse_grained_cellulose_coefficients_env_common_without_threshold.py ../v"$i$j"_physics/coarse_grained_cellulose_coefficients_env_common.py
cp ../common/coarse_grained_cellulose_post_processing_without_threshold.py ../v"$i$j"_physics/coarse_grained_cellulose_post_processing.py

done
done


