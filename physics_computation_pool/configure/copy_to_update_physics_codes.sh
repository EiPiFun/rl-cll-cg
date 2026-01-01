#!/usr/bin/sh

# LAMMPS Data for bonded

for i in 2 3 4 5;do
for j in 1 2 3 4;do

rm ../v"$i"3_physics/physics_computation_$j/inputs/*.data
cp ../v"$i"1_physics/physics_computation_$j/inputs/*.data ../v"$i"3_physics/physics_computation_$j/inputs/

done
done

# estimated_coefficients for bonded

for i in 2 3 4 5;do
for j in 2 3 4;do

rm ../v"$i"1_physics/physics_computation_$j/inputs/in_file_estimated_coefficients.txt
cp ../v"$i"1_physics/physics_computation_1/inputs/in_file_estimated_coefficients.txt ../v"$i"1_physics/physics_computation_$j/inputs/

done
done

# estimated_coefficients for bonded and nonbonded

for i in 2 3 4 5;do
for j in 2 3 4 5 6 7;do

rm ../v"$i"3_physics/physics_computation_$j/inputs/in_file_estimated_coefficients.txt
cp ../v"$i"3_physics/physics_computation_1/inputs/in_file_estimated_coefficients.txt ../v"$i"3_physics/physics_computation_$j/inputs/

done
done

# in_file_constant_head_common for bonded except for 4

for i in 2 3 5;do
for j in 1 2 3 4;do

rm ../v"$i"1_physics/physics_computation_$j/inputs/in_file_constant_head_common.txt
cp ../common/vX1_physics/physics_computation_$j/inputs/in_file_constant_head_common.txt ../v"$i"1_physics/physics_computation_$j/inputs/

done
done

# in_file_constant_head_common for bonded and nonbonded except for 4

for i in 2 3 5;do
for j in 1 2 3 4 5 6 7;do

rm ../v"$i"3_physics/physics_computation_$j/inputs/in_file_constant_head_common.txt
cp ../common/vX3_physics/physics_computation_$j/inputs/in_file_constant_head_common.txt ../v"$i"3_physics/physics_computation_$j/inputs/

done
done

# in_file_constant_tail for bonded

for i in 2 3 4 5;do
for j in 1 2 3 4;do

rm ../v"$i"1_physics/physics_computation_$j/inputs/in_file_constant_tail.txt
cp ../common/vX1_physics/physics_computation_$j/inputs/in_file_constant_tail.txt ../v"$i"1_physics/physics_computation_$j/inputs/

done
done

# in_file_constant_tail for bonded and nonbonded

for i in 2 3 4 5;do
for j in 1 2 3 4 5 6 7;do

rm ../v"$i"3_physics/physics_computation_$j/inputs/in_file_constant_tail.txt
cp ../common/vX3_physics/physics_computation_$j/inputs/in_file_constant_tail.txt ../v"$i"3_physics/physics_computation_$j/inputs/

done
done

# in_file for bonded

for i in 2 3 4 5;do
for j in 1 2 3 4;do

cat ../v"$i"1_physics/physics_computation_$j/inputs/in_file_constant_head_common.txt > ../v"$i"1_physics/physics_computation_$j/inputs/in_file_constant_head.txt
cat ../v"$i"1_physics/physics_computation_$j/inputs/in_file_constant_head_specific.txt >> ../v"$i"1_physics/physics_computation_$j/inputs/in_file_constant_head.txt

cat ../v"$i"1_physics/physics_computation_$j/inputs/in_file_constant_head.txt > ../v"$i"1_physics/physics_computation_$j/inputs/coarse_grained_cellulose.in
cat ../v"$i"1_physics/physics_computation_$j/inputs/in_file_estimated_coefficients.txt >> ../v"$i"1_physics/physics_computation_$j/inputs/coarse_grained_cellulose.in
cat ../v"$i"1_physics/physics_computation_$j/inputs/in_file_constant_tail.txt >> ../v"$i"1_physics/physics_computation_$j/inputs/coarse_grained_cellulose.in

done
done

# in_file for bonded and nonbonded

for i in 2 3 4 5;do
for j in 1 2 3 4 5 6 7;do

cat ../v"$i"3_physics/physics_computation_$j/inputs/in_file_constant_head_common.txt > ../v"$i"3_physics/physics_computation_$j/inputs/in_file_constant_head.txt
cat ../v"$i"3_physics/physics_computation_$j/inputs/in_file_constant_head_specific.txt >> ../v"$i"3_physics/physics_computation_$j/inputs/in_file_constant_head.txt

cat ../v"$i"3_physics/physics_computation_$j/inputs/in_file_constant_head.txt > ../v"$i"3_physics/physics_computation_$j/inputs/coarse_grained_cellulose.in
cat ../v"$i"3_physics/physics_computation_$j/inputs/in_file_estimated_coefficients.txt >> ../v"$i"3_physics/physics_computation_$j/inputs/coarse_grained_cellulose.in
cat ../v"$i"3_physics/physics_computation_$j/inputs/in_file_constant_tail.txt >> ../v"$i"3_physics/physics_computation_$j/inputs/coarse_grained_cellulose.in

done
done


