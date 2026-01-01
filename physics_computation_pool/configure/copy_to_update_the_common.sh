#!/usr/bin/sh

# computation.py

for i in 2 3 4 5;do

rm ../v"$i"1_physics/coarse_grained_cellulose_computation.py
rm ../v"$i"3_physics/coarse_grained_cellulose_computation.py
cp ../common/coarse_grained_cellulose_computation_bonded.py ../v"$i"1_physics/coarse_grained_cellulose_computation.py
cp ../common/coarse_grained_cellulose_computation_bonded_and_nonbonded.py ../v"$i"3_physics/coarse_grained_cellulose_computation.py

done

# computation_common.py env_common.py and post_processing.py

for i in 2 3 4 5;do
for j in 1 3;do

rm ../v"$i$j"_physics/coarse_grained_cellulose_computation_common.py
rm ../v"$i$j"_physics/coarse_grained_cellulose_coefficients_env_common.py
rm ../v"$i$j"_physics/coarse_grained_cellulose_post_processing.py
cp ../common/coarse_grained_cellulose_computation_common.py ../v"$i$j"_physics/coarse_grained_cellulose_computation_common.py
cp ../common/coarse_grained_cellulose_coefficients_env_common_with_threshold.py ../v"$i$j"_physics/coarse_grained_cellulose_coefficients_env_common.py
cp ../common/coarse_grained_cellulose_post_processing_with_threshold.py ../v"$i$j"_physics/coarse_grained_cellulose_post_processing.py

done
done

rm ../common/coarse_grained_cellulose_coefficients_env_common_without_threshold.py
cp ../common/coarse_grained_cellulose_coefficients_env_common_with_threshold.py ../common/coarse_grained_cellulose_coefficients_env_common_without_threshold.py
sed -e "/^with_threshold_switch/ c with_threshold_switch = False" -i ../common/coarse_grained_cellulose_coefficients_env_common_without_threshold.py


