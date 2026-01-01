#!/usr/bin/sh

cd ../../../
echo $(pwd)

rm -rf ./coarse_grained_cellulose_coefficients_code_no_threshold*
cp -r ./coarse_grained_cellulose_coefficients_code/ ./coarse_grained_cellulose_coefficients_code_no_threshold/

cd ./coarse_grained_cellulose_coefficients_code_no_threshold/physics_computation_pool/configure/
sh ./turn_off_threshold.sh
cd ../../../
echo $(pwd)
zip -r -q ./coarse_grained_cellulose_coefficients_code_no_threshold.zip ./coarse_grained_cellulose_coefficients_code_no_threshold/


