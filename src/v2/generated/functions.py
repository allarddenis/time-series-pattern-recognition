# ------------------------------------------
# This file was auto-generated on 2017-11-23
# By Florine Cercle - Denis Allard
# ------------------------------------------

import operator

# ----- MAX -----
# ----- MAX MIN -----
# MAX MIN INCREASING
def max_min_increasing(data):
    C = float('-inf')
    D = float('inf')
    R = float('-inf')
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    D = float('inf')                    
                    R = max(R_temp,min(min(D_temp,data[i]),data[i+1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return max(R,C)    

# MAX MIN INCREASING_TERRACE
def max_min_increasing_terrace(data):
    C = float('-inf')
    D = float('inf')
    R = float('-inf')
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = float('inf')                    
                    R = max(R_temp,min(D_temp,data[i]))                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = float('inf')                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX MIN PEAK
def max_min_peak(data):
    C = float('-inf')
    D = float('inf')
    R = float('-inf')
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = float('-inf')                    
                    D = float('inf')                    
                    R = max(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = min(D_temp,data[i])                    
                    D = float('inf')                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = min(C_temp,min(D_temp,data[i]))                    
                    D = float('inf')                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i])                    
                    currentState = 't'                    
    return max(R,C)    

# ----- MAX MAX -----
# MAX MAX INCREASING
def max_max_increasing(data):
    C = float('-inf')
    D = float('-inf')
    R = float('-inf')
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    D = float('-inf')                    
                    R = max(R_temp,max(max(D_temp,data[i]),data[i+1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return max(R,C)    

# MAX MAX INCREASING_TERRACE
def max_max_increasing_terrace(data):
    C = float('-inf')
    D = float('-inf')
    R = float('-inf')
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = float('-inf')                    
                    R = max(R_temp,max(D_temp,data[i]))                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = float('-inf')                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX MAX PEAK
def max_max_peak(data):
    C = float('-inf')
    D = float('-inf')
    R = float('-inf')
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = float('-inf')                    
                    D = float('-inf')                    
                    R = max(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = max(D_temp,data[i])                    
                    D = float('-inf')                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,data[i]))                    
                    D = float('-inf')                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i])                    
                    currentState = 't'                    
    return max(R,C)    

# ----- MAX SURFACE -----
# MAX SURFACE INCREASING
def max_surface_increasing(data):
    C = float('-inf')
    D = 0
    R = float('-inf')
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    D = 0                    
                    R = max(R_temp,operator.add(operator.add(D_temp,data[i]),data[i+1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return max(R,C)    

# MAX SURFACE INCREASING_TERRACE
def max_surface_increasing_terrace(data):
    C = float('-inf')
    D = 0
    R = float('-inf')
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    R = max(R_temp,operator.add(D_temp,data[i]))                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX SURFACE PEAK
def max_surface_peak(data):
    C = float('-inf')
    D = 0
    R = float('-inf')
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = float('-inf')                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = operator.add(D_temp,data[i])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,data[i]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i])                    
                    currentState = 't'                    
    return max(R,C)    

# ----- MAX ONE -----
# MAX ONE INCREASING
def max_one_increasing(data):
    C = 1
    D = 1
    R = 1
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    D = 1                    
                    R = max(R_temp,max(max(D_temp,0),data[i+1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return max(R,C)    

# MAX ONE INCREASING_TERRACE
def max_one_increasing_terrace(data):
    C = 1
    D = 1
    R = 1
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 1                    
                    R = max(R_temp,max(D_temp,0))                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 1                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,0)                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = max(D_temp,0)                    
                    currentState = 't'                    
    return max(R,C)    

# MAX ONE PEAK
def max_one_peak(data):
    C = 1
    D = 1
    R = 1
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = max(D_temp,0)                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 1                    
                    D = 1                    
                    R = max(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = max(D_temp,0)                    
                    D = 1                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,0))                    
                    D = 1                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,0)                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = max(D_temp,0)                    
                    currentState = 't'                    
    return max(R,C)    

# ----- MAX WIDTH -----
# MAX WIDTH INCREASING
def max_width_increasing(data):
    C = 0
    D = 0
    R = 0
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    D = 0                    
                    R = max(R_temp,operator.add(operator.add(D_temp,1),data[i+1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return max(R,C)    

# MAX WIDTH INCREASING_TERRACE
def max_width_increasing_terrace(data):
    C = 0
    D = 0
    R = 0
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    R = max(R_temp,operator.add(D_temp,1))                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,1)                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,1)                    
                    currentState = 't'                    
    return max(R,C)    

# MAX WIDTH PEAK
def max_width_peak(data):
    C = 0
    D = 0
    R = 0
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 0                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = operator.add(D_temp,1)                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,1))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,1)                    
                    currentState = 't'                    
    return max(R,C)    

# ----- MAX RANGE -----
# MAX RANGE INCREASING
def max_range_increasing(data):
    C = 0
    D = 0
    R = 0
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    D = 0                    
                    R = max(R_temp,((D_temp,data[i]),data[i+1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return max(R,C)    

# MAX RANGE INCREASING_TERRACE
def max_range_increasing_terrace(data):
    C = 0
    D = 0
    R = 0
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    R = max(R_temp,(D_temp,data[i]))                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = (D_temp,data[i])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX RANGE PEAK
def max_range_peak(data):
    C = 0
    D = 0
    R = 0
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 0                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = (D_temp,data[i])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = (C_temp,(D_temp,data[i]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = (D_temp,data[i])                    
                    currentState = 't'                    
    return max(R,C)    

# ----- SUM -----
# ----- SUM MIN -----
# SUM MIN INCREASING
def sum_min_increasing(data):
    C = 0
    D = float('inf')
    R = 0
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    D = float('inf')                    
                    R = sum(R_temp,min(min(D_temp,data[i]),data[i+1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return sum(R,C)    

# SUM MIN INCREASING_TERRACE
def sum_min_increasing_terrace(data):
    C = 0
    D = float('inf')
    R = 0
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = float('inf')                    
                    R = sum(R_temp,min(D_temp,data[i]))                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = float('inf')                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i])                    
                    currentState = 't'                    
    return sum(R,C)    

# SUM MIN PEAK
def sum_min_peak(data):
    C = 0
    D = float('inf')
    R = 0
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 0                    
                    D = float('inf')                    
                    R = sum(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = min(D_temp,data[i])                    
                    D = float('inf')                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = min(C_temp,min(D_temp,data[i]))                    
                    D = float('inf')                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i])                    
                    currentState = 't'                    
    return sum(R,C)    

# ----- SUM MAX -----
# SUM MAX INCREASING
def sum_max_increasing(data):
    C = 0
    D = float('-inf')
    R = 0
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    D = float('-inf')                    
                    R = sum(R_temp,max(max(D_temp,data[i]),data[i+1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return sum(R,C)    

# SUM MAX INCREASING_TERRACE
def sum_max_increasing_terrace(data):
    C = 0
    D = float('-inf')
    R = 0
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = float('-inf')                    
                    R = sum(R_temp,max(D_temp,data[i]))                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = float('-inf')                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i])                    
                    currentState = 't'                    
    return sum(R,C)    

# SUM MAX PEAK
def sum_max_peak(data):
    C = 0
    D = float('-inf')
    R = 0
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 0                    
                    D = float('-inf')                    
                    R = sum(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = max(D_temp,data[i])                    
                    D = float('-inf')                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,data[i]))                    
                    D = float('-inf')                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i])                    
                    currentState = 't'                    
    return sum(R,C)    

# ----- SUM SURFACE -----
# SUM SURFACE INCREASING
def sum_surface_increasing(data):
    C = 0
    D = 0
    R = 0
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    D = 0                    
                    R = sum(R_temp,operator.add(operator.add(D_temp,data[i]),data[i+1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return sum(R,C)    

# SUM SURFACE INCREASING_TERRACE
def sum_surface_increasing_terrace(data):
    C = 0
    D = 0
    R = 0
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    R = sum(R_temp,operator.add(D_temp,data[i]))                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i])                    
                    currentState = 't'                    
    return sum(R,C)    

# SUM SURFACE PEAK
def sum_surface_peak(data):
    C = 0
    D = 0
    R = 0
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 0                    
                    D = 0                    
                    R = sum(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = operator.add(D_temp,data[i])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,data[i]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i])                    
                    currentState = 't'                    
    return sum(R,C)    

# ----- SUM ONE -----
# SUM ONE INCREASING
def sum_one_increasing(data):
    C = 0
    D = 1
    R = 0
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    D = 1                    
                    R = sum(R_temp,max(max(D_temp,0),data[i+1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return sum(R,C)    

# SUM ONE INCREASING_TERRACE
def sum_one_increasing_terrace(data):
    C = 0
    D = 1
    R = 0
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 1                    
                    R = sum(R_temp,max(D_temp,0))                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 1                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,0)                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = max(D_temp,0)                    
                    currentState = 't'                    
    return sum(R,C)    

# SUM ONE PEAK
def sum_one_peak(data):
    C = 0
    D = 1
    R = 0
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = max(D_temp,0)                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 0                    
                    D = 1                    
                    R = sum(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = max(D_temp,0)                    
                    D = 1                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,0))                    
                    D = 1                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,0)                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = max(D_temp,0)                    
                    currentState = 't'                    
    return sum(R,C)    

# ----- SUM WIDTH -----
# SUM WIDTH INCREASING
def sum_width_increasing(data):
    C = 0
    D = 0
    R = 0
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    D = 0                    
                    R = sum(R_temp,operator.add(operator.add(D_temp,1),data[i+1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return sum(R,C)    

# SUM WIDTH INCREASING_TERRACE
def sum_width_increasing_terrace(data):
    C = 0
    D = 0
    R = 0
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    R = sum(R_temp,operator.add(D_temp,1))                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,1)                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,1)                    
                    currentState = 't'                    
    return sum(R,C)    

# SUM WIDTH PEAK
def sum_width_peak(data):
    C = 0
    D = 0
    R = 0
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 0                    
                    D = 0                    
                    R = sum(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = operator.add(D_temp,1)                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,1))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,1)                    
                    currentState = 't'                    
    return sum(R,C)    

# ----- SUM RANGE -----
# SUM RANGE INCREASING
def sum_range_increasing(data):
    C = 0
    D = 0
    R = 0
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    D = 0                    
                    R = sum(R_temp,((D_temp,data[i]),data[i+1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return sum(R,C)    

# SUM RANGE INCREASING_TERRACE
def sum_range_increasing_terrace(data):
    C = 0
    D = 0
    R = 0
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    R = sum(R_temp,(D_temp,data[i]))                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = (D_temp,data[i])                    
                    currentState = 't'                    
    return sum(R,C)    

# SUM RANGE PEAK
def sum_range_peak(data):
    C = 0
    D = 0
    R = 0
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 0                    
                    D = 0                    
                    R = sum(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = (D_temp,data[i])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = (C_temp,(D_temp,data[i]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = (D_temp,data[i])                    
                    currentState = 't'                    
    return sum(R,C)    

# ----- MIN -----
# ----- MIN MIN -----
# MIN MIN INCREASING
def min_min_increasing(data):
    C = float('inf')
    D = float('inf')
    R = float('inf')
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    D = float('inf')                    
                    R = min(R_temp,min(min(D_temp,data[i]),data[i+1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return min(R,C)    

# MIN MIN INCREASING_TERRACE
def min_min_increasing_terrace(data):
    C = float('inf')
    D = float('inf')
    R = float('inf')
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = float('inf')                    
                    R = min(R_temp,min(D_temp,data[i]))                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = float('inf')                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN MIN PEAK
def min_min_peak(data):
    C = float('inf')
    D = float('inf')
    R = float('inf')
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = float('inf')                    
                    D = float('inf')                    
                    R = min(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = min(D_temp,data[i])                    
                    D = float('inf')                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = min(C_temp,min(D_temp,data[i]))                    
                    D = float('inf')                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i])                    
                    currentState = 't'                    
    return min(R,C)    

# ----- MIN MAX -----
# MIN MAX INCREASING
def min_max_increasing(data):
    C = float('inf')
    D = float('-inf')
    R = float('inf')
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    D = float('-inf')                    
                    R = min(R_temp,max(max(D_temp,data[i]),data[i+1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return min(R,C)    

# MIN MAX INCREASING_TERRACE
def min_max_increasing_terrace(data):
    C = float('inf')
    D = float('-inf')
    R = float('inf')
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = float('-inf')                    
                    R = min(R_temp,max(D_temp,data[i]))                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = float('-inf')                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN MAX PEAK
def min_max_peak(data):
    C = float('inf')
    D = float('-inf')
    R = float('inf')
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = float('inf')                    
                    D = float('-inf')                    
                    R = min(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = max(D_temp,data[i])                    
                    D = float('-inf')                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,data[i]))                    
                    D = float('-inf')                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i])                    
                    currentState = 't'                    
    return min(R,C)    

# ----- MIN SURFACE -----
# MIN SURFACE INCREASING
def min_surface_increasing(data):
    C = float('inf')
    D = 0
    R = float('inf')
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    D = 0                    
                    R = min(R_temp,operator.add(operator.add(D_temp,data[i]),data[i+1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return min(R,C)    

# MIN SURFACE INCREASING_TERRACE
def min_surface_increasing_terrace(data):
    C = float('inf')
    D = 0
    R = float('inf')
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    R = min(R_temp,operator.add(D_temp,data[i]))                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN SURFACE PEAK
def min_surface_peak(data):
    C = float('inf')
    D = 0
    R = float('inf')
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = float('inf')                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = operator.add(D_temp,data[i])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,data[i]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i])                    
                    currentState = 't'                    
    return min(R,C)    

# ----- MIN ONE -----
# MIN ONE INCREASING
def min_one_increasing(data):
    C = 1
    D = 1
    R = 1
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    D = 1                    
                    R = min(R_temp,max(max(D_temp,0),data[i+1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return min(R,C)    

# MIN ONE INCREASING_TERRACE
def min_one_increasing_terrace(data):
    C = 1
    D = 1
    R = 1
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 1                    
                    R = min(R_temp,max(D_temp,0))                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 1                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,0)                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = max(D_temp,0)                    
                    currentState = 't'                    
    return min(R,C)    

# MIN ONE PEAK
def min_one_peak(data):
    C = 1
    D = 1
    R = 1
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = max(D_temp,0)                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 1                    
                    D = 1                    
                    R = min(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = max(D_temp,0)                    
                    D = 1                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,0))                    
                    D = 1                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,0)                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = max(D_temp,0)                    
                    currentState = 't'                    
    return min(R,C)    

# ----- MIN WIDTH -----
# MIN WIDTH INCREASING
def min_width_increasing(data):
    C = len(data)
    D = 0
    R = len(data)
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    D = 0                    
                    R = min(R_temp,operator.add(operator.add(D_temp,1),data[i+1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return min(R,C)    

# MIN WIDTH INCREASING_TERRACE
def min_width_increasing_terrace(data):
    C = len(data)
    D = 0
    R = len(data)
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    R = min(R_temp,operator.add(D_temp,1))                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,1)                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,1)                    
                    currentState = 't'                    
    return min(R,C)    

# MIN WIDTH PEAK
def min_width_peak(data):
    C = len(data)
    D = 0
    R = len(data)
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = len(data)                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = operator.add(D_temp,1)                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,1))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,1)                    
                    currentState = 't'                    
    return min(R,C)    

# ----- MIN RANGE -----
# MIN RANGE INCREASING
def min_range_increasing(data):
    C = float('inf')
    D = 0
    R = float('inf')
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    D = 0                    
                    R = min(R_temp,((D_temp,data[i]),data[i+1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return min(R,C)    

# MIN RANGE INCREASING_TERRACE
def min_range_increasing_terrace(data):
    C = float('inf')
    D = 0
    R = float('inf')
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    R = min(R_temp,(D_temp,data[i]))                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = (D_temp,data[i])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN RANGE PEAK
def min_range_peak(data):
    C = float('inf')
    D = 0
    R = float('inf')
    currentState = 's'
    for i in xrange(1,len(data)):    
        if(i < len(data)):        
            C_temp = C            
            D_temp = D            
            R_temp = R            
            if data[i] > data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = float('inf')                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = (D_temp,data[i])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = (C_temp,(D_temp,data[i]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = (D_temp,data[i])                    
                    currentState = 't'                    
    return min(R,C)    

