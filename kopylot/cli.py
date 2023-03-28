import subprocess
import sys

args = sys.argv[1:]
subprocess.call(["kubectl"] + args)