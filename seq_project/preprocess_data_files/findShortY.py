import numpy as np
import pandas as pd
from helpers.yieldcalc import yieldcalc

def find_short_Y(capLeverage, wantedYield, yieldArray):
    negY_interval = np.zeros((yieldArray.shape[0],1))
    yieldArray = yieldArray.to_numpy()
#   %start with the second 
    basecap = 1
    local_neg_cap = basecap
    len_array = yieldArray.shape[0] -1
    i_lead = 1
    i_leg = 1
    local_neg_cap *= (1 - yieldArray[i_lead])
    while i_lead < len_array:
#  % there are 5 possible actions - yield cause an absolute loss - intervalIndex = 0
#   pos cap reaches wanted yield - intervalIndex = 1 and the leg increase by 1 and - 
#   poscap and neg cap recalculate with yieldcalc function
#   neg cap reaches wanted yield - intervalIndex = 1 and the leg increase by 1 and - 
#   poscap and neg cap recalculate with yieldcalc function
#   if none of them happend than i_lead ncrease by 1

#    [i_leg,negY_interval,local_neg_cap] = recLoseShortCheck (yieldArray, i_lead, i_leg,basecap,local_neg_cap,negY_interval);
        if (local_neg_cap < basecap):
            i_leg = i_lead + 1
            local_neg_cap = basecap
        if local_neg_cap > basecap * (1+ wantedYield/capLeverage):
            negY_interval[i_leg] = 2
            i_leg += 1
            local_neg_cap = basecap * (1 - yieldcalc(yieldArray,i_leg,i_lead))
        else:
            i_lead = i_lead + 1
            local_neg_cap *= (1 - yieldArray[i_lead])
    return negY_interval