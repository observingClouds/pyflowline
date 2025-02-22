from pyflowline.algorithms.auxiliary.check_head_water import check_head_water
def remove_small_river(aFlowline_in, dThreshold_in):
    """Remove small river that meet the threshold and headwater requirement, also dam flowline are reserved

    Args:
        aFlowline_in (_type_): _description_
        dThreshold_in (_type_): _description_

    Returns:
        List: Theortically, the flowline should be ordered from outlet to headwater
    """
    nFlowline = len(aFlowline_in)
    aFlowline_out=list()        
    if nFlowline == 1:
        aFlowline_out.append(aFlowline_in[0])
    else:
        lID = 0        
        for i in range(nFlowline):
            pFlowline = aFlowline_in[i]      
            iFlag_dam = pFlowline.iFlag_dam
            pVertex_start = pFlowline.pVertex_start
            pVertex_end = pFlowline.pVertex_end
            dLength = pFlowline.calculate_length()
            if iFlag_dam ==1:
                pFlowline.lFlowlineIndex = lID
                aFlowline_out.append(pFlowline)
                lID = lID +1       
            else:
                if pFlowline.iStream_order == 1:
                    if dLength > dThreshold_in :
                        pFlowline.lFlowlineIndex = lID
                        aFlowline_out.append(pFlowline)
                        lID = lID + 1 
                        pass
                    else:
                        pass
                    pass
                else: #this one might be not used     
                    pFlowline.lFlowlineIndex = lID
                    aFlowline_out.append(pFlowline)
                    lID = lID +1       
                    pass        
                    #if check_head_water(aFlowline_in, pVertex_start)==1:
                    #    if dLength > dThreshold_in :
                    #        pFlowline.lIndex = lID
                    #        aFlowline_out.append(pFlowline)
                    #        lID = lID + 1 
                    #        pass
                    #    else:
                    #        pass
                    #else:        
                    #    pFlowline.lIndex = lID
                    #    aFlowline_out.append(pFlowline)
                    #    lID = lID +1       
                    #    pass            
            
            pass    

    return aFlowline_out