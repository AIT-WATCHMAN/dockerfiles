import urllib.request
import os.path
from subprocess import call
import argparse

def getargs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--base', action='store_true',
            help='Rebuild the base image')
    return parser.parse_args()

def download(url, name):
    print('Downloading %s to %s'%(url,name))
    if os.path.isfile(name):
        print(' -- file already available, skipping')
        return
    urllib.request.urlretrieve(url, name)

args = getargs()

files_to_download = { 
        'root.tar.gz':'https://root.cern.ch/download/root_v5.34.32.source.tar.gz',
        'geant.tar.gz':'https://github.com/Geant4/geant4/archive/v10.4.2.tar.gz',
        'G4NDL.tar.gz':'http://cern.ch/geant4-data/datasets/G4NDL.4.5.tar.gz',
        'G4EMLOW.tar.gz':'http://cern.ch/geant4-data/datasets/G4EMLOW.7.3.tar.gz',
        'G4PhotonEvaporation.tar.gz':'http://cern.ch/geant4-data/datasets/G4PhotonEvaporation.5.2.tar.gz',
        'G4RadioactiveDecay.tar.gz':'http://cern.ch/geant4-data/datasets/G4RadioactiveDecay.5.2.tar.gz',
        'G4SAIDDATA.tar.gz':'http://cern.ch/geant4-data/datasets/G4SAIDDATA.1.1.tar.gz',
        'G4NEUTRONXS.tar.gz':'http://cern.ch/geant4-data/datasets/G4NEUTRONXS.1.4.tar.gz',
        'G4ABLA.tar.gz':'http://cern.ch/geant4-data/datasets/G4ABLA.3.1.tar.gz',
        'G4PII.tar.gz':'http://cern.ch/geant4-data/datasets/G4PII.1.3.tar.gz',
        'G4ENSDFSTATE.tar.gz':'http://cern.ch/geant4-data/datasets/G4ENSDFSTATE.2.2.tar.gz',
        'G4RealSurface.tar.gz':'http://cern.ch/geant4-data/datasets/G4RealSurface.2.1.1.tar.gz',
        'G4TENDL.tar.gz':'http://cern.ch/geant4-data/datasets/G4TENDL.1.3.2.tar.gz',
        }

for k,v in files_to_download.items():
    download(v, k)

if args.base:
    cmd = 'docker build -f Dockerfile.base -t aitwatchman/simulation:base .'.split(' ')
    call(cmd)

# Build the rat-pac image
cmd = 'docker build -f Dockerfile -t aitwatchman/simulation:latest .'.split(' ')
call(cmd)
