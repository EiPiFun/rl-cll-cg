#!/usr/bin/sh

sh clean_results.sh
sh copy_to_update_the_common.sh
sh copy_to_update_physics_codes.sh
sh create_zip.sh
sh create_no_langevin.sh
sh create_no_velocity.sh
sh create_no_threshold.sh
sh create_suffix_off.sh


