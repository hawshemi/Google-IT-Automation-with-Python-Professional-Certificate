#!/usr/bin/env python3

import subprocess
import os

from multiprocessing import Pool

def run(task):
    print(task)
    subprocess.run(["rsync", "-varq", task, dest])

src = "/home/student-XXX/data/prod/" # Replace XXX to your actual user path
dest = "/home/student-XXX/data/prod_backup/" # Replace XXX to your actual user path

dir_tasks = [os.path.join(src, x) for x in os.listdir(src)]
p = Pool(len(dir_tasks))
p.map(run, dir_tasks)
