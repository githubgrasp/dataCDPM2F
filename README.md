Info for input files for article "CDPM2F: A damage-plasticity approach for modelling the failure of strain hardening cementitious composites", Chao Zhou, Antoine Marlot and Peter Grassl, University of Glasgow 2024. The article is accepted in Engineering Fracture Mechanics. The pre-print is available at  

Three tests are included in this folder: structural tensile test; structural compressive test; structural shear test.
In tensile test: tensile_test/...
12mm long fibers are investigated with three mesh sizes(0.04m,0.02m,0.01m)
6mm short fibers are investigated with three mesh sizes(0.04m,0.02m,0.01m)

In compressive test: compressive_test/...
cylinder column are tested with three mesh sizes(0.04m,0.02m,0.01m)

In shear test: shear_test/...
ohno beam are tested with three mesh sizes(0.04m,0.02m,0.01m)
material point input for tensile response

In each folder, there are 5 files (mesh.in; oofem.t3d.ctrl; oofem.in; strain.py; combine.py;)

After running oofem.in, use command:'extractor.py -f oofem.in>ld.dat' 
Then use python script (strain.py;combine.py) to extract strain and stress data.
Run the command 'python strain.py'
Then run 'python combine.py'
New .dat file is be stress and strain data file for each test.