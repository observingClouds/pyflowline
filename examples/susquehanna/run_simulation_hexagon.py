import os, sys
from pathlib import Path
from os.path import realpath



#===================================
#set up workspace path
#===================================
sPath_parent = str(Path(__file__).parents[2]) # data is located two dir's up
import sys
sys.path.append(sPath_parent)
from pyflowline.pyflowline_read_model_configuration_file import pyflowline_read_model_configuration_file

sPath_data = realpath( sPath_parent +  '/data/susquehanna' )
sWorkspace_input =  str(Path(sPath_data)  /  'input')
sWorkspace_output=  str(Path(sPath_data)  /  'output')

#===================================
#you need to update this file based on your own case study
#===================================
sFilename_configuration_in = realpath( sPath_parent +  '/data/susquehanna/input/pyflowline_susquehanna_hexagon.json' )
if os.path.isfile(sFilename_configuration_in):
    pass
else:
    print('This configuration does not exist: ', sFilename_configuration_in )

#===================================
#setup case information
#===================================
iCase_index = 1
dResolution_meter = 50000

sMesh = 'hexagon'
sDate='20230101'

  
  
    
oPyflowline = pyflowline_read_model_configuration_file(sFilename_configuration_in, \
iCase_index_in=iCase_index, dResolution_meter_in=dResolution_meter, sDate_in=sDate)
oPyflowline.aBasin[0].dLatitude_outlet_degree=39.462000
oPyflowline.aBasin[0].dLongitude_outlet_degree=-76.009300
oPyflowline.setup()
oPyflowline.flowline_simplification()
aCell = oPyflowline.mesh_generation()
oPyflowline.reconstruct_topological_relationship(aCell)
oPyflowline.export()
iCase_index= iCase_index+1
           
print('Finished')


