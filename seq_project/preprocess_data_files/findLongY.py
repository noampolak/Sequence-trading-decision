def findLongY(capLeverage, wantedYield, yieldArray):
    posY_interval = zeros(rows(yieldArray),1)

#   start with the second
  
    basecap = 1
    local_pos_cap = basecap
    len_array = length(yieldArray)
    i_lead = 1
    i_leg = 1
    local_pos_cap *= (1 + yieldArray(i_lead))
    while i_lead < len_array:
#   there are 5 possible actions - yield cause an absolute loss - intervalIndex = 0
#  pos cap reaches wanted yield - intervalIndex = 1 and the leg increase by 1 and - 
#  poscap and neg cap recalculate with yieldcalc function
#  neg cap reaches wanted yield - intervalIndex = 1 and the leg increase by 1 and - 
#  poscap and neg cap recalculate with yieldcalc function
#  if none of them happend than i_lead ncrease by 1
    
# [i_leg,posY_interval,local_pos_cap] = recLoseLongCheck(yieldArray, i_leg, i_lead, basecap, local_pos_cap,posY_interval);
        if (local_pos_cap < basecap):
            i_leg = i_lead+1
            local_pos_cap = basecap
   
        if (local_pos_cap > basecap * (1+ wantedYield/capLeverage)):
            posY_interval(i_leg) = 1
            i_leg = i_leg + 1
            local_pos_cap = basecap * (1 + yieldcalc(yieldArray,i_leg,i_lead))
            # adjust local_pos_cap and local_neg_cap
        else:
            i_lead = i_lead + 1
            local_pos_cap *= (1 + yieldArray(i_lead))
