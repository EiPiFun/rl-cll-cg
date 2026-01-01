#!/usr/bin/sh

cd ../../../
echo $(pwd)

rm -rf ./coarse_grained_cellulose_coefficients_code_suffix_off*
cp -r ./coarse_grained_cellulose_coefficients_code/ ./coarse_grained_cellulose_coefficients_code_suffix_off/

cd ./coarse_grained_cellulose_coefficients_code_suffix_off/physics_computation_pool/configure/
sh ./turn_off_suffix.sh
cd ../../../
echo $(pwd)
zip -r -q ./coarse_grained_cellulose_coefficients_code_suffix_off.zip ./coarse_grained_cellulose_coefficients_code_suffix_off/


