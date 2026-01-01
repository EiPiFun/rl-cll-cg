import numpy

estimated_interaction_coefficients = (62.00,51.00,136.39,30.00,14.96,25.89,17.65,20.77,10.82,0.25,0.22,0.23)

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
bond_coeff 1 {0} 5.273 # CL1-CL1\n\
bond_coeff 2 {1} 2.188 # CL2-CL1\n\
bond_coeff 3 {2} 2.353 # CL3-CL1\n\
\n\
angle_coeff 1 {3} 161.9 # CL1-CL1-CL1\n\
angle_coeff 2 {4} 109.8 # CL2-CL1-CL1_1\n\
angle_coeff 3 {5}  81.5 # CL3-CL1-CL1_1\n\
angle_coeff 4 {6}  87.9 # CL2-CL1-CL1_2\n\
angle_coeff 5 {7}  80.4 # CL3-CL1-CL1_2\n\
angle_coeff 6 {8} 167.3 # CL2-CL1-CL3\n\
\n\
improper_coeff 1 {9} 176.9 # CL1-CL1-CL1-CL1\n\
improper_coeff 2 {10}   2.0 # CL2-CL1-CL1-CL3\n\
improper_coeff 3 {11}   2.1 # CL3-CL1-CL1-CL2\n\
\n'.format(bc_1,bc_2,bc_3,ac_1,ac_2,ac_3,ac_4,ac_5,ac_6,ic_1,ic_2,ic_3)

            in_file_content = constant_head+coeff_information+constant_tail
            in_file = open(in_file_locations[i],'w')
            in_file.write(in_file_content)
            in_file.close()

        numpy.savetxt(self.interaction_coefficients_location,interaction_coefficients,header=interaction_coefficients_header,fmt='%.6f',delimiter=',')

