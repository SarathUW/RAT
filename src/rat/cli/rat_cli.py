import argparse
import os
from pathlib import Path
import subprocess
import requests, zipfile, io


def init_func(args):
    print("Initializing RAT using: ", args)

    #### Directory creation
    if args.project_dir is None:
        project_dir_input = input(f"Enter path of RAT project directory: ")
        project_dir = Path(project_dir_input).resolve()
    else:
        project_dir = Path(args.project_dir).resolve()
    
    try:
        project_dir.mkdir(exist_ok=True)
    except Exception as e:
        print(f"Failed creating RAT project directory: {e}")
        raise e

    # create additional directories
    data_dir = project_dir.joinpath('data')
    data_dir.mkdir(exist_ok=True)
    models_dir = project_dir.joinpath('models')
    models_dir.mkdir(exist_ok=True)

    # install metsim
    metsim_path = models_dir.joinpath('metsim')
    cmd = f"conda create -p {metsim_path} -c conda-forge metsim -y".split(" ")
    print(f"Installing Metsim: {' '.join(cmd)}")
    subprocess.run(cmd)
    
    # install vic
    vic_path = models_dir.joinpath('vic')
    cmd = f"conda create -p {vic_path} -c conda-forge vic -y".split(" ")
    print(f"Installing VIC: {' '.join(cmd)}")
    subprocess.run(cmd)
    
    # install route
    print(f"Downloading source code of routing model")
    route_model_src_dl_path = "https://www.dropbox.com/s/9jwep2g5pyj8sni/routing.zip?dl=1"
    r = requests.get(route_model_src_dl_path)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(models_dir)
    route_model = models_dir.joinpath("routing")
    cmd = f"make"
    print(f"Installing VIC-Route using make in directory: {route_model}")
    subprocess.run(cmd, cwd=route_model)

def run_func(args):
    print("Running RAT using: ", args) # TODO: debug line, delete later

def main():
    ## CLI interface
    p = argparse.ArgumentParser(description='Reservoir Assessment Tool')

    # Treat the different commands, such as `init`, and `run` as different sub parsers
    command_parsers = p.add_subparsers()

    # Init command
    init_parser = command_parsers.add_parser('init', help='Initialize RAT')

    # options for init parser
    init_parser.add_argument(
        '-d', '--dir', 
        help='Specify RAT project directory', 
        action='store',
        dest='project_dir',
        required=False
    )

    init_parser.set_defaults(func=init_func)

    # Run command
    run_parser = command_parsers.add_parser('run', help='Run RAT')

    run_parser.add_argument(
        '-p', '--param',
        help='RAT Parameter file',
        action='store',
        dest='param',
        required=True
    )
    
    run_parser.set_defaults(func=run_func)

    args = p.parse_args(['init', '-d', '/mnt/2tb/pritam/rat_test/RAT'])
    # args = p.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()