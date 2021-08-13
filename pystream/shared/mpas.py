from abc import ABCMeta, abstractmethod
from osgeo import gdal, osr, ogr
import numpy as np
import json

from pystream.shared.vertex import pyvertex
from pystream.shared.edge import pyedge
from pystream.shared.cell import pycell
from pystream.shared.flowline import pyflowline

import numpy as np
import json
from json import JSONEncoder

class CellClassEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, pyedge):
            return obj.lEdgeID
        if isinstance(obj, pyvertex):
            return obj.lVertexID
        if isinstance(obj, pyflowline):
            return obj.lFlowlineID
        return JSONEncoder.default(self, obj)

class pympas(pycell):
    
    nFlowline=0
    nVertex =0 
    nEdge=0
    dLength=0.0
    dArea=0.0
    dx_center=0.0
    dy_center=0.0
    dz_center=0.0
    dLon_center=0.0
    dLat_center=0.0
    dElevation=0.0

    aEdge=None
    aEdgeID=None
    aVertex=None
    aVertexID=None

    pVertex_center = None
    aFlowline=None
    lCellID  = -1
    nNeighbor=-1
    aNeighbor=None #the global ID of all neighbors

    def __init__(self, aEdge,aVertex):    
        nEdge = len(aEdge)
        if nEdge < 3 or nEdge > 8:
            pass
        else:                          
            self.aEdge = aEdge
            self.aVertex = aVertex #the first one and last one are the same
            self.nEdge = len(aEdge)
            self.nVertex = len(aVertex) 

            dLon=0.0
            dLat=0.0
            for i in range(self.nVertex):
                dLon = dLon + aVertex[i].dLongitude
                dLat = dLat + aVertex[i].dLatitude
                pass

            self.dLon_center = dLon/self.nVertex
            self.dLat_center = dLat/self.nVertex
            pVertex = dict()        
            pVertex['lon'] =self.dLon_center
            pVertex['lat'] =self.dLat_center           
            self.pVertex_center = pyvertex(pVertex)

            pass
        pass
    
   
    def has_this_edge(self, pEdge_in):
        iFlag_found = 0
        for pEdge in self.aEdge:
            if pEdge.is_overlap(pEdge_in):
                iFlag_found =1 
                break
            else:
                pass       
        
        return iFlag_found

    def which_edge_cross_this_vertex(self, pVertex_in):
        iFlag_found = 0
        pEdge_out = None
        for pEdge in self.aEdge:
            if( pEdge.check_vertex_on_edge(pVertex_in) ==1 ):
                iFlag_found =1
                pEdge_out = pEdge
                break

            else:
                pass

        return iFlag_found, pEdge_out
    
    def calculate_cell_area(self):
           
        self.dArea = 0.0
        return self.dArea

    def calculate_edge_length(self):
        
        self.dLength_edge =0.0
        return self.dLength_edge
    
    def share_edge(self, other):
        iFlag_share = 0
        for pEdge in self.aEdge:
            for pEdge2 in other.aEdge:
                if pEdge.is_overlap(pEdge2) ==1 :
                    iFlag_share = 1 
                    break

        return iFlag_share

    
    def tojson(self):
        sJson = json.dumps(self.__dict__, \
            sort_keys=True, \
                indent = 4, \
                    ensure_ascii=True, \
                        cls=CellClassEncoder)
        return sJson
