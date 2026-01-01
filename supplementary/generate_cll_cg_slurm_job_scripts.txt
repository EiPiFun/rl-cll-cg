#!/usr/bin/sh

# vXY_initial_and_following_training.sh

```
#!/usr/bin/sh

#SBATCH -w localhost
#SBATCH -n 1
#SBATCH -c n
#SBATCH -J vXYif

export CLL_CG_HOME=/homex/home2/donx/cll_cg_new/

/homex/home2/donx/software/venv/bin/python3 $CLL_CG_HOME/coarse_grained_cellulose_coefficients_code/initial_training.py vXY
/homex/home2/donx/software/venv/bin/python3 $CLL_CG_HOME/coarse_grained_cellulose_coefficients_code/following_training.py vXY 1024 10
```

# Generate

mkdir -p ./slurm_jobs/
rm -rf ./slurm_jobs/*.sh

for i in 2 3 4 5;do
for j in 2;do
for k in initial initial_and_following following;do

cp ./vXY_"$k"_training.sh ./slurm_jobs/v"$i$j"_"$k"_training.sh
sed -e "s|vXY|v"$i$j"|g" -i ./slurm_jobs/v"$i$j"_"$k"_training.sh
sed -e "s|-c n|-c 2|g" -i ./slurm_jobs/v"$i$j"_"$k"_training.sh

done
done
done

for i in 2 3 4 5;do
for j in 4;do
for k in initial initial_and_following following;do

cp ./vXY_"$k"_training.sh ./slurm_jobs/v"$i$j"_"$k"_training.sh
sed -e "s|vXY|v"$i$j"|g" -i ./slurm_jobs/v"$i$j"_"$k"_training.sh
sed -e "s|-c n|-c 6|g" -i ./slurm_jobs/v"$i$j"_"$k"_training.sh

done
done
done

# Submit

cd ./slurm_jobs/;for i in 3;do for j in 2 4;do for k in following;do sbatch ./v"$i$j"_"$k"_training.sh;done;done;done



