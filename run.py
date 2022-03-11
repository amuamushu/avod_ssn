import sys
import os
import json
import shutil
import subprocess

from avod.experiments import run_evaluation, run_inference, run_training
from utils_avod import avod_utils

OUTPUT_PATH = "./outputs"

def main(targets):
    '''
    Runs the main project pipeline logic, given the targets.
    targets must contain: 'data', 'analysis', 'model'. 
    
    `main` runs the targets in order of data=>analysis=>model.
    '''
    if 'clean' in targets:
        if os.path.exists(OUTPUT_PATH):
            shutil.rmtree(OUTPUT_PATH)
        os.mkdir(OUTPUT_PATH)
        
    if 'test' in targets:
        with open('config/test.json') as fh:
            test_config = json.load(fh)

        # make the data target
        avod_utils.run_main_with_command_line_args(run_training, **(test_config['training']))
        avod_utils.run_main_with_command_line_args(run_inference, **(test_config['inference']))
        return

    if 'adv-test' in targets:
        with open('config/test_adv.json') as fh:
            test_config = json.load(fh)

        # make the data target
        avod_utils.run_main_with_command_line_args(run_training, **(test_config['training']))
        avod_utils.run_main_with_command_line_args(run_inference, **(test_config['inference']))
        return

    if 'adv-model' in targets:
        # Runs the training and all the inferences (clean, adversarial, and SSN) on trained
        # model. Training is skipped if the model is already trained.
        subprocess.call(['scripts/sin_test/rand_5/run_adv.sh'])
        return
    
    if 'clean-model' in targets:
        # Runs the training and the adversarial inferences on trained
        # model. Training is skipped if the model is already trained.
        subprocess.call(['scripts/sin_test/rand_5/run_pyramid_cars_with_aug_simple.sh'])
        return

    if 'ssn-model' in targets:
        # Runs the training and the adversarial inferences on trained
        # model. Training is skipped if the model is already trained.        
        subprocess.call(['scripts/sin_test/rand_5/run_trainsin_pyramid_cars_with_aug_simple.sh'])
        return


if __name__ == '__main__':
    # run via:
    # python main.py data features model
    targets = sys.argv[1:]
    main(targets)