Docker Setup
------------

To run:
$ python setup.py
$ docker build -t watchdock .

# Setup.py prepares the directory prior to docker building
# and includes downloading root and geant4
Requires certain files download a priori
- Todo: Fix this so that they are wget if they don't exist
