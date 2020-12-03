import os
import sys
from subprocess import Popen, PIPE
from distutils.core import setup, Command
from modules import MODULES

class build(Command):
    
    description = 'Build to executable file'

    user_options = [
        ('show-progress','S','Show building progress'),
    ]
    boolean_options = ['show_progress']

    def initialize_options(self):
        self.packages = None
        self.compiler = None
        self.show_progress = None

        self.command_args = []

    def finalize_options(self):
        self.packages = self.distribution.packages

        if self.show_progress:
            self.command_args.append('--show-progress')

    def run(self):
        modules_str = [f'--include-module={package}' for package in self.packages]
        cmd = ' '.join([sys.executable,'-m','nuitka','--follow-imports','--mingw64','--remove-output','--output-dir=./build','./main.py',*modules_str,*self.command_args])
        print("Running:", cmd)
        proc = Popen(cmd,stdout=sys.stdout,stderr=sys.stderr)
        ec = proc.wait()
        if ec == 0:
            print("Build successfull")
        else:
            print("Build failed with exit-code:",ec)

def get_packages():
    packages = []
    
    for m in MODULES:
        packages.append(m)

    return packages

setup(
    name="lp-cli",
    packages=get_packages(),
    cmdclass={"build": build}
)