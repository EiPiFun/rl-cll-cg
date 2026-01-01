#!/usr/bin/sh

cd ../../../
echo $(pwd)

rm -rf ./coarse_grained_cellulose_coefficients_code_no_velocity*
cp -r ./coarse_grained_cellulose_coefficients_code/ ./coarse_grained_cellulose_coefficients_code_no_velocity/

cd ./coarse_grained_cellulose_coefficients_code_no_velocity/physics_computation_pool/configure/
sh ./turn_off_velocity_create.sh
cd ../../../
echo $(pwd)
zip -r -q ./coarse_grained_cellulose_coefficients_code_no_velocity.zip ./coarse_grained_cellulose_coefficients_code_no_velocity/

