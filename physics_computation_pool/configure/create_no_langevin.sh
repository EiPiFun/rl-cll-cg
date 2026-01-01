#!/usr/bin/sh

cd ../../../
echo $(pwd)

rm -rf ./coarse_grained_cellulose_coefficients_code_no_langevin*
cp -r ./coarse_grained_cellulose_coefficients_code/ ./coarse_grained_cellulose_coefficients_code_no_langevin/

cd ./coarse_grained_cellulose_coefficients_code_no_langevin/physics_computation_pool/configure/
sh ./turn_off_langevin.sh
cd ../../../
echo $(pwd)
zip -r -q ./coarse_grained_cellulose_coefficients_code_no_langevin.zip ./coarse_grained_cellulose_coefficients_code_no_langevin/


