import numpy

estimated_interaction_coefficients = (60.00,45.01,97.07,25.00,19.44,28.38,10.90,12.96,12.06,0.16,0.21,0.18)

interaction_coefficients_header = 'bc_1,bc_2,bc_3,ac_1,ac_2,ac_3,ac_4,ac_5,ac_6,ic_1,ic_2,ic_3'

coarse_grained_cellulose_coefficients_pool_header = 'step_count,'+interaction_coefficients_header

class CoarseGrainedCelluloseComputationSpecific():

    def __init__(self,working_directory):

        self.physics_computation_1_inputs_directory = working_directory+'physics_computation_1/inputs/'
        self.physics_computation_2_inputs_directory = working_directory+'physics_computation_2/inputs/'
        self.physics_computation_3_inputs_directory = working_directory+'physics_computation_3/inputs/'
        self.physics_computation_4_inputs_directory = working_directory+'physics_computation_4/inputs/'

        self.physics_computation_1_in_file_location = self.physics_computation_1_inputs_directory+'coarse_grained_cellulose.in'
        self.physics_computation_2_in_file_location = self.physics_computation_2_inputs_directory+'coarse_grained_cellulose.in'
        self.physics_computation_3_in_file_location = self.physics_computation_3_inputs_directory+'coarse_grained_cellulose.in'
        self.physics_computation_4_in_file_location = self.physics_computation_4_inputs_directory+'coarse_grained_cellulose.in'

        self.interaction_coefficients_location = working_directory+'interaction_coefficients.txt'

    def in_file_generation(self,interaction_coefficients):

        bc_1,bc_2,bc_3,ac_1,ac_2,ac_3,ac_4,ac_5,ac_6,ic_1,ic_2,ic_3 = interaction_coefficients

        inputs_directories = (self.physics_computation_1_inputs_directory,self.physics_computation_2_inputs_directory,self.physics_computation_3_inputs_directory,self.physics_computation_4_inputs_directory)
        in_file_locations = (self.physics_computation_1_in_file_location,self.physics_computation_2_in_file_location,self.physics_computation_3_in_file_location,self.physics_computation_4_in_file_location)

        for i in (0,1,2,3):

            constant_head = open(inputs_directories[i]+'in_file_constant_head.txt').read()
            constant_tail = open(inputs_directories[i]+'in_file_constant_tail.txt').read()

            coeff_information = '\n\
bond_coeff 1 {0} 5.242 # CL1-CL1\n\
bond_coeff 2 {1} 1.955 # CL2-CL1\n\
bond_coeff 3 {2} 2.250 # CL3-CL1\n\
\n\
angle_coeff 1 {3} 166.2 # CL1-CL1-CL1\n\
angle_coeff 2 {4}  77.0 # CL2-CL1-CL1_1\n\
angle_coeff 3 {5}  71.4 # CL3-CL1-CL1_1\n\
angle_coeff 4 {6} 112.5 # CL2-CL1-CL1_2\n\
angle_coeff 5 {7}  97.3 # CL3-CL1-CL1_2\n\
angle_coeff 6 {8} 147.5 # CL2-CL1-CL3\n\
\n\
improper_coeff 1 {9} 176.7 # CL1-CL1-CL1-CL1\n\
improper_coeff 2 {10}   7.8 # CL2-CL1-CL1-CL3\n\
improper_coeff 3 {11}   9.1 # CL3-CL1-CL1-CL2\n\
\n'.format(bc_1,bc_2,bc_3,ac_1,ac_2,ac_3,ac_4,ac_5,ac_6,ic_1,ic_2,ic_3)

            in_file_content = constant_head+coeff_information+constant_tail
            in_file = open(in_file_locations[i],'w')
            in_file.write(in_file_content)
            in_file.close()

        numpy.savetxt(self.interaction_coefficients_location,interaction_coefficients,header=interaction_coefficients_header,fmt='%.6f',delimiter=',')

