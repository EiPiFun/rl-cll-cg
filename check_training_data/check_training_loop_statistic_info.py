import numpy
import os
import pathlib
import sys

target_version = sys.argv[1]

current_user_main_directory = str(pathlib.Path.home())+'/'
try:
    coarse_grained_cellulose_computation_home_directory = os.getenv('CLL_CG_HOME')+'/'
except:
    coarse_grained_cellulose_computation_home_directory = current_user_main_directory

training_data_directory = coarse_grained_cellulose_computation_home_directory+'coarse_grained_cellulose_coefficients_data/training_data/{0}_training_data/'.format(target_version)

training_loop_statistic_info_pools_directory = coarse_grained_cellulose_computation_home_directory+'coarse_grained_cellulose_coefficients_data/training_loop_statistic_info_pools/'
pathlib.Path(training_loop_statistic_info_pools_directory).mkdir(parents=True,exist_ok=True)

print('\33c',end='\r')
print('Target version: {}'.format(target_version))

training_data_file_name_list = sorted(os.listdir(training_data_directory))
cellulose_data_pool_file_name_list = []
coefficients_pool_file_name_list = []

for training_data_file_name in training_data_file_name_list:
    if training_data_file_name.__contains__('cellulose_data_pool-'):
        cellulose_data_pool_file_name_list.append(training_data_file_name)
    elif training_data_file_name.__contains__('coefficients_pool-'):
        coefficients_pool_file_name_list.append(training_data_file_name)

total_cellulose_data_pool_file_number = len(cellulose_data_pool_file_name_list)
total_coefficients_pool_file_number = len(coefficients_pool_file_name_list)

if total_cellulose_data_pool_file_number > 0 and total_cellulose_data_pool_file_number == total_coefficients_pool_file_number:

    reward_data_column_number = -1
    training_data_statistic_info_pool = numpy.zeros((total_cellulose_data_pool_file_number,3))

    for i in range(0,total_cellulose_data_pool_file_number):

        temp_cellulose_data_pool_file_name = cellulose_data_pool_file_name_list[i]
        try:
            temp_cellulose_data_pool = numpy.loadtxt(training_data_directory+temp_cellulose_data_pool_file_name)
        except:
            temp_cellulose_data_pool = numpy.loadtxt(training_data_directory+temp_cellulose_data_pool_file_name,delimiter=',')

        if len(temp_cellulose_data_pool) > 0:
            if temp_cellulose_data_pool.ndim > 1:
                temp_reward_data_column = temp_cellulose_data_pool[:,reward_data_column_number]
                temp_total_step_number = len(temp_reward_data_column)
                temp_mean_reward_value = numpy.mean(temp_reward_data_column)
                temp_max_reward_value = numpy.max(temp_reward_data_column)
            else:
                temp_total_step_number = 1
                temp_mean_reward_value = temp_cellulose_data_pool[reward_data_column_number]
                temp_max_reward_value = temp_cellulose_data_pool[reward_data_column_number]
        else:
            temp_total_step_number = 0
            temp_mean_reward_value = 0.0
            temp_max_reward_value = 0.0

        training_data_statistic_info_pool[i,:] = (temp_total_step_number,temp_mean_reward_value,temp_max_reward_value)

    print('\nTotal training loop number: {}'.format(total_cellulose_data_pool_file_number))
    print('\nTotal step number|Mean reward|Max reward\nof each training loop\n')
    print(training_data_statistic_info_pool)
    numpy.savetxt(training_loop_statistic_info_pools_directory+target_version+'_training_loop_statistic_info_pool.txt',training_data_statistic_info_pool)

else:
    print('Improper training data files')
