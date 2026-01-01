import numpy

estimated_interaction_coefficients = (65.00, 113.95,-1027.78,2326.55, 152.66,
                          30.00, 83.59,-948.45,2664.18, 99.71, 51.77,-555.66,1563.45, 62.33, 112.18,-1433.94,4230.00,
                           0.20, 0.39, 0.71)

interaction_coefficients_header = 'bc_1,bc_2,bc_2_3,bc_2_4,bc_3,ac_1,ac_2,ac_2_3,ac_2_4,ac_3,ac_4,ac_4_3,ac_4_4,ac_5,ac_6,ac_6_3,ac_6_4,ic_1,ic_2,ic_3'

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

        bc_1,bc_2,bc_2_3,bc_2_4,bc_3,ac_1,ac_2,ac_2_3,ac_2_4,ac_3,ac_4,ac_4_3,ac_4_4,ac_5,ac_6,ac_6_3,ac_6_4,ic_1,ic_2,ic_3 = interaction_coefficients

        inputs_directories = (self.physics_computation_1_inputs_directory,self.physics_computation_2_inputs_directory,self.physics_computation_3_inputs_directory,self.physics_computation_4_inputs_directory)
        in_file_locations = (self.physics_computation_1_in_file_location,self.physics_computation_2_in_file_location,self.physics_computation_3_in_file_location,self.physics_computation_4_in_file_location)

        for i in (0,1,2,3):

            constant_head = open(inputs_directories[i]+'in_file_constant_head.txt').read()
            constant_tail = open(inputs_directories[i]+'in_file_constant_tail.txt').read()

            coeff_information = '\n\
bond_coeff 1 harmonic {0} 5.277 # CL1-CL1\n\
bond_coeff 2 class2         2.457 {1} {2} {3} # CL2-CL1\n\
bond_coeff 3 harmonic {4} 2.078 # CL3-CL1\n\
\n\
angle_coeff 1 harmonic {5} 163.4 # CL1-CL1-CL1\n\
angle_coeff 2 class2          74.1 {6} {7} {8} # CL2-CL1-CL1_1\n\
angle_coeff 3 harmonic {9}  94.9 # CL3-CL1-CL1_1\n\
angle_coeff 4 class2          90.5 {10} {11} {12} # CL2-CL1-CL1_2\n\
angle_coeff 5 harmonic {13} 100.4 # CL3-CL1-CL1_2\n\
angle_coeff 6 class2         168.0 {14} {15} {16} # CL2-CL1-CL3\n\
\n\
improper_coeff 1 {17} 173.7 # CL1-CL1-CL1-CL1\n\
improper_coeff 2 {18}   4.8 # CL2-CL1-CL1-CL3\n\
improper_coeff 3 {19}   4.7 # CL3-CL1-CL1-CL2\n\
\n'.format(bc_1,bc_2,bc_2_3,bc_2_4,bc_3,ac_1,ac_2,ac_2_3,ac_2_4,ac_3,ac_4,ac_4_3,ac_4_4,ac_5,ac_6,ac_6_3,ac_6_4,ic_1,ic_2,ic_3)

            in_file_content = constant_head+coeff_information+constant_tail
            in_file = open(in_file_locations[i],'w')
            in_file.write(in_file_content)
            in_file.close()

        numpy.savetxt(self.interaction_coefficients_location,interaction_coefficients,header=interaction_coefficients_header,fmt='%.6f',delimiter=',')

