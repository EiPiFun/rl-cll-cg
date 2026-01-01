import gymnasium as gym
import numpy
import sys
import os
import pathlib
import time

code_version = 'v53'
physics_version = 'v55'

coefficient_precision_format = '%.4g'

current_user_main_directory = str(pathlib.Path.home())+'/'
try:
    coarse_grained_cellulose_computation_home_directory = os.getenv('CLL_CG_HOME')+'/'
except:
    coarse_grained_cellulose_computation_home_directory = current_user_main_directory

coarse_grained_cellulose_computation_code_directory = coarse_grained_cellulose_computation_home_directory+'coarse_grained_cellulose_coefficients_code/physics_computation_pool/'+code_version+'_physics/'

sys.path.append(coarse_grained_cellulose_computation_code_directory)

from coarse_grained_cellulose_coefficients_env_common import CoarseGrainedCelluloseCoefficientsEnvCommon

from coarse_grained_cellulose_computation_specific import coarse_grained_cellulose_coefficients_pool_header
from coarse_grained_cellulose_computation import coarse_grained_cellulose_data_pool_header

class CoarseGrainedCelluloseCoefficientsEnv(gym.Env):

    def __init__(self):

        super().__init__()

        self.pcs_pool = []
        self.coarse_grained_cellulose_data_pool = []
        self.action = None
        self.reward = 0.0
        self.observation = 1

        self.terminated = False
        self.truncated = False

        self.step_count = 0

        self.action_space = gym.spaces.Box(
            (-1.0*numpy.ones((15),dtype=numpy.float32)),
            (+1.0*numpy.ones((15),dtype=numpy.float32)),
        )

        self.observation_space = gym.spaces.Discrete(2)

        training_data_directory = coarse_grained_cellulose_computation_home_directory+'/coarse_grained_cellulose_coefficients_data/training_data/'+physics_version+'_training_data/'
        pathlib.Path(training_data_directory).mkdir(parents=True,exist_ok=True)

        self.coefficients_temp_pool_file_location = training_data_directory+'coefficients_temp_pool.txt'
        self.coarse_grained_cellulose_data_temp_pool_file_location = training_data_directory+'coarse_grained_cellulose_data_temp_pool.txt'

        self.coefficients_pool_file_location_base = training_data_directory+'coefficients_pool-'
        self.coarse_grained_cellulose_data_pool_file_location_base = training_data_directory+'coarse_grained_cellulose_data_pool-'

        self.coarse_grained_cellulose_coefficients_pool_header = 'step_count,bc_1,bc_2,bc_3,ac_1,ac_2,ac_3,ac_4,ac_5,ac_6,ic_1,ic_2,ic_3,pc_1_2_1_hb,pc_1_2_2_hb,pc_1_3_1_hb,pc_1_3_2_hb,pc_1_1_1,pc_1_1_2,pc_1_2_1,pc_1_2_2,pc_1_3_1,pc_1_3_2,pc_2_2_1,pc_2_2_2,pc_2_3_1,pc_2_3_2,pc_3_3_1,pc_3_3_2'
        self.coarse_grained_cellulose_data_pool_header = 'step_count,fitted_elastic_modulus,elastic_modulus_match_degree,average_persistence_length,persistence_length_match_degree,average_end_to_end_distance,end_to_end_distance_match_degree,system_stable_enough_switch,fracture_average_direction_angle_match_degree,fracture_rotation_angle_match_degree,max_stress_match_degree,max_strain_energy_match_degree,equivalent_strain_match_degree,reward_value'

    def step(self, action):

        self.step_count = self.step_count+1
        self.observation = 1

        if action is not None:

            temp_bc_1 = float(coefficient_precision_format % (10.0*action[0]+70.0))
            temp_bc_2 = float(coefficient_precision_format % (0.8226*temp_bc_1))
            temp_bc_3 = float(coefficient_precision_format % (2.1999*temp_bc_1))
            temp_ac_1 = float(coefficient_precision_format % (10.0*action[1]+40.0))
            temp_ac_2 = float(coefficient_precision_format % (0.4987*temp_ac_1))
            temp_ac_3 = float(coefficient_precision_format % (0.8631*temp_ac_1))
            temp_ac_4 = float(coefficient_precision_format % (0.5884*temp_ac_1))
            temp_ac_5 = float(coefficient_precision_format % (0.6923*temp_ac_1))
            temp_ac_6 = float(coefficient_precision_format % (0.3608*temp_ac_1))
            temp_ic_1 = float(coefficient_precision_format % (0.35*action[2]+0.50))
            temp_ic_2 = float(coefficient_precision_format % (0.8821*temp_ic_1))
            temp_ic_3 = float(coefficient_precision_format % (0.9299*temp_ic_1))
            temp_pc_1_2_1_hb = float(coefficient_precision_format % (2.0*action[3]+2.0))
            temp_pc_1_2_2_hb = float(coefficient_precision_format % (1.525*action[4]+6.1))
            temp_pc_1_3_1_hb = float(coefficient_precision_format % (2.0*action[3]+2.0))
            temp_pc_1_3_2_hb = float(coefficient_precision_format % (1.475*action[4]+5.9))
            temp_pc_1_1_1 = float(coefficient_precision_format % (2.0*action[5]+2.0))
            temp_pc_1_1_2 = float(coefficient_precision_format % (1.3*action[6]+5.1))
            temp_pc_1_2_1 = float(coefficient_precision_format % (2.0*action[7]+2.0))
            temp_pc_1_2_2 = float(coefficient_precision_format % (1.0*action[8]+3.9))
            temp_pc_1_3_1 = float(coefficient_precision_format % (2.0*action[9]+2.0))
            temp_pc_1_3_2 = float(coefficient_precision_format % (1.0*action[10]+4.0))
            temp_pc_2_2_1 = float(coefficient_precision_format % (2.0*action[11]+2.0))
            temp_pc_2_2_2 = float(coefficient_precision_format % (1.3*action[6]+5.1))
            temp_pc_2_3_1 = float(coefficient_precision_format % (2.0*action[12]+2.0))
            temp_pc_2_3_2 = float(coefficient_precision_format % (0.9*action[13]+3.7))
            temp_pc_3_3_1 = float(coefficient_precision_format % (2.0*action[14]+2.0))
            temp_pc_3_3_2 = float(coefficient_precision_format % (1.3*action[6]+5.1))

        temp_coefficients = (self.step_count,temp_bc_1,temp_bc_2,temp_bc_3,temp_ac_1,temp_ac_2,temp_ac_3,temp_ac_4,temp_ac_5,temp_ac_6,temp_ic_1,temp_ic_2,temp_ic_3,temp_pc_1_2_1_hb,temp_pc_1_2_2_hb,temp_pc_1_3_1_hb,temp_pc_1_3_2_hb,temp_pc_1_1_1,temp_pc_1_1_2,temp_pc_1_2_1,temp_pc_1_2_2,temp_pc_1_3_1,temp_pc_1_3_2,temp_pc_2_2_1,temp_pc_2_2_2,temp_pc_2_3_1,temp_pc_2_3_2,temp_pc_3_3_1,temp_pc_3_3_2)
        self.pcs_pool.append(temp_coefficients)
        numpy.savetxt(self.coefficients_temp_pool_file_location,self.pcs_pool,header=coarse_grained_cellulose_coefficients_pool_header,fmt='%.6e',delimiter=',')

        temp_interaction_coefficients = (temp_bc_1,temp_bc_2,temp_bc_3,temp_ac_1,temp_ac_2,temp_ac_3,temp_ac_4,temp_ac_5,temp_ac_6,temp_ic_1,temp_ic_2,temp_ic_3,temp_pc_1_2_1_hb,temp_pc_1_2_2_hb,temp_pc_1_3_1_hb,temp_pc_1_3_2_hb,temp_pc_1_1_1,temp_pc_1_1_2,temp_pc_1_2_1,temp_pc_1_2_2,temp_pc_1_3_1,temp_pc_1_3_2,temp_pc_2_2_1,temp_pc_2_2_2,temp_pc_2_3_1,temp_pc_2_3_2,temp_pc_3_3_1,temp_pc_3_3_2)

        temp_coarse_grained_cellulose_coefficients_env_class = CoarseGrainedCelluloseCoefficientsEnvCommon(coarse_grained_cellulose_computation_home_directory,coarse_grained_cellulose_computation_code_directory,physics_version)
        temp_fitted_elastic_modulus,temp_elastic_modulus_match_degree,temp_average_persistence_length,temp_persistence_length_match_degree,temp_average_end_to_end_distance,temp_end_to_end_distance_match_degree,temp_system_stable_enough_switch,temp_fracture_average_direction_angle_match_degree,temp_fracture_rotation_angle_match_degree,temp_max_stress_match_degree,temp_max_strain_energy_match_degree,temp_equivalent_strain_match_degree,temp_reward_value = temp_coarse_grained_cellulose_coefficients_env_class.processing_bonded_and_nonbonded(temp_interaction_coefficients)

        temp_coarse_grained_cellulose_data = (self.step_count,temp_fitted_elastic_modulus,temp_elastic_modulus_match_degree,temp_average_persistence_length,temp_persistence_length_match_degree,temp_average_end_to_end_distance,temp_end_to_end_distance_match_degree,temp_system_stable_enough_switch,temp_fracture_average_direction_angle_match_degree,temp_fracture_rotation_angle_match_degree,temp_max_stress_match_degree,temp_max_strain_energy_match_degree,temp_equivalent_strain_match_degree,temp_reward_value)
        self.coarse_grained_cellulose_data_pool.append(temp_coarse_grained_cellulose_data)
        numpy.savetxt(self.coarse_grained_cellulose_data_temp_pool_file_location,self.coarse_grained_cellulose_data_pool,header=coarse_grained_cellulose_data_pool_header,fmt='%.6e',delimiter=',')

        self.reward = temp_reward_value

        self.terminated = True

        return self.observation,self.reward,self.terminated,self.truncated,{}

    def reset(self, seed=None, options=None):
        self.observation = 1
        return self.observation, {}

    def render(self):
        print("No graphical output")

    def close(self):
        current_time = time.strftime('%Y-%m-%d-%H:%M:%S')
        numpy.savetxt(self.coefficients_pool_file_location_base+current_time+'.txt',self.pcs_pool,header=coarse_grained_cellulose_coefficients_pool_header,fmt='%.6e',delimiter=',')
        numpy.savetxt(self.coarse_grained_cellulose_data_pool_file_location_base+current_time+'.txt',self.coarse_grained_cellulose_data_pool,header=coarse_grained_cellulose_data_pool_header,fmt='%.6e',delimiter=',')
        print('None of unexpectations met.')

