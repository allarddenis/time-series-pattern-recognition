# ------------------------------------------
# This file was auto-generated on 2017-11-27
# By Florine Cercle - Denis Allard
# ------------------------------------------

import operator

# ----- MAX -----
# ----- MAX MIN -----
# MAX MIN BUMP_ON_DECREASING_SEQUENCE
def max_min_bump_on_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = float('inf')                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'v':                
                    D = float('inf')                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'v'                    
                elif currentState == 't':                
                    currentState = 't'                    
                elif currentState == 'v':                
                    D = float('inf')                    
                    R = max(R_temp,min(D_temp,data[i-1]))                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = float('inf')                    
                    currentState = 's'                    
                elif currentState == 't':                
                    currentState = 's'                    
                elif currentState == 'v':                
                    D = float('inf')                    
                    currentState = 's'                    
    return max(R,C)    

# MAX MIN STRICTLY_DECREASING_SEQUENCE
def max_min_strictly_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('-inf')                    
                    D = float('inf')                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    C = min(min(D_temp,data[i-1]),data[i])                    
                    D = float('inf')                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = min(C_temp,min(D_temp,data[i]))                    
                    D = float('inf')                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('-inf')                    
                    D = float('inf')                    
                    R = max(R_temp,C_temp)                    
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
                    R = max(R_temp,min(D_temp,data[i-1]))                    
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
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX MIN PROPER_PLATEAU
def max_min_proper_plateau(data):
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
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = float('inf')                    
                    R = max(R_temp,min(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX MIN INCREASING_SEQUENCE
def max_min_increasing_sequence(data):
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
                    C = min(min(D_temp,data[i-1]),data[i])                    
                    D = float('inf')                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = min(C_temp,min(D_temp,data[i]))                    
                    D = float('inf')                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    C = float('-inf')                    
                    D = float('inf')                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX MIN PLATEAU
def max_min_plateau(data):
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
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = float('inf')                    
                    R = max(R_temp,min(D_temp,data[i-1]))                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = float('inf')                    
                    R = max(R_temp,min(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX MIN STRICTLY_INCREASING_SEQUENCE
def max_min_strictly_increasing_sequence(data):
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
                    C = min(min(D_temp,data[i-1]),data[i])                    
                    D = float('inf')                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = min(C_temp,min(D_temp,data[i]))                    
                    D = float('inf')                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('-inf')                    
                    D = float('inf')                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('-inf')                    
                    D = float('inf')                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
    return max(R,C)    

# MAX MIN VALLEY
def max_min_valley(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = min(D_temp,data[i-1])                    
                    D = float('inf')                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = min(C_temp,min(D_temp,data[i-1]))                    
                    D = float('inf')                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = float('-inf')                    
                    D = float('inf')                    
                    R = max(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX MIN PROPER_PLAIN
def max_min_proper_plain(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = float('inf')                    
                    R = max(R_temp,min(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = float('inf')                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX MIN ZIGZAG
def max_min_zigzag(data):
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
                if currentState == 'a':                
                    currentState = 'a'                    
                elif currentState == 'c':                
                    C = float('-inf')                    
                    D = float('inf')                    
                    R = max(R_temp,C_temp)                    
                    currentState = 'a'                    
                elif currentState == 'b':                
                    C = min(D_temp,data[i-1])                    
                    D = float('inf')                    
                    currentState = 'c'                    
                elif currentState == 'e':                
                    D = float('inf')                    
                    currentState = 'a'                    
                elif currentState == 'd':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'e'                    
                elif currentState == 'f':                
                    C = min(C_temp,min(D_temp,data[i-1]))                    
                    D = float('inf')                    
                    currentState = 'c'                    
                elif currentState == 's':                
                    currentState = 'a'                    
            elif data[i] < data[i-1]:            
                if currentState == 'a':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'b'                    
                elif currentState == 'c':                
                    C = min(C_temp,min(D_temp,data[i-1]))                    
                    D = float('inf')                    
                    currentState = 'f'                    
                elif currentState == 'b':                
                    currentState = 'd'                    
                elif currentState == 'e':                
                    C = min(D_temp,data[i-1])                    
                    D = float('inf')                    
                    currentState = 'f'                    
                elif currentState == 'd':                
                    currentState = 'd'                    
                elif currentState == 'f':                
                    C = float('-inf')                    
                    D = float('inf')                    
                    R = max(R_temp,C_temp)                    
                    currentState = 'd'                    
                elif currentState == 's':                
                    currentState = 'd'                    
            elif data[i] == data[i-1]:            
                if currentState == 'a':                
                    currentState = 's'                    
                elif currentState == 'c':                
                    C = float('-inf')                    
                    D = float('inf')                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
                elif currentState == 'b':                
                    D = float('inf')                    
                    currentState = 's'                    
                elif currentState == 'e':                
                    D = float('inf')                    
                    currentState = 's'                    
                elif currentState == 'd':                
                    currentState = 's'                    
                elif currentState == 'f':                
                    C = float('-inf')                    
                    D = float('inf')                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
                elif currentState == 's':                
                    currentState = 's'                    
    return max(R,C)    

# MAX MIN INFLEXION
def max_min_inflexion(data):
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
                    D = min(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = float('inf')                    
                    R = max(R_temp,min(D_temp,data[i-1]))                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 't'                    
                elif currentState == 'r':                
                    D = float('inf')                    
                    R = max(R_temp,min(D_temp,data[i-1]))                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX MIN DECREASING_SEQUENCE
def max_min_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 't':                
                    C = float('-inf')                    
                    D = float('inf')                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    C = min(min(D_temp,data[i-1]),data[i])                    
                    D = float('inf')                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = min(C_temp,min(D_temp,data[i]))                    
                    D = float('inf')                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
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
                    D = min(D_temp,data[i-1])                    
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
                    C = min(D_temp,data[i-1])                    
                    D = float('inf')                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = min(C_temp,min(D_temp,data[i-1]))                    
                    D = float('inf')                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX MIN DIP_ON_INCREASING_SEQUENCE
def max_min_dip_on_increasing_sequence(data):
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
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'v'                    
                elif currentState == 't':                
                    currentState = 't'                    
                elif currentState == 'v':                
                    D = float('inf')                    
                    R = max(R_temp,min(D_temp,data[i-1]))                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = float('inf')                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'v':                
                    D = float('inf')                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = float('inf')                    
                    currentState = 's'                    
                elif currentState == 't':                
                    currentState = 's'                    
                elif currentState == 'v':                
                    D = float('inf')                    
                    currentState = 's'                    
    return max(R,C)    

# MAX MIN DECREASING_TERRACE
def max_min_decreasing_terrace(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = float('inf')                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = float('inf')                    
                    R = max(R_temp,min(D_temp,data[i-1]))                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX MIN GORGE
def max_min_gorge(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = min(D_temp,data[i-1])                    
                    D = float('inf')                    
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = float('inf')                    
                    currentState = 's'                    
                elif currentState == 't':                
                    C = min(C_temp,min(D_temp,data[i-1]))                    
                    D = float('inf')                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 'u':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = float('-inf')                    
                    D = float('inf')                    
                    R = max(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'u':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

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
                    R = max(R_temp,min(min(D_temp,data[i-1]),data[i]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return max(R,C)    

# MAX MIN PLAIN
def max_min_plain(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = float('inf')                    
                    R = max(R_temp,min(D_temp,data[i-1]))                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = float('inf')                    
                    R = max(R_temp,min(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = float('inf')                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX MIN STEADY
def max_min_steady(data):
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
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    D = float('inf')                    
                    R = max(R_temp,min(min(D_temp,data[i-1]),data[i]))                    
                    currentState = 's'                    
    return max(R,C)    

# MAX MIN SUMMIT
def max_min_summit(data):
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
                    C = min(D_temp,data[i-1])                    
                    D = float('inf')                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 'u':                
                    D = min(D_temp,data[i-1])                    
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
                    C = min(D_temp,data[i-1])                    
                    D = float('inf')                    
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = float('inf')                    
                    currentState = 's'                    
                elif currentState == 't':                
                    C = min(C_temp,min(D_temp,data[i-1]))                    
                    D = float('inf')                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'u':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX MIN DECREASING
def max_min_decreasing(data):
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
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    D = float('inf')                    
                    R = max(R_temp,min(min(D_temp,data[i-1]),data[i]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return max(R,C)    

# MAX MIN STEADY_SEQUENCE
def max_min_steady_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('-inf')                    
                    D = float('inf')                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('-inf')                    
                    D = float('inf')                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    C = min(min(D_temp,data[i-1]),data[i])                    
                    D = float('inf')                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = min(C_temp,min(D_temp,data[i]))                    
                    D = float('inf')                    
                    currentState = 'r'                    
    return max(R,C)    

# ----- MAX MAX -----
# MAX MAX BUMP_ON_DECREASING_SEQUENCE
def max_max_bump_on_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = float('-inf')                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'v':                
                    D = float('-inf')                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'v'                    
                elif currentState == 't':                
                    currentState = 't'                    
                elif currentState == 'v':                
                    D = float('-inf')                    
                    R = max(R_temp,max(D_temp,data[i-1]))                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = float('-inf')                    
                    currentState = 's'                    
                elif currentState == 't':                
                    currentState = 's'                    
                elif currentState == 'v':                
                    D = float('-inf')                    
                    currentState = 's'                    
    return max(R,C)    

# MAX MAX STRICTLY_DECREASING_SEQUENCE
def max_max_strictly_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('-inf')                    
                    D = float('-inf')                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    C = max(max(D_temp,data[i-1]),data[i])                    
                    D = float('-inf')                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = max(C_temp,max(D_temp,data[i]))                    
                    D = float('-inf')                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('-inf')                    
                    D = float('-inf')                    
                    R = max(R_temp,C_temp)                    
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
                    R = max(R_temp,max(D_temp,data[i-1]))                    
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
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX MAX PROPER_PLATEAU
def max_max_proper_plateau(data):
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
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = float('-inf')                    
                    R = max(R_temp,max(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX MAX INCREASING_SEQUENCE
def max_max_increasing_sequence(data):
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
                    C = max(max(D_temp,data[i-1]),data[i])                    
                    D = float('-inf')                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,data[i]))                    
                    D = float('-inf')                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    C = float('-inf')                    
                    D = float('-inf')                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX MAX PLATEAU
def max_max_plateau(data):
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
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = float('-inf')                    
                    R = max(R_temp,max(D_temp,data[i-1]))                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = float('-inf')                    
                    R = max(R_temp,max(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX MAX STRICTLY_INCREASING_SEQUENCE
def max_max_strictly_increasing_sequence(data):
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
                    C = max(max(D_temp,data[i-1]),data[i])                    
                    D = float('-inf')                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = max(C_temp,max(D_temp,data[i]))                    
                    D = float('-inf')                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('-inf')                    
                    D = float('-inf')                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('-inf')                    
                    D = float('-inf')                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
    return max(R,C)    

# MAX MAX VALLEY
def max_max_valley(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = max(D_temp,data[i-1])                    
                    D = float('-inf')                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,data[i-1]))                    
                    D = float('-inf')                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = float('-inf')                    
                    D = float('-inf')                    
                    R = max(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX MAX PROPER_PLAIN
def max_max_proper_plain(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = float('-inf')                    
                    R = max(R_temp,max(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = float('-inf')                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX MAX ZIGZAG
def max_max_zigzag(data):
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
                if currentState == 'a':                
                    currentState = 'a'                    
                elif currentState == 'c':                
                    C = float('-inf')                    
                    D = float('-inf')                    
                    R = max(R_temp,C_temp)                    
                    currentState = 'a'                    
                elif currentState == 'b':                
                    C = max(D_temp,data[i-1])                    
                    D = float('-inf')                    
                    currentState = 'c'                    
                elif currentState == 'e':                
                    D = float('-inf')                    
                    currentState = 'a'                    
                elif currentState == 'd':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'e'                    
                elif currentState == 'f':                
                    C = max(C_temp,max(D_temp,data[i-1]))                    
                    D = float('-inf')                    
                    currentState = 'c'                    
                elif currentState == 's':                
                    currentState = 'a'                    
            elif data[i] < data[i-1]:            
                if currentState == 'a':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'b'                    
                elif currentState == 'c':                
                    C = max(C_temp,max(D_temp,data[i-1]))                    
                    D = float('-inf')                    
                    currentState = 'f'                    
                elif currentState == 'b':                
                    currentState = 'd'                    
                elif currentState == 'e':                
                    C = max(D_temp,data[i-1])                    
                    D = float('-inf')                    
                    currentState = 'f'                    
                elif currentState == 'd':                
                    currentState = 'd'                    
                elif currentState == 'f':                
                    C = float('-inf')                    
                    D = float('-inf')                    
                    R = max(R_temp,C_temp)                    
                    currentState = 'd'                    
                elif currentState == 's':                
                    currentState = 'd'                    
            elif data[i] == data[i-1]:            
                if currentState == 'a':                
                    currentState = 's'                    
                elif currentState == 'c':                
                    C = float('-inf')                    
                    D = float('-inf')                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
                elif currentState == 'b':                
                    D = float('-inf')                    
                    currentState = 's'                    
                elif currentState == 'e':                
                    D = float('-inf')                    
                    currentState = 's'                    
                elif currentState == 'd':                
                    currentState = 's'                    
                elif currentState == 'f':                
                    C = float('-inf')                    
                    D = float('-inf')                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
                elif currentState == 's':                
                    currentState = 's'                    
    return max(R,C)    

# MAX MAX INFLEXION
def max_max_inflexion(data):
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
                    D = max(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = float('-inf')                    
                    R = max(R_temp,max(D_temp,data[i-1]))                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 't'                    
                elif currentState == 'r':                
                    D = float('-inf')                    
                    R = max(R_temp,max(D_temp,data[i-1]))                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX MAX DECREASING_SEQUENCE
def max_max_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 't':                
                    C = float('-inf')                    
                    D = float('-inf')                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    C = max(max(D_temp,data[i-1]),data[i])                    
                    D = float('-inf')                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,data[i]))                    
                    D = float('-inf')                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
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
                    D = max(D_temp,data[i-1])                    
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
                    C = max(D_temp,data[i-1])                    
                    D = float('-inf')                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,data[i-1]))                    
                    D = float('-inf')                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX MAX DIP_ON_INCREASING_SEQUENCE
def max_max_dip_on_increasing_sequence(data):
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
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'v'                    
                elif currentState == 't':                
                    currentState = 't'                    
                elif currentState == 'v':                
                    D = float('-inf')                    
                    R = max(R_temp,max(D_temp,data[i-1]))                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = float('-inf')                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'v':                
                    D = float('-inf')                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = float('-inf')                    
                    currentState = 's'                    
                elif currentState == 't':                
                    currentState = 's'                    
                elif currentState == 'v':                
                    D = float('-inf')                    
                    currentState = 's'                    
    return max(R,C)    

# MAX MAX DECREASING_TERRACE
def max_max_decreasing_terrace(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = float('-inf')                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = float('-inf')                    
                    R = max(R_temp,max(D_temp,data[i-1]))                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX MAX GORGE
def max_max_gorge(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = max(D_temp,data[i-1])                    
                    D = float('-inf')                    
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = float('-inf')                    
                    currentState = 's'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,data[i-1]))                    
                    D = float('-inf')                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 'u':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = float('-inf')                    
                    D = float('-inf')                    
                    R = max(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'u':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

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
                    R = max(R_temp,max(max(D_temp,data[i-1]),data[i]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return max(R,C)    

# MAX MAX PLAIN
def max_max_plain(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = float('-inf')                    
                    R = max(R_temp,max(D_temp,data[i-1]))                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = float('-inf')                    
                    R = max(R_temp,max(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = float('-inf')                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX MAX STEADY
def max_max_steady(data):
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
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    D = float('-inf')                    
                    R = max(R_temp,max(max(D_temp,data[i-1]),data[i]))                    
                    currentState = 's'                    
    return max(R,C)    

# MAX MAX SUMMIT
def max_max_summit(data):
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
                    C = max(D_temp,data[i-1])                    
                    D = float('-inf')                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 'u':                
                    D = max(D_temp,data[i-1])                    
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
                    C = max(D_temp,data[i-1])                    
                    D = float('-inf')                    
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = float('-inf')                    
                    currentState = 's'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,data[i-1]))                    
                    D = float('-inf')                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'u':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX MAX DECREASING
def max_max_decreasing(data):
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
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    D = float('-inf')                    
                    R = max(R_temp,max(max(D_temp,data[i-1]),data[i]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return max(R,C)    

# MAX MAX STEADY_SEQUENCE
def max_max_steady_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('-inf')                    
                    D = float('-inf')                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('-inf')                    
                    D = float('-inf')                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    C = max(max(D_temp,data[i-1]),data[i])                    
                    D = float('-inf')                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = max(C_temp,max(D_temp,data[i]))                    
                    D = float('-inf')                    
                    currentState = 'r'                    
    return max(R,C)    

# ----- MAX SURFACE -----
# MAX SURFACE BUMP_ON_DECREASING_SEQUENCE
def max_surface_bump_on_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'v':                
                    D = 0                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'v'                    
                elif currentState == 't':                
                    currentState = 't'                    
                elif currentState == 'v':                
                    D = 0                    
                    R = max(R_temp,operator.add(D_temp,data[i-1]))                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    currentState = 's'                    
                elif currentState == 'v':                
                    D = 0                    
                    currentState = 's'                    
    return max(R,C)    

# MAX SURFACE STRICTLY_DECREASING_SEQUENCE
def max_surface_strictly_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('-inf')                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    C = operator.add(operator.add(D_temp,data[i-1]),data[i])                    
                    D = 0                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = operator.add(C_temp,operator.add(D_temp,data[i]))                    
                    D = 0                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('-inf')                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
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
                    R = max(R_temp,operator.add(D_temp,data[i-1]))                    
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
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX SURFACE PROPER_PLATEAU
def max_surface_proper_plateau(data):
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
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    R = max(R_temp,operator.add(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX SURFACE INCREASING_SEQUENCE
def max_surface_increasing_sequence(data):
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
                    C = operator.add(operator.add(D_temp,data[i-1]),data[i])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,data[i]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    C = float('-inf')                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX SURFACE PLATEAU
def max_surface_plateau(data):
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
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = 0                    
                    R = max(R_temp,operator.add(D_temp,data[i-1]))                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    R = max(R_temp,operator.add(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX SURFACE STRICTLY_INCREASING_SEQUENCE
def max_surface_strictly_increasing_sequence(data):
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
                    C = operator.add(operator.add(D_temp,data[i-1]),data[i])                    
                    D = 0                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = operator.add(C_temp,operator.add(D_temp,data[i]))                    
                    D = 0                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('-inf')                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('-inf')                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
    return max(R,C)    

# MAX SURFACE VALLEY
def max_surface_valley(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = operator.add(D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,data[i-1]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = float('-inf')                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX SURFACE PROPER_PLAIN
def max_surface_proper_plain(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    R = max(R_temp,operator.add(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX SURFACE ZIGZAG
def max_surface_zigzag(data):
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
                if currentState == 'a':                
                    currentState = 'a'                    
                elif currentState == 'c':                
                    C = float('-inf')                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 'a'                    
                elif currentState == 'b':                
                    C = operator.add(D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 'c'                    
                elif currentState == 'e':                
                    D = 0                    
                    currentState = 'a'                    
                elif currentState == 'd':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'e'                    
                elif currentState == 'f':                
                    C = operator.add(C_temp,operator.add(D_temp,data[i-1]))                    
                    D = 0                    
                    currentState = 'c'                    
                elif currentState == 's':                
                    currentState = 'a'                    
            elif data[i] < data[i-1]:            
                if currentState == 'a':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'b'                    
                elif currentState == 'c':                
                    C = operator.add(C_temp,operator.add(D_temp,data[i-1]))                    
                    D = 0                    
                    currentState = 'f'                    
                elif currentState == 'b':                
                    currentState = 'd'                    
                elif currentState == 'e':                
                    C = operator.add(D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 'f'                    
                elif currentState == 'd':                
                    currentState = 'd'                    
                elif currentState == 'f':                
                    C = float('-inf')                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 'd'                    
                elif currentState == 's':                
                    currentState = 'd'                    
            elif data[i] == data[i-1]:            
                if currentState == 'a':                
                    currentState = 's'                    
                elif currentState == 'c':                
                    C = float('-inf')                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
                elif currentState == 'b':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 'e':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 'd':                
                    currentState = 's'                    
                elif currentState == 'f':                
                    C = float('-inf')                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
                elif currentState == 's':                
                    currentState = 's'                    
    return max(R,C)    

# MAX SURFACE INFLEXION
def max_surface_inflexion(data):
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
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    R = max(R_temp,operator.add(D_temp,data[i-1]))                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 't'                    
                elif currentState == 'r':                
                    D = 0                    
                    R = max(R_temp,operator.add(D_temp,data[i-1]))                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX SURFACE DECREASING_SEQUENCE
def max_surface_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 't':                
                    C = float('-inf')                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    C = operator.add(operator.add(D_temp,data[i-1]),data[i])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,data[i]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
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
                    D = operator.add(D_temp,data[i-1])                    
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
                    C = operator.add(D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,data[i-1]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX SURFACE DIP_ON_INCREASING_SEQUENCE
def max_surface_dip_on_increasing_sequence(data):
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
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'v'                    
                elif currentState == 't':                
                    currentState = 't'                    
                elif currentState == 'v':                
                    D = 0                    
                    R = max(R_temp,operator.add(D_temp,data[i-1]))                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'v':                
                    D = 0                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    currentState = 's'                    
                elif currentState == 'v':                
                    D = 0                    
                    currentState = 's'                    
    return max(R,C)    

# MAX SURFACE DECREASING_TERRACE
def max_surface_decreasing_terrace(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    R = max(R_temp,operator.add(D_temp,data[i-1]))                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX SURFACE GORGE
def max_surface_gorge(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = operator.add(D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,data[i-1]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 'u':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = float('-inf')                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'u':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

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
                    R = max(R_temp,operator.add(operator.add(D_temp,data[i-1]),data[i]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return max(R,C)    

# MAX SURFACE PLAIN
def max_surface_plain(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = 0                    
                    R = max(R_temp,operator.add(D_temp,data[i-1]))                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    R = max(R_temp,operator.add(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX SURFACE STEADY
def max_surface_steady(data):
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
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    D = 0                    
                    R = max(R_temp,operator.add(operator.add(D_temp,data[i-1]),data[i]))                    
                    currentState = 's'                    
    return max(R,C)    

# MAX SURFACE SUMMIT
def max_surface_summit(data):
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
                    C = operator.add(D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 'u':                
                    D = operator.add(D_temp,data[i-1])                    
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
                    C = operator.add(D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,data[i-1]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'u':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX SURFACE DECREASING
def max_surface_decreasing(data):
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
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    D = 0                    
                    R = max(R_temp,operator.add(operator.add(D_temp,data[i-1]),data[i]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return max(R,C)    

# MAX SURFACE STEADY_SEQUENCE
def max_surface_steady_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('-inf')                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('-inf')                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    C = operator.add(operator.add(D_temp,data[i-1]),data[i])                    
                    D = 0                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = operator.add(C_temp,operator.add(D_temp,data[i]))                    
                    D = 0                    
                    currentState = 'r'                    
    return max(R,C)    

# ----- MAX ONE -----
# MAX ONE BUMP_ON_DECREASING_SEQUENCE
def max_one_bump_on_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 1                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = max(D_temp,0)                    
                    currentState = 'u'                    
                elif currentState == 'v':                
                    D = 1                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = max(D_temp,0)                    
                    currentState = 'v'                    
                elif currentState == 't':                
                    currentState = 't'                    
                elif currentState == 'v':                
                    D = 1                    
                    R = max(R_temp,max(D_temp,0))                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 1                    
                    currentState = 's'                    
                elif currentState == 't':                
                    currentState = 's'                    
                elif currentState == 'v':                
                    D = 1                    
                    currentState = 's'                    
    return max(R,C)    

# MAX ONE STRICTLY_DECREASING_SEQUENCE
def max_one_strictly_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 1                    
                    D = 1                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    C = max(max(D_temp,0),data[i])                    
                    D = 1                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = max(C_temp,max(D_temp,data[i]))                    
                    D = 1                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 1                    
                    D = 1                    
                    R = max(R_temp,C_temp)                    
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

# MAX ONE PROPER_PLATEAU
def max_one_proper_plateau(data):
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
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 1                    
                    R = max(R_temp,max(D_temp,0))                    
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

# MAX ONE INCREASING_SEQUENCE
def max_one_increasing_sequence(data):
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
                    C = max(max(D_temp,0),data[i])                    
                    D = 1                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,data[i]))                    
                    D = 1                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    C = 1                    
                    D = 1                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX ONE PLATEAU
def max_one_plateau(data):
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
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = 1                    
                    R = max(R_temp,max(D_temp,0))                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 1                    
                    R = max(R_temp,max(D_temp,0))                    
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

# MAX ONE STRICTLY_INCREASING_SEQUENCE
def max_one_strictly_increasing_sequence(data):
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
                    C = max(max(D_temp,0),data[i])                    
                    D = 1                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = max(C_temp,max(D_temp,data[i]))                    
                    D = 1                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 1                    
                    D = 1                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 1                    
                    D = 1                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
    return max(R,C)    

# MAX ONE VALLEY
def max_one_valley(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = max(D_temp,0)                    
                    D = 1                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,0))                    
                    D = 1                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
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

# MAX ONE PROPER_PLAIN
def max_one_proper_plain(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 1                    
                    R = max(R_temp,max(D_temp,0))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 1                    
                    currentState = 'r'                    
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

# MAX ONE ZIGZAG
def max_one_zigzag(data):
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
                if currentState == 'a':                
                    currentState = 'a'                    
                elif currentState == 'c':                
                    C = 1                    
                    D = 1                    
                    R = max(R_temp,C_temp)                    
                    currentState = 'a'                    
                elif currentState == 'b':                
                    C = max(D_temp,0)                    
                    D = 1                    
                    currentState = 'c'                    
                elif currentState == 'e':                
                    D = 1                    
                    currentState = 'a'                    
                elif currentState == 'd':                
                    D = max(D_temp,0)                    
                    currentState = 'e'                    
                elif currentState == 'f':                
                    C = max(C_temp,max(D_temp,0))                    
                    D = 1                    
                    currentState = 'c'                    
                elif currentState == 's':                
                    currentState = 'a'                    
            elif data[i] < data[i-1]:            
                if currentState == 'a':                
                    D = max(D_temp,0)                    
                    currentState = 'b'                    
                elif currentState == 'c':                
                    C = max(C_temp,max(D_temp,0))                    
                    D = 1                    
                    currentState = 'f'                    
                elif currentState == 'b':                
                    currentState = 'd'                    
                elif currentState == 'e':                
                    C = max(D_temp,0)                    
                    D = 1                    
                    currentState = 'f'                    
                elif currentState == 'd':                
                    currentState = 'd'                    
                elif currentState == 'f':                
                    C = 1                    
                    D = 1                    
                    R = max(R_temp,C_temp)                    
                    currentState = 'd'                    
                elif currentState == 's':                
                    currentState = 'd'                    
            elif data[i] == data[i-1]:            
                if currentState == 'a':                
                    currentState = 's'                    
                elif currentState == 'c':                
                    C = 1                    
                    D = 1                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
                elif currentState == 'b':                
                    D = 1                    
                    currentState = 's'                    
                elif currentState == 'e':                
                    D = 1                    
                    currentState = 's'                    
                elif currentState == 'd':                
                    currentState = 's'                    
                elif currentState == 'f':                
                    C = 1                    
                    D = 1                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
                elif currentState == 's':                
                    currentState = 's'                    
    return max(R,C)    

# MAX ONE INFLEXION
def max_one_inflexion(data):
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
                    D = 1                    
                    R = max(R_temp,max(D_temp,0))                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 't'                    
                elif currentState == 'r':                
                    D = 1                    
                    R = max(R_temp,max(D_temp,0))                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = max(D_temp,0)                    
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

# MAX ONE DECREASING_SEQUENCE
def max_one_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 't':                
                    C = 1                    
                    D = 1                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    C = max(max(D_temp,0),data[i])                    
                    D = 1                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,data[i]))                    
                    D = 1                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i])                    
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

# MAX ONE DIP_ON_INCREASING_SEQUENCE
def max_one_dip_on_increasing_sequence(data):
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
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = max(D_temp,0)                    
                    currentState = 'v'                    
                elif currentState == 't':                
                    currentState = 't'                    
                elif currentState == 'v':                
                    D = 1                    
                    R = max(R_temp,max(D_temp,0))                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 1                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = max(D_temp,0)                    
                    currentState = 'u'                    
                elif currentState == 'v':                
                    D = 1                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 1                    
                    currentState = 's'                    
                elif currentState == 't':                
                    currentState = 's'                    
                elif currentState == 'v':                
                    D = 1                    
                    currentState = 's'                    
    return max(R,C)    

# MAX ONE DECREASING_TERRACE
def max_one_decreasing_terrace(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 1                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 1                    
                    R = max(R_temp,max(D_temp,0))                    
                    currentState = 'r'                    
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

# MAX ONE GORGE
def max_one_gorge(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = max(D_temp,0)                    
                    D = 1                    
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = 1                    
                    currentState = 's'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,0))                    
                    D = 1                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = max(D_temp,0)                    
                    currentState = 'r'                    
                elif currentState == 'u':                
                    D = max(D_temp,0)                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 1                    
                    D = 1                    
                    R = max(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,0)                    
                    currentState = 'u'                    
                elif currentState == 'u':                
                    D = max(D_temp,0)                    
                    currentState = 'u'                    
                elif currentState == 't':                
                    D = max(D_temp,0)                    
                    currentState = 't'                    
    return max(R,C)    

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
                    R = max(R_temp,max(max(D_temp,0),data[i]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return max(R,C)    

# MAX ONE PLAIN
def max_one_plain(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = 1                    
                    R = max(R_temp,max(D_temp,0))                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 1                    
                    R = max(R_temp,max(D_temp,0))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 1                    
                    currentState = 'r'                    
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

# MAX ONE STEADY
def max_one_steady(data):
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
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    D = 1                    
                    R = max(R_temp,max(max(D_temp,0),data[i]))                    
                    currentState = 's'                    
    return max(R,C)    

# MAX ONE SUMMIT
def max_one_summit(data):
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
                    C = max(D_temp,0)                    
                    D = 1                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = max(D_temp,0)                    
                    currentState = 'r'                    
                elif currentState == 'u':                
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
                elif currentState == 'u':                
                    D = 1                    
                    currentState = 's'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,0))                    
                    D = 1                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,0)                    
                    currentState = 'u'                    
                elif currentState == 'u':                
                    D = max(D_temp,0)                    
                    currentState = 'u'                    
                elif currentState == 't':                
                    D = max(D_temp,0)                    
                    currentState = 't'                    
    return max(R,C)    

# MAX ONE DECREASING
def max_one_decreasing(data):
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
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    D = 1                    
                    R = max(R_temp,max(max(D_temp,0),data[i]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return max(R,C)    

# MAX ONE STEADY_SEQUENCE
def max_one_steady_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 1                    
                    D = 1                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 1                    
                    D = 1                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    C = max(max(D_temp,0),data[i])                    
                    D = 1                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = max(C_temp,max(D_temp,data[i]))                    
                    D = 1                    
                    currentState = 'r'                    
    return max(R,C)    

# ----- MAX WIDTH -----
# MAX WIDTH BUMP_ON_DECREASING_SEQUENCE
def max_width_bump_on_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'u'                    
                elif currentState == 'v':                
                    D = 0                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'v'                    
                elif currentState == 't':                
                    currentState = 't'                    
                elif currentState == 'v':                
                    D = 0                    
                    R = max(R_temp,operator.add(D_temp,1))                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    currentState = 's'                    
                elif currentState == 'v':                
                    D = 0                    
                    currentState = 's'                    
    return max(R,C)    

# MAX WIDTH STRICTLY_DECREASING_SEQUENCE
def max_width_strictly_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    C = operator.add(operator.add(D_temp,1),1)                    
                    D = 0                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = operator.add(C_temp,operator.add(D_temp,1))                    
                    D = 0                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
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

# MAX WIDTH PROPER_PLATEAU
def max_width_proper_plateau(data):
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
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    R = max(R_temp,operator.add(D_temp,1))                    
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

# MAX WIDTH INCREASING_SEQUENCE
def max_width_increasing_sequence(data):
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
                    C = operator.add(operator.add(D_temp,1),1)                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,1))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    C = 0                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,1)                    
                    currentState = 't'                    
    return max(R,C)    

# MAX WIDTH PLATEAU
def max_width_plateau(data):
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
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = 0                    
                    R = max(R_temp,operator.add(D_temp,1))                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    R = max(R_temp,operator.add(D_temp,1))                    
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

# MAX WIDTH STRICTLY_INCREASING_SEQUENCE
def max_width_strictly_increasing_sequence(data):
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
                    C = operator.add(operator.add(D_temp,1),1)                    
                    D = 0                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = operator.add(C_temp,operator.add(D_temp,1))                    
                    D = 0                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
    return max(R,C)    

# MAX WIDTH VALLEY
def max_width_valley(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = operator.add(D_temp,1)                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,1))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
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

# MAX WIDTH PROPER_PLAIN
def max_width_proper_plain(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    R = max(R_temp,operator.add(D_temp,1))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    currentState = 'r'                    
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

# MAX WIDTH ZIGZAG
def max_width_zigzag(data):
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
                if currentState == 'a':                
                    currentState = 'a'                    
                elif currentState == 'c':                
                    C = 0                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 'a'                    
                elif currentState == 'b':                
                    C = operator.add(D_temp,1)                    
                    D = 0                    
                    currentState = 'c'                    
                elif currentState == 'e':                
                    D = 0                    
                    currentState = 'a'                    
                elif currentState == 'd':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'e'                    
                elif currentState == 'f':                
                    C = operator.add(C_temp,operator.add(D_temp,1))                    
                    D = 0                    
                    currentState = 'c'                    
                elif currentState == 's':                
                    currentState = 'a'                    
            elif data[i] < data[i-1]:            
                if currentState == 'a':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'b'                    
                elif currentState == 'c':                
                    C = operator.add(C_temp,operator.add(D_temp,1))                    
                    D = 0                    
                    currentState = 'f'                    
                elif currentState == 'b':                
                    currentState = 'd'                    
                elif currentState == 'e':                
                    C = operator.add(D_temp,1)                    
                    D = 0                    
                    currentState = 'f'                    
                elif currentState == 'd':                
                    currentState = 'd'                    
                elif currentState == 'f':                
                    C = 0                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 'd'                    
                elif currentState == 's':                
                    currentState = 'd'                    
            elif data[i] == data[i-1]:            
                if currentState == 'a':                
                    currentState = 's'                    
                elif currentState == 'c':                
                    C = 0                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
                elif currentState == 'b':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 'e':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 'd':                
                    currentState = 's'                    
                elif currentState == 'f':                
                    C = 0                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
                elif currentState == 's':                
                    currentState = 's'                    
    return max(R,C)    

# MAX WIDTH INFLEXION
def max_width_inflexion(data):
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
                    D = 0                    
                    R = max(R_temp,operator.add(D_temp,1))                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 't'                    
                elif currentState == 'r':                
                    D = 0                    
                    R = max(R_temp,operator.add(D_temp,1))                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,1)                    
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

# MAX WIDTH DECREASING_SEQUENCE
def max_width_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 't':                
                    C = 0                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    C = operator.add(operator.add(D_temp,1),1)                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,1))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
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

# MAX WIDTH DIP_ON_INCREASING_SEQUENCE
def max_width_dip_on_increasing_sequence(data):
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
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'v'                    
                elif currentState == 't':                
                    currentState = 't'                    
                elif currentState == 'v':                
                    D = 0                    
                    R = max(R_temp,operator.add(D_temp,1))                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'u'                    
                elif currentState == 'v':                
                    D = 0                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    currentState = 's'                    
                elif currentState == 'v':                
                    D = 0                    
                    currentState = 's'                    
    return max(R,C)    

# MAX WIDTH DECREASING_TERRACE
def max_width_decreasing_terrace(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    R = max(R_temp,operator.add(D_temp,1))                    
                    currentState = 'r'                    
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

# MAX WIDTH GORGE
def max_width_gorge(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = operator.add(D_temp,1)                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,1))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'r'                    
                elif currentState == 'u':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 0                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'u'                    
                elif currentState == 'u':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'u'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,1)                    
                    currentState = 't'                    
    return max(R,C)    

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
                    R = max(R_temp,operator.add(operator.add(D_temp,1),1))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return max(R,C)    

# MAX WIDTH PLAIN
def max_width_plain(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = 0                    
                    R = max(R_temp,operator.add(D_temp,1))                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    R = max(R_temp,operator.add(D_temp,1))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    currentState = 'r'                    
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

# MAX WIDTH STEADY
def max_width_steady(data):
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
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    D = 0                    
                    R = max(R_temp,operator.add(operator.add(D_temp,1),1))                    
                    currentState = 's'                    
    return max(R,C)    

# MAX WIDTH SUMMIT
def max_width_summit(data):
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
                    C = operator.add(D_temp,1)                    
                    D = 0                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'r'                    
                elif currentState == 'u':                
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
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,1))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'u'                    
                elif currentState == 'u':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'u'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,1)                    
                    currentState = 't'                    
    return max(R,C)    

# MAX WIDTH DECREASING
def max_width_decreasing(data):
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
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    D = 0                    
                    R = max(R_temp,operator.add(operator.add(D_temp,1),1))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return max(R,C)    

# MAX WIDTH STEADY_SEQUENCE
def max_width_steady_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    C = operator.add(operator.add(D_temp,1),1)                    
                    D = 0                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = operator.add(C_temp,operator.add(D_temp,1))                    
                    D = 0                    
                    currentState = 'r'                    
    return max(R,C)    

# ----- MAX RANGE -----
# MAX RANGE BUMP_ON_DECREASING_SEQUENCE
def max_range_bump_on_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'v':                
                    D = 0                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'v'                    
                elif currentState == 't':                
                    currentState = 't'                    
                elif currentState == 'v':                
                    D = 0                    
                    R = max(R_temp,(D_temp,data[i-1]))                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    currentState = 's'                    
                elif currentState == 'v':                
                    D = 0                    
                    currentState = 's'                    
    return max(R,C)    

# MAX RANGE STRICTLY_DECREASING_SEQUENCE
def max_range_strictly_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    C = ((D_temp,data[i-1]),data[i])                    
                    D = 0                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = (C_temp,(D_temp,data[i]))                    
                    D = 0                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
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
                    R = max(R_temp,(D_temp,data[i-1]))                    
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
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX RANGE PROPER_PLATEAU
def max_range_proper_plateau(data):
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
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    R = max(R_temp,(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX RANGE INCREASING_SEQUENCE
def max_range_increasing_sequence(data):
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
                    C = ((D_temp,data[i-1]),data[i])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = (C_temp,(D_temp,data[i]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    C = 0                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = (D_temp,data[i])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX RANGE PLATEAU
def max_range_plateau(data):
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
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = 0                    
                    R = max(R_temp,(D_temp,data[i-1]))                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    R = max(R_temp,(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX RANGE STRICTLY_INCREASING_SEQUENCE
def max_range_strictly_increasing_sequence(data):
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
                    C = ((D_temp,data[i-1]),data[i])                    
                    D = 0                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = (C_temp,(D_temp,data[i]))                    
                    D = 0                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
    return max(R,C)    

# MAX RANGE VALLEY
def max_range_valley(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = (D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = (C_temp,(D_temp,data[i-1]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 0                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX RANGE PROPER_PLAIN
def max_range_proper_plain(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    R = max(R_temp,(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX RANGE ZIGZAG
def max_range_zigzag(data):
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
                if currentState == 'a':                
                    currentState = 'a'                    
                elif currentState == 'c':                
                    C = 0                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 'a'                    
                elif currentState == 'b':                
                    C = (D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 'c'                    
                elif currentState == 'e':                
                    D = 0                    
                    currentState = 'a'                    
                elif currentState == 'd':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'e'                    
                elif currentState == 'f':                
                    C = (C_temp,(D_temp,data[i-1]))                    
                    D = 0                    
                    currentState = 'c'                    
                elif currentState == 's':                
                    currentState = 'a'                    
            elif data[i] < data[i-1]:            
                if currentState == 'a':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'b'                    
                elif currentState == 'c':                
                    C = (C_temp,(D_temp,data[i-1]))                    
                    D = 0                    
                    currentState = 'f'                    
                elif currentState == 'b':                
                    currentState = 'd'                    
                elif currentState == 'e':                
                    C = (D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 'f'                    
                elif currentState == 'd':                
                    currentState = 'd'                    
                elif currentState == 'f':                
                    C = 0                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 'd'                    
                elif currentState == 's':                
                    currentState = 'd'                    
            elif data[i] == data[i-1]:            
                if currentState == 'a':                
                    currentState = 's'                    
                elif currentState == 'c':                
                    C = 0                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
                elif currentState == 'b':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 'e':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 'd':                
                    currentState = 's'                    
                elif currentState == 'f':                
                    C = 0                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
                elif currentState == 's':                
                    currentState = 's'                    
    return max(R,C)    

# MAX RANGE INFLEXION
def max_range_inflexion(data):
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
                    D = (D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    R = max(R_temp,(D_temp,data[i-1]))                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 't'                    
                elif currentState == 'r':                
                    D = 0                    
                    R = max(R_temp,(D_temp,data[i-1]))                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX RANGE DECREASING_SEQUENCE
def max_range_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 't':                
                    C = 0                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    C = ((D_temp,data[i-1]),data[i])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = (C_temp,(D_temp,data[i]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
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
                    D = (D_temp,data[i-1])                    
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
                    C = (D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = (C_temp,(D_temp,data[i-1]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX RANGE DIP_ON_INCREASING_SEQUENCE
def max_range_dip_on_increasing_sequence(data):
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
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'v'                    
                elif currentState == 't':                
                    currentState = 't'                    
                elif currentState == 'v':                
                    D = 0                    
                    R = max(R_temp,(D_temp,data[i-1]))                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'v':                
                    D = 0                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    currentState = 's'                    
                elif currentState == 'v':                
                    D = 0                    
                    currentState = 's'                    
    return max(R,C)    

# MAX RANGE DECREASING_TERRACE
def max_range_decreasing_terrace(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    R = max(R_temp,(D_temp,data[i-1]))                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX RANGE GORGE
def max_range_gorge(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = (D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    C = (C_temp,(D_temp,data[i-1]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 'u':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 0                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'u':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

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
                    R = max(R_temp,((D_temp,data[i-1]),data[i]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return max(R,C)    

# MAX RANGE PLAIN
def max_range_plain(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = 0                    
                    R = max(R_temp,(D_temp,data[i-1]))                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    R = max(R_temp,(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX RANGE STEADY
def max_range_steady(data):
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
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    D = 0                    
                    R = max(R_temp,((D_temp,data[i-1]),data[i]))                    
                    currentState = 's'                    
    return max(R,C)    

# MAX RANGE SUMMIT
def max_range_summit(data):
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
                    C = (D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 'u':                
                    D = (D_temp,data[i-1])                    
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
                    C = (D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    C = (C_temp,(D_temp,data[i-1]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'u':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
    return max(R,C)    

# MAX RANGE DECREASING
def max_range_decreasing(data):
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
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    D = 0                    
                    R = max(R_temp,((D_temp,data[i-1]),data[i]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return max(R,C)    

# MAX RANGE STEADY_SEQUENCE
def max_range_steady_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = 0                    
                    R = max(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    C = ((D_temp,data[i-1]),data[i])                    
                    D = 0                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = (C_temp,(D_temp,data[i]))                    
                    D = 0                    
                    currentState = 'r'                    
    return max(R,C)    

# ----- SUM -----
# ----- SUM MIN -----
# SUM MIN BUMP_ON_DECREASING_SEQUENCE
def sum_min_bump_on_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = float('inf')                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'v':                
                    D = float('inf')                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'v'                    
                elif currentState == 't':                
                    currentState = 't'                    
                elif currentState == 'v':                
                    D = float('inf')                    
                    R = operator.add(R_temp,min(D_temp,data[i-1]))                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = float('inf')                    
                    currentState = 's'                    
                elif currentState == 't':                
                    currentState = 's'                    
                elif currentState == 'v':                
                    D = float('inf')                    
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM MIN STRICTLY_DECREASING_SEQUENCE
def sum_min_strictly_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = float('inf')                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    C = min(min(D_temp,data[i-1]),data[i])                    
                    D = float('inf')                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = min(C_temp,min(D_temp,data[i]))                    
                    D = float('inf')                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = float('inf')                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
    return operator.add(R,C)    

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
                    R = operator.add(R_temp,min(D_temp,data[i-1]))                    
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
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM MIN PROPER_PLATEAU
def sum_min_proper_plateau(data):
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
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = float('inf')                    
                    R = operator.add(R_temp,min(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM MIN INCREASING_SEQUENCE
def sum_min_increasing_sequence(data):
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
                    C = min(min(D_temp,data[i-1]),data[i])                    
                    D = float('inf')                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = min(C_temp,min(D_temp,data[i]))                    
                    D = float('inf')                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    C = 0                    
                    D = float('inf')                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM MIN PLATEAU
def sum_min_plateau(data):
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
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = float('inf')                    
                    R = operator.add(R_temp,min(D_temp,data[i-1]))                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = float('inf')                    
                    R = operator.add(R_temp,min(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM MIN STRICTLY_INCREASING_SEQUENCE
def sum_min_strictly_increasing_sequence(data):
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
                    C = min(min(D_temp,data[i-1]),data[i])                    
                    D = float('inf')                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = min(C_temp,min(D_temp,data[i]))                    
                    D = float('inf')                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = float('inf')                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = float('inf')                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM MIN VALLEY
def sum_min_valley(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = min(D_temp,data[i-1])                    
                    D = float('inf')                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = min(C_temp,min(D_temp,data[i-1]))                    
                    D = float('inf')                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 0                    
                    D = float('inf')                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM MIN PROPER_PLAIN
def sum_min_proper_plain(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = float('inf')                    
                    R = operator.add(R_temp,min(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = float('inf')                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM MIN ZIGZAG
def sum_min_zigzag(data):
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
                if currentState == 'a':                
                    currentState = 'a'                    
                elif currentState == 'c':                
                    C = 0                    
                    D = float('inf')                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 'a'                    
                elif currentState == 'b':                
                    C = min(D_temp,data[i-1])                    
                    D = float('inf')                    
                    currentState = 'c'                    
                elif currentState == 'e':                
                    D = float('inf')                    
                    currentState = 'a'                    
                elif currentState == 'd':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'e'                    
                elif currentState == 'f':                
                    C = min(C_temp,min(D_temp,data[i-1]))                    
                    D = float('inf')                    
                    currentState = 'c'                    
                elif currentState == 's':                
                    currentState = 'a'                    
            elif data[i] < data[i-1]:            
                if currentState == 'a':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'b'                    
                elif currentState == 'c':                
                    C = min(C_temp,min(D_temp,data[i-1]))                    
                    D = float('inf')                    
                    currentState = 'f'                    
                elif currentState == 'b':                
                    currentState = 'd'                    
                elif currentState == 'e':                
                    C = min(D_temp,data[i-1])                    
                    D = float('inf')                    
                    currentState = 'f'                    
                elif currentState == 'd':                
                    currentState = 'd'                    
                elif currentState == 'f':                
                    C = 0                    
                    D = float('inf')                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 'd'                    
                elif currentState == 's':                
                    currentState = 'd'                    
            elif data[i] == data[i-1]:            
                if currentState == 'a':                
                    currentState = 's'                    
                elif currentState == 'c':                
                    C = 0                    
                    D = float('inf')                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
                elif currentState == 'b':                
                    D = float('inf')                    
                    currentState = 's'                    
                elif currentState == 'e':                
                    D = float('inf')                    
                    currentState = 's'                    
                elif currentState == 'd':                
                    currentState = 's'                    
                elif currentState == 'f':                
                    C = 0                    
                    D = float('inf')                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
                elif currentState == 's':                
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM MIN INFLEXION
def sum_min_inflexion(data):
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
                    D = min(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = float('inf')                    
                    R = operator.add(R_temp,min(D_temp,data[i-1]))                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 't'                    
                elif currentState == 'r':                
                    D = float('inf')                    
                    R = operator.add(R_temp,min(D_temp,data[i-1]))                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM MIN DECREASING_SEQUENCE
def sum_min_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 't':                
                    C = 0                    
                    D = float('inf')                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    C = min(min(D_temp,data[i-1]),data[i])                    
                    D = float('inf')                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = min(C_temp,min(D_temp,data[i]))                    
                    D = float('inf')                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i])                    
                    currentState = 't'                    
    return operator.add(R,C)    

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
                    D = min(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 0                    
                    D = float('inf')                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = min(D_temp,data[i-1])                    
                    D = float('inf')                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = min(C_temp,min(D_temp,data[i-1]))                    
                    D = float('inf')                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM MIN DIP_ON_INCREASING_SEQUENCE
def sum_min_dip_on_increasing_sequence(data):
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
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'v'                    
                elif currentState == 't':                
                    currentState = 't'                    
                elif currentState == 'v':                
                    D = float('inf')                    
                    R = operator.add(R_temp,min(D_temp,data[i-1]))                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = float('inf')                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'v':                
                    D = float('inf')                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = float('inf')                    
                    currentState = 's'                    
                elif currentState == 't':                
                    currentState = 's'                    
                elif currentState == 'v':                
                    D = float('inf')                    
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM MIN DECREASING_TERRACE
def sum_min_decreasing_terrace(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = float('inf')                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = float('inf')                    
                    R = operator.add(R_temp,min(D_temp,data[i-1]))                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM MIN GORGE
def sum_min_gorge(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = min(D_temp,data[i-1])                    
                    D = float('inf')                    
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = float('inf')                    
                    currentState = 's'                    
                elif currentState == 't':                
                    C = min(C_temp,min(D_temp,data[i-1]))                    
                    D = float('inf')                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 'u':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 0                    
                    D = float('inf')                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'u':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

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
                    R = operator.add(R_temp,min(min(D_temp,data[i-1]),data[i]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM MIN PLAIN
def sum_min_plain(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = float('inf')                    
                    R = operator.add(R_temp,min(D_temp,data[i-1]))                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = float('inf')                    
                    R = operator.add(R_temp,min(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = float('inf')                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM MIN STEADY
def sum_min_steady(data):
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
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    D = float('inf')                    
                    R = operator.add(R_temp,min(min(D_temp,data[i-1]),data[i]))                    
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM MIN SUMMIT
def sum_min_summit(data):
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
                    C = min(D_temp,data[i-1])                    
                    D = float('inf')                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 'u':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 0                    
                    D = float('inf')                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = min(D_temp,data[i-1])                    
                    D = float('inf')                    
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = float('inf')                    
                    currentState = 's'                    
                elif currentState == 't':                
                    C = min(C_temp,min(D_temp,data[i-1]))                    
                    D = float('inf')                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'u':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM MIN DECREASING
def sum_min_decreasing(data):
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
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    D = float('inf')                    
                    R = operator.add(R_temp,min(min(D_temp,data[i-1]),data[i]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM MIN STEADY_SEQUENCE
def sum_min_steady_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = float('inf')                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = float('inf')                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    C = min(min(D_temp,data[i-1]),data[i])                    
                    D = float('inf')                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = min(C_temp,min(D_temp,data[i]))                    
                    D = float('inf')                    
                    currentState = 'r'                    
    return operator.add(R,C)    

# ----- SUM MAX -----
# SUM MAX BUMP_ON_DECREASING_SEQUENCE
def sum_max_bump_on_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = float('-inf')                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'v':                
                    D = float('-inf')                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'v'                    
                elif currentState == 't':                
                    currentState = 't'                    
                elif currentState == 'v':                
                    D = float('-inf')                    
                    R = operator.add(R_temp,max(D_temp,data[i-1]))                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = float('-inf')                    
                    currentState = 's'                    
                elif currentState == 't':                
                    currentState = 's'                    
                elif currentState == 'v':                
                    D = float('-inf')                    
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM MAX STRICTLY_DECREASING_SEQUENCE
def sum_max_strictly_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = float('-inf')                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    C = max(max(D_temp,data[i-1]),data[i])                    
                    D = float('-inf')                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = max(C_temp,max(D_temp,data[i]))                    
                    D = float('-inf')                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = float('-inf')                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
    return operator.add(R,C)    

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
                    R = operator.add(R_temp,max(D_temp,data[i-1]))                    
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
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM MAX PROPER_PLATEAU
def sum_max_proper_plateau(data):
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
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = float('-inf')                    
                    R = operator.add(R_temp,max(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM MAX INCREASING_SEQUENCE
def sum_max_increasing_sequence(data):
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
                    C = max(max(D_temp,data[i-1]),data[i])                    
                    D = float('-inf')                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,data[i]))                    
                    D = float('-inf')                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    C = 0                    
                    D = float('-inf')                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM MAX PLATEAU
def sum_max_plateau(data):
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
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = float('-inf')                    
                    R = operator.add(R_temp,max(D_temp,data[i-1]))                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = float('-inf')                    
                    R = operator.add(R_temp,max(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM MAX STRICTLY_INCREASING_SEQUENCE
def sum_max_strictly_increasing_sequence(data):
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
                    C = max(max(D_temp,data[i-1]),data[i])                    
                    D = float('-inf')                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = max(C_temp,max(D_temp,data[i]))                    
                    D = float('-inf')                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = float('-inf')                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = float('-inf')                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM MAX VALLEY
def sum_max_valley(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = max(D_temp,data[i-1])                    
                    D = float('-inf')                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,data[i-1]))                    
                    D = float('-inf')                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 0                    
                    D = float('-inf')                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM MAX PROPER_PLAIN
def sum_max_proper_plain(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = float('-inf')                    
                    R = operator.add(R_temp,max(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = float('-inf')                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM MAX ZIGZAG
def sum_max_zigzag(data):
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
                if currentState == 'a':                
                    currentState = 'a'                    
                elif currentState == 'c':                
                    C = 0                    
                    D = float('-inf')                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 'a'                    
                elif currentState == 'b':                
                    C = max(D_temp,data[i-1])                    
                    D = float('-inf')                    
                    currentState = 'c'                    
                elif currentState == 'e':                
                    D = float('-inf')                    
                    currentState = 'a'                    
                elif currentState == 'd':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'e'                    
                elif currentState == 'f':                
                    C = max(C_temp,max(D_temp,data[i-1]))                    
                    D = float('-inf')                    
                    currentState = 'c'                    
                elif currentState == 's':                
                    currentState = 'a'                    
            elif data[i] < data[i-1]:            
                if currentState == 'a':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'b'                    
                elif currentState == 'c':                
                    C = max(C_temp,max(D_temp,data[i-1]))                    
                    D = float('-inf')                    
                    currentState = 'f'                    
                elif currentState == 'b':                
                    currentState = 'd'                    
                elif currentState == 'e':                
                    C = max(D_temp,data[i-1])                    
                    D = float('-inf')                    
                    currentState = 'f'                    
                elif currentState == 'd':                
                    currentState = 'd'                    
                elif currentState == 'f':                
                    C = 0                    
                    D = float('-inf')                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 'd'                    
                elif currentState == 's':                
                    currentState = 'd'                    
            elif data[i] == data[i-1]:            
                if currentState == 'a':                
                    currentState = 's'                    
                elif currentState == 'c':                
                    C = 0                    
                    D = float('-inf')                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
                elif currentState == 'b':                
                    D = float('-inf')                    
                    currentState = 's'                    
                elif currentState == 'e':                
                    D = float('-inf')                    
                    currentState = 's'                    
                elif currentState == 'd':                
                    currentState = 's'                    
                elif currentState == 'f':                
                    C = 0                    
                    D = float('-inf')                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
                elif currentState == 's':                
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM MAX INFLEXION
def sum_max_inflexion(data):
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
                    D = max(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = float('-inf')                    
                    R = operator.add(R_temp,max(D_temp,data[i-1]))                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 't'                    
                elif currentState == 'r':                
                    D = float('-inf')                    
                    R = operator.add(R_temp,max(D_temp,data[i-1]))                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM MAX DECREASING_SEQUENCE
def sum_max_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 't':                
                    C = 0                    
                    D = float('-inf')                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    C = max(max(D_temp,data[i-1]),data[i])                    
                    D = float('-inf')                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,data[i]))                    
                    D = float('-inf')                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i])                    
                    currentState = 't'                    
    return operator.add(R,C)    

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
                    D = max(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 0                    
                    D = float('-inf')                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = max(D_temp,data[i-1])                    
                    D = float('-inf')                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,data[i-1]))                    
                    D = float('-inf')                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM MAX DIP_ON_INCREASING_SEQUENCE
def sum_max_dip_on_increasing_sequence(data):
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
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'v'                    
                elif currentState == 't':                
                    currentState = 't'                    
                elif currentState == 'v':                
                    D = float('-inf')                    
                    R = operator.add(R_temp,max(D_temp,data[i-1]))                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = float('-inf')                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'v':                
                    D = float('-inf')                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = float('-inf')                    
                    currentState = 's'                    
                elif currentState == 't':                
                    currentState = 's'                    
                elif currentState == 'v':                
                    D = float('-inf')                    
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM MAX DECREASING_TERRACE
def sum_max_decreasing_terrace(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = float('-inf')                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = float('-inf')                    
                    R = operator.add(R_temp,max(D_temp,data[i-1]))                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM MAX GORGE
def sum_max_gorge(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = max(D_temp,data[i-1])                    
                    D = float('-inf')                    
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = float('-inf')                    
                    currentState = 's'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,data[i-1]))                    
                    D = float('-inf')                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 'u':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 0                    
                    D = float('-inf')                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'u':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

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
                    R = operator.add(R_temp,max(max(D_temp,data[i-1]),data[i]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM MAX PLAIN
def sum_max_plain(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = float('-inf')                    
                    R = operator.add(R_temp,max(D_temp,data[i-1]))                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = float('-inf')                    
                    R = operator.add(R_temp,max(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = float('-inf')                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM MAX STEADY
def sum_max_steady(data):
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
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    D = float('-inf')                    
                    R = operator.add(R_temp,max(max(D_temp,data[i-1]),data[i]))                    
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM MAX SUMMIT
def sum_max_summit(data):
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
                    C = max(D_temp,data[i-1])                    
                    D = float('-inf')                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 'u':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 0                    
                    D = float('-inf')                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = max(D_temp,data[i-1])                    
                    D = float('-inf')                    
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = float('-inf')                    
                    currentState = 's'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,data[i-1]))                    
                    D = float('-inf')                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'u':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM MAX DECREASING
def sum_max_decreasing(data):
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
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    D = float('-inf')                    
                    R = operator.add(R_temp,max(max(D_temp,data[i-1]),data[i]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM MAX STEADY_SEQUENCE
def sum_max_steady_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = float('-inf')                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = float('-inf')                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    C = max(max(D_temp,data[i-1]),data[i])                    
                    D = float('-inf')                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = max(C_temp,max(D_temp,data[i]))                    
                    D = float('-inf')                    
                    currentState = 'r'                    
    return operator.add(R,C)    

# ----- SUM SURFACE -----
# SUM SURFACE BUMP_ON_DECREASING_SEQUENCE
def sum_surface_bump_on_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'v':                
                    D = 0                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'v'                    
                elif currentState == 't':                
                    currentState = 't'                    
                elif currentState == 'v':                
                    D = 0                    
                    R = operator.add(R_temp,operator.add(D_temp,data[i-1]))                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    currentState = 's'                    
                elif currentState == 'v':                
                    D = 0                    
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM SURFACE STRICTLY_DECREASING_SEQUENCE
def sum_surface_strictly_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    C = operator.add(operator.add(D_temp,data[i-1]),data[i])                    
                    D = 0                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = operator.add(C_temp,operator.add(D_temp,data[i]))                    
                    D = 0                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
    return operator.add(R,C)    

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
                    R = operator.add(R_temp,operator.add(D_temp,data[i-1]))                    
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
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM SURFACE PROPER_PLATEAU
def sum_surface_proper_plateau(data):
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
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    R = operator.add(R_temp,operator.add(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM SURFACE INCREASING_SEQUENCE
def sum_surface_increasing_sequence(data):
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
                    C = operator.add(operator.add(D_temp,data[i-1]),data[i])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,data[i]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM SURFACE PLATEAU
def sum_surface_plateau(data):
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
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = 0                    
                    R = operator.add(R_temp,operator.add(D_temp,data[i-1]))                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    R = operator.add(R_temp,operator.add(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM SURFACE STRICTLY_INCREASING_SEQUENCE
def sum_surface_strictly_increasing_sequence(data):
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
                    C = operator.add(operator.add(D_temp,data[i-1]),data[i])                    
                    D = 0                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = operator.add(C_temp,operator.add(D_temp,data[i]))                    
                    D = 0                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM SURFACE VALLEY
def sum_surface_valley(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = operator.add(D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,data[i-1]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM SURFACE PROPER_PLAIN
def sum_surface_proper_plain(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    R = operator.add(R_temp,operator.add(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM SURFACE ZIGZAG
def sum_surface_zigzag(data):
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
                if currentState == 'a':                
                    currentState = 'a'                    
                elif currentState == 'c':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 'a'                    
                elif currentState == 'b':                
                    C = operator.add(D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 'c'                    
                elif currentState == 'e':                
                    D = 0                    
                    currentState = 'a'                    
                elif currentState == 'd':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'e'                    
                elif currentState == 'f':                
                    C = operator.add(C_temp,operator.add(D_temp,data[i-1]))                    
                    D = 0                    
                    currentState = 'c'                    
                elif currentState == 's':                
                    currentState = 'a'                    
            elif data[i] < data[i-1]:            
                if currentState == 'a':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'b'                    
                elif currentState == 'c':                
                    C = operator.add(C_temp,operator.add(D_temp,data[i-1]))                    
                    D = 0                    
                    currentState = 'f'                    
                elif currentState == 'b':                
                    currentState = 'd'                    
                elif currentState == 'e':                
                    C = operator.add(D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 'f'                    
                elif currentState == 'd':                
                    currentState = 'd'                    
                elif currentState == 'f':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 'd'                    
                elif currentState == 's':                
                    currentState = 'd'                    
            elif data[i] == data[i-1]:            
                if currentState == 'a':                
                    currentState = 's'                    
                elif currentState == 'c':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
                elif currentState == 'b':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 'e':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 'd':                
                    currentState = 's'                    
                elif currentState == 'f':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
                elif currentState == 's':                
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM SURFACE INFLEXION
def sum_surface_inflexion(data):
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
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    R = operator.add(R_temp,operator.add(D_temp,data[i-1]))                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 't'                    
                elif currentState == 'r':                
                    D = 0                    
                    R = operator.add(R_temp,operator.add(D_temp,data[i-1]))                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM SURFACE DECREASING_SEQUENCE
def sum_surface_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 't':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    C = operator.add(operator.add(D_temp,data[i-1]),data[i])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,data[i]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i])                    
                    currentState = 't'                    
    return operator.add(R,C)    

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
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = operator.add(D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,data[i-1]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM SURFACE DIP_ON_INCREASING_SEQUENCE
def sum_surface_dip_on_increasing_sequence(data):
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
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'v'                    
                elif currentState == 't':                
                    currentState = 't'                    
                elif currentState == 'v':                
                    D = 0                    
                    R = operator.add(R_temp,operator.add(D_temp,data[i-1]))                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'v':                
                    D = 0                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    currentState = 's'                    
                elif currentState == 'v':                
                    D = 0                    
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM SURFACE DECREASING_TERRACE
def sum_surface_decreasing_terrace(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    R = operator.add(R_temp,operator.add(D_temp,data[i-1]))                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM SURFACE GORGE
def sum_surface_gorge(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = operator.add(D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,data[i-1]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 'u':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'u':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

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
                    R = operator.add(R_temp,operator.add(operator.add(D_temp,data[i-1]),data[i]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM SURFACE PLAIN
def sum_surface_plain(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = 0                    
                    R = operator.add(R_temp,operator.add(D_temp,data[i-1]))                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    R = operator.add(R_temp,operator.add(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM SURFACE STEADY
def sum_surface_steady(data):
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
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    D = 0                    
                    R = operator.add(R_temp,operator.add(operator.add(D_temp,data[i-1]),data[i]))                    
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM SURFACE SUMMIT
def sum_surface_summit(data):
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
                    C = operator.add(D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 'u':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = operator.add(D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,data[i-1]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'u':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM SURFACE DECREASING
def sum_surface_decreasing(data):
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
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    D = 0                    
                    R = operator.add(R_temp,operator.add(operator.add(D_temp,data[i-1]),data[i]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM SURFACE STEADY_SEQUENCE
def sum_surface_steady_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    C = operator.add(operator.add(D_temp,data[i-1]),data[i])                    
                    D = 0                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = operator.add(C_temp,operator.add(D_temp,data[i]))                    
                    D = 0                    
                    currentState = 'r'                    
    return operator.add(R,C)    

# ----- SUM ONE -----
# SUM ONE BUMP_ON_DECREASING_SEQUENCE
def sum_one_bump_on_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 1                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = max(D_temp,0)                    
                    currentState = 'u'                    
                elif currentState == 'v':                
                    D = 1                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = max(D_temp,0)                    
                    currentState = 'v'                    
                elif currentState == 't':                
                    currentState = 't'                    
                elif currentState == 'v':                
                    D = 1                    
                    R = operator.add(R_temp,max(D_temp,0))                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 1                    
                    currentState = 's'                    
                elif currentState == 't':                
                    currentState = 's'                    
                elif currentState == 'v':                
                    D = 1                    
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM ONE STRICTLY_DECREASING_SEQUENCE
def sum_one_strictly_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = 1                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    C = max(max(D_temp,0),data[i])                    
                    D = 1                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = max(C_temp,max(D_temp,data[i]))                    
                    D = 1                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = 1                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
    return operator.add(R,C)    

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
                    R = operator.add(R_temp,max(D_temp,0))                    
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
    return operator.add(R,C)    

# SUM ONE PROPER_PLATEAU
def sum_one_proper_plateau(data):
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
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 1                    
                    R = operator.add(R_temp,max(D_temp,0))                    
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
    return operator.add(R,C)    

# SUM ONE INCREASING_SEQUENCE
def sum_one_increasing_sequence(data):
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
                    C = max(max(D_temp,0),data[i])                    
                    D = 1                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,data[i]))                    
                    D = 1                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    C = 0                    
                    D = 1                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM ONE PLATEAU
def sum_one_plateau(data):
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
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = 1                    
                    R = operator.add(R_temp,max(D_temp,0))                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 1                    
                    R = operator.add(R_temp,max(D_temp,0))                    
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
    return operator.add(R,C)    

# SUM ONE STRICTLY_INCREASING_SEQUENCE
def sum_one_strictly_increasing_sequence(data):
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
                    C = max(max(D_temp,0),data[i])                    
                    D = 1                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = max(C_temp,max(D_temp,data[i]))                    
                    D = 1                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = 1                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = 1                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM ONE VALLEY
def sum_one_valley(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = max(D_temp,0)                    
                    D = 1                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,0))                    
                    D = 1                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = max(D_temp,0)                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 0                    
                    D = 1                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,0)                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = max(D_temp,0)                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM ONE PROPER_PLAIN
def sum_one_proper_plain(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 1                    
                    R = operator.add(R_temp,max(D_temp,0))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 1                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,0)                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = max(D_temp,0)                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM ONE ZIGZAG
def sum_one_zigzag(data):
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
                if currentState == 'a':                
                    currentState = 'a'                    
                elif currentState == 'c':                
                    C = 0                    
                    D = 1                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 'a'                    
                elif currentState == 'b':                
                    C = max(D_temp,0)                    
                    D = 1                    
                    currentState = 'c'                    
                elif currentState == 'e':                
                    D = 1                    
                    currentState = 'a'                    
                elif currentState == 'd':                
                    D = max(D_temp,0)                    
                    currentState = 'e'                    
                elif currentState == 'f':                
                    C = max(C_temp,max(D_temp,0))                    
                    D = 1                    
                    currentState = 'c'                    
                elif currentState == 's':                
                    currentState = 'a'                    
            elif data[i] < data[i-1]:            
                if currentState == 'a':                
                    D = max(D_temp,0)                    
                    currentState = 'b'                    
                elif currentState == 'c':                
                    C = max(C_temp,max(D_temp,0))                    
                    D = 1                    
                    currentState = 'f'                    
                elif currentState == 'b':                
                    currentState = 'd'                    
                elif currentState == 'e':                
                    C = max(D_temp,0)                    
                    D = 1                    
                    currentState = 'f'                    
                elif currentState == 'd':                
                    currentState = 'd'                    
                elif currentState == 'f':                
                    C = 0                    
                    D = 1                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 'd'                    
                elif currentState == 's':                
                    currentState = 'd'                    
            elif data[i] == data[i-1]:            
                if currentState == 'a':                
                    currentState = 's'                    
                elif currentState == 'c':                
                    C = 0                    
                    D = 1                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
                elif currentState == 'b':                
                    D = 1                    
                    currentState = 's'                    
                elif currentState == 'e':                
                    D = 1                    
                    currentState = 's'                    
                elif currentState == 'd':                
                    currentState = 's'                    
                elif currentState == 'f':                
                    C = 0                    
                    D = 1                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
                elif currentState == 's':                
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM ONE INFLEXION
def sum_one_inflexion(data):
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
                    D = 1                    
                    R = operator.add(R_temp,max(D_temp,0))                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 't'                    
                elif currentState == 'r':                
                    D = 1                    
                    R = operator.add(R_temp,max(D_temp,0))                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = max(D_temp,0)                    
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
    return operator.add(R,C)    

# SUM ONE DECREASING_SEQUENCE
def sum_one_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 't':                
                    C = 0                    
                    D = 1                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    C = max(max(D_temp,0),data[i])                    
                    D = 1                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,data[i]))                    
                    D = 1                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i])                    
                    currentState = 't'                    
    return operator.add(R,C)    

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
                    R = operator.add(R_temp,C_temp)                    
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
    return operator.add(R,C)    

# SUM ONE DIP_ON_INCREASING_SEQUENCE
def sum_one_dip_on_increasing_sequence(data):
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
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = max(D_temp,0)                    
                    currentState = 'v'                    
                elif currentState == 't':                
                    currentState = 't'                    
                elif currentState == 'v':                
                    D = 1                    
                    R = operator.add(R_temp,max(D_temp,0))                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 1                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = max(D_temp,0)                    
                    currentState = 'u'                    
                elif currentState == 'v':                
                    D = 1                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 1                    
                    currentState = 's'                    
                elif currentState == 't':                
                    currentState = 's'                    
                elif currentState == 'v':                
                    D = 1                    
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM ONE DECREASING_TERRACE
def sum_one_decreasing_terrace(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 1                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 1                    
                    R = operator.add(R_temp,max(D_temp,0))                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,0)                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = max(D_temp,0)                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM ONE GORGE
def sum_one_gorge(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = max(D_temp,0)                    
                    D = 1                    
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = 1                    
                    currentState = 's'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,0))                    
                    D = 1                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = max(D_temp,0)                    
                    currentState = 'r'                    
                elif currentState == 'u':                
                    D = max(D_temp,0)                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 0                    
                    D = 1                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,0)                    
                    currentState = 'u'                    
                elif currentState == 'u':                
                    D = max(D_temp,0)                    
                    currentState = 'u'                    
                elif currentState == 't':                
                    D = max(D_temp,0)                    
                    currentState = 't'                    
    return operator.add(R,C)    

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
                    R = operator.add(R_temp,max(max(D_temp,0),data[i]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM ONE PLAIN
def sum_one_plain(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = 1                    
                    R = operator.add(R_temp,max(D_temp,0))                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 1                    
                    R = operator.add(R_temp,max(D_temp,0))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 1                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,0)                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = max(D_temp,0)                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM ONE STEADY
def sum_one_steady(data):
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
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    D = 1                    
                    R = operator.add(R_temp,max(max(D_temp,0),data[i]))                    
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM ONE SUMMIT
def sum_one_summit(data):
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
                    C = max(D_temp,0)                    
                    D = 1                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = max(D_temp,0)                    
                    currentState = 'r'                    
                elif currentState == 'u':                
                    D = max(D_temp,0)                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 0                    
                    D = 1                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = max(D_temp,0)                    
                    D = 1                    
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = 1                    
                    currentState = 's'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,0))                    
                    D = 1                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,0)                    
                    currentState = 'u'                    
                elif currentState == 'u':                
                    D = max(D_temp,0)                    
                    currentState = 'u'                    
                elif currentState == 't':                
                    D = max(D_temp,0)                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM ONE DECREASING
def sum_one_decreasing(data):
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
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    D = 1                    
                    R = operator.add(R_temp,max(max(D_temp,0),data[i]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM ONE STEADY_SEQUENCE
def sum_one_steady_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = 1                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = 1                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    C = max(max(D_temp,0),data[i])                    
                    D = 1                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = max(C_temp,max(D_temp,data[i]))                    
                    D = 1                    
                    currentState = 'r'                    
    return operator.add(R,C)    

# ----- SUM WIDTH -----
# SUM WIDTH BUMP_ON_DECREASING_SEQUENCE
def sum_width_bump_on_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'u'                    
                elif currentState == 'v':                
                    D = 0                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'v'                    
                elif currentState == 't':                
                    currentState = 't'                    
                elif currentState == 'v':                
                    D = 0                    
                    R = operator.add(R_temp,operator.add(D_temp,1))                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    currentState = 's'                    
                elif currentState == 'v':                
                    D = 0                    
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM WIDTH STRICTLY_DECREASING_SEQUENCE
def sum_width_strictly_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    C = operator.add(operator.add(D_temp,1),1)                    
                    D = 0                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = operator.add(C_temp,operator.add(D_temp,1))                    
                    D = 0                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
    return operator.add(R,C)    

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
                    R = operator.add(R_temp,operator.add(D_temp,1))                    
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
    return operator.add(R,C)    

# SUM WIDTH PROPER_PLATEAU
def sum_width_proper_plateau(data):
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
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    R = operator.add(R_temp,operator.add(D_temp,1))                    
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
    return operator.add(R,C)    

# SUM WIDTH INCREASING_SEQUENCE
def sum_width_increasing_sequence(data):
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
                    C = operator.add(operator.add(D_temp,1),1)                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,1))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,1)                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM WIDTH PLATEAU
def sum_width_plateau(data):
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
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = 0                    
                    R = operator.add(R_temp,operator.add(D_temp,1))                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    R = operator.add(R_temp,operator.add(D_temp,1))                    
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
    return operator.add(R,C)    

# SUM WIDTH STRICTLY_INCREASING_SEQUENCE
def sum_width_strictly_increasing_sequence(data):
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
                    C = operator.add(operator.add(D_temp,1),1)                    
                    D = 0                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = operator.add(C_temp,operator.add(D_temp,1))                    
                    D = 0                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM WIDTH VALLEY
def sum_width_valley(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = operator.add(D_temp,1)                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,1))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,1)                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM WIDTH PROPER_PLAIN
def sum_width_proper_plain(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    R = operator.add(R_temp,operator.add(D_temp,1))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,1)                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,1)                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM WIDTH ZIGZAG
def sum_width_zigzag(data):
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
                if currentState == 'a':                
                    currentState = 'a'                    
                elif currentState == 'c':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 'a'                    
                elif currentState == 'b':                
                    C = operator.add(D_temp,1)                    
                    D = 0                    
                    currentState = 'c'                    
                elif currentState == 'e':                
                    D = 0                    
                    currentState = 'a'                    
                elif currentState == 'd':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'e'                    
                elif currentState == 'f':                
                    C = operator.add(C_temp,operator.add(D_temp,1))                    
                    D = 0                    
                    currentState = 'c'                    
                elif currentState == 's':                
                    currentState = 'a'                    
            elif data[i] < data[i-1]:            
                if currentState == 'a':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'b'                    
                elif currentState == 'c':                
                    C = operator.add(C_temp,operator.add(D_temp,1))                    
                    D = 0                    
                    currentState = 'f'                    
                elif currentState == 'b':                
                    currentState = 'd'                    
                elif currentState == 'e':                
                    C = operator.add(D_temp,1)                    
                    D = 0                    
                    currentState = 'f'                    
                elif currentState == 'd':                
                    currentState = 'd'                    
                elif currentState == 'f':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 'd'                    
                elif currentState == 's':                
                    currentState = 'd'                    
            elif data[i] == data[i-1]:            
                if currentState == 'a':                
                    currentState = 's'                    
                elif currentState == 'c':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
                elif currentState == 'b':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 'e':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 'd':                
                    currentState = 's'                    
                elif currentState == 'f':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
                elif currentState == 's':                
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM WIDTH INFLEXION
def sum_width_inflexion(data):
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
                    D = 0                    
                    R = operator.add(R_temp,operator.add(D_temp,1))                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 't'                    
                elif currentState == 'r':                
                    D = 0                    
                    R = operator.add(R_temp,operator.add(D_temp,1))                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,1)                    
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
    return operator.add(R,C)    

# SUM WIDTH DECREASING_SEQUENCE
def sum_width_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 't':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    C = operator.add(operator.add(D_temp,1),1)                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,1))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,1)                    
                    currentState = 't'                    
    return operator.add(R,C)    

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
                    R = operator.add(R_temp,C_temp)                    
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
    return operator.add(R,C)    

# SUM WIDTH DIP_ON_INCREASING_SEQUENCE
def sum_width_dip_on_increasing_sequence(data):
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
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'v'                    
                elif currentState == 't':                
                    currentState = 't'                    
                elif currentState == 'v':                
                    D = 0                    
                    R = operator.add(R_temp,operator.add(D_temp,1))                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'u'                    
                elif currentState == 'v':                
                    D = 0                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    currentState = 's'                    
                elif currentState == 'v':                
                    D = 0                    
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM WIDTH DECREASING_TERRACE
def sum_width_decreasing_terrace(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    R = operator.add(R_temp,operator.add(D_temp,1))                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,1)                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,1)                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM WIDTH GORGE
def sum_width_gorge(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = operator.add(D_temp,1)                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,1))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'r'                    
                elif currentState == 'u':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'u'                    
                elif currentState == 'u':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'u'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,1)                    
                    currentState = 't'                    
    return operator.add(R,C)    

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
                    R = operator.add(R_temp,operator.add(operator.add(D_temp,1),1))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM WIDTH PLAIN
def sum_width_plain(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = 0                    
                    R = operator.add(R_temp,operator.add(D_temp,1))                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    R = operator.add(R_temp,operator.add(D_temp,1))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,1)                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,1)                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM WIDTH STEADY
def sum_width_steady(data):
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
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    D = 0                    
                    R = operator.add(R_temp,operator.add(operator.add(D_temp,1),1))                    
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM WIDTH SUMMIT
def sum_width_summit(data):
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
                    C = operator.add(D_temp,1)                    
                    D = 0                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'r'                    
                elif currentState == 'u':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = operator.add(D_temp,1)                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,1))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'u'                    
                elif currentState == 'u':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'u'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,1)                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM WIDTH DECREASING
def sum_width_decreasing(data):
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
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    D = 0                    
                    R = operator.add(R_temp,operator.add(operator.add(D_temp,1),1))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM WIDTH STEADY_SEQUENCE
def sum_width_steady_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    C = operator.add(operator.add(D_temp,1),1)                    
                    D = 0                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = operator.add(C_temp,operator.add(D_temp,1))                    
                    D = 0                    
                    currentState = 'r'                    
    return operator.add(R,C)    

# ----- SUM RANGE -----
# SUM RANGE BUMP_ON_DECREASING_SEQUENCE
def sum_range_bump_on_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'v':                
                    D = 0                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'v'                    
                elif currentState == 't':                
                    currentState = 't'                    
                elif currentState == 'v':                
                    D = 0                    
                    R = operator.add(R_temp,(D_temp,data[i-1]))                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    currentState = 's'                    
                elif currentState == 'v':                
                    D = 0                    
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM RANGE STRICTLY_DECREASING_SEQUENCE
def sum_range_strictly_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    C = ((D_temp,data[i-1]),data[i])                    
                    D = 0                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = (C_temp,(D_temp,data[i]))                    
                    D = 0                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
    return operator.add(R,C)    

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
                    R = operator.add(R_temp,(D_temp,data[i-1]))                    
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
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM RANGE PROPER_PLATEAU
def sum_range_proper_plateau(data):
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
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    R = operator.add(R_temp,(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM RANGE INCREASING_SEQUENCE
def sum_range_increasing_sequence(data):
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
                    C = ((D_temp,data[i-1]),data[i])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = (C_temp,(D_temp,data[i]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = (D_temp,data[i])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM RANGE PLATEAU
def sum_range_plateau(data):
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
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = 0                    
                    R = operator.add(R_temp,(D_temp,data[i-1]))                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    R = operator.add(R_temp,(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM RANGE STRICTLY_INCREASING_SEQUENCE
def sum_range_strictly_increasing_sequence(data):
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
                    C = ((D_temp,data[i-1]),data[i])                    
                    D = 0                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = (C_temp,(D_temp,data[i]))                    
                    D = 0                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM RANGE VALLEY
def sum_range_valley(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = (D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = (C_temp,(D_temp,data[i-1]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM RANGE PROPER_PLAIN
def sum_range_proper_plain(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    R = operator.add(R_temp,(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM RANGE ZIGZAG
def sum_range_zigzag(data):
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
                if currentState == 'a':                
                    currentState = 'a'                    
                elif currentState == 'c':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 'a'                    
                elif currentState == 'b':                
                    C = (D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 'c'                    
                elif currentState == 'e':                
                    D = 0                    
                    currentState = 'a'                    
                elif currentState == 'd':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'e'                    
                elif currentState == 'f':                
                    C = (C_temp,(D_temp,data[i-1]))                    
                    D = 0                    
                    currentState = 'c'                    
                elif currentState == 's':                
                    currentState = 'a'                    
            elif data[i] < data[i-1]:            
                if currentState == 'a':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'b'                    
                elif currentState == 'c':                
                    C = (C_temp,(D_temp,data[i-1]))                    
                    D = 0                    
                    currentState = 'f'                    
                elif currentState == 'b':                
                    currentState = 'd'                    
                elif currentState == 'e':                
                    C = (D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 'f'                    
                elif currentState == 'd':                
                    currentState = 'd'                    
                elif currentState == 'f':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 'd'                    
                elif currentState == 's':                
                    currentState = 'd'                    
            elif data[i] == data[i-1]:            
                if currentState == 'a':                
                    currentState = 's'                    
                elif currentState == 'c':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
                elif currentState == 'b':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 'e':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 'd':                
                    currentState = 's'                    
                elif currentState == 'f':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
                elif currentState == 's':                
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM RANGE INFLEXION
def sum_range_inflexion(data):
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
                    D = (D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    R = operator.add(R_temp,(D_temp,data[i-1]))                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 't'                    
                elif currentState == 'r':                
                    D = 0                    
                    R = operator.add(R_temp,(D_temp,data[i-1]))                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM RANGE DECREASING_SEQUENCE
def sum_range_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 't':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    C = ((D_temp,data[i-1]),data[i])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = (C_temp,(D_temp,data[i]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = (D_temp,data[i])                    
                    currentState = 't'                    
    return operator.add(R,C)    

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
                    D = (D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = (D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = (C_temp,(D_temp,data[i-1]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM RANGE DIP_ON_INCREASING_SEQUENCE
def sum_range_dip_on_increasing_sequence(data):
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
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'v'                    
                elif currentState == 't':                
                    currentState = 't'                    
                elif currentState == 'v':                
                    D = 0                    
                    R = operator.add(R_temp,(D_temp,data[i-1]))                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'v':                
                    D = 0                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    currentState = 's'                    
                elif currentState == 'v':                
                    D = 0                    
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM RANGE DECREASING_TERRACE
def sum_range_decreasing_terrace(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    R = operator.add(R_temp,(D_temp,data[i-1]))                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM RANGE GORGE
def sum_range_gorge(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = (D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    C = (C_temp,(D_temp,data[i-1]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 'u':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'u':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

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
                    R = operator.add(R_temp,((D_temp,data[i-1]),data[i]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM RANGE PLAIN
def sum_range_plain(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = 0                    
                    R = operator.add(R_temp,(D_temp,data[i-1]))                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    R = operator.add(R_temp,(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM RANGE STEADY
def sum_range_steady(data):
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
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    D = 0                    
                    R = operator.add(R_temp,((D_temp,data[i-1]),data[i]))                    
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM RANGE SUMMIT
def sum_range_summit(data):
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
                    C = (D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 'u':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = (D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    C = (C_temp,(D_temp,data[i-1]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'u':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
    return operator.add(R,C)    

# SUM RANGE DECREASING
def sum_range_decreasing(data):
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
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    D = 0                    
                    R = operator.add(R_temp,((D_temp,data[i-1]),data[i]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return operator.add(R,C)    

# SUM RANGE STEADY_SEQUENCE
def sum_range_steady_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 0                    
                    D = 0                    
                    R = operator.add(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    C = ((D_temp,data[i-1]),data[i])                    
                    D = 0                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = (C_temp,(D_temp,data[i]))                    
                    D = 0                    
                    currentState = 'r'                    
    return operator.add(R,C)    

# ----- MIN -----
# ----- MIN MIN -----
# MIN MIN BUMP_ON_DECREASING_SEQUENCE
def min_min_bump_on_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = float('inf')                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'v':                
                    D = float('inf')                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'v'                    
                elif currentState == 't':                
                    currentState = 't'                    
                elif currentState == 'v':                
                    D = float('inf')                    
                    R = min(R_temp,min(D_temp,data[i-1]))                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = float('inf')                    
                    currentState = 's'                    
                elif currentState == 't':                
                    currentState = 's'                    
                elif currentState == 'v':                
                    D = float('inf')                    
                    currentState = 's'                    
    return min(R,C)    

# MIN MIN STRICTLY_DECREASING_SEQUENCE
def min_min_strictly_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('inf')                    
                    D = float('inf')                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    C = min(min(D_temp,data[i-1]),data[i])                    
                    D = float('inf')                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = min(C_temp,min(D_temp,data[i]))                    
                    D = float('inf')                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('inf')                    
                    D = float('inf')                    
                    R = min(R_temp,C_temp)                    
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
                    R = min(R_temp,min(D_temp,data[i-1]))                    
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
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN MIN PROPER_PLATEAU
def min_min_proper_plateau(data):
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
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = float('inf')                    
                    R = min(R_temp,min(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN MIN INCREASING_SEQUENCE
def min_min_increasing_sequence(data):
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
                    C = min(min(D_temp,data[i-1]),data[i])                    
                    D = float('inf')                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = min(C_temp,min(D_temp,data[i]))                    
                    D = float('inf')                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    C = float('inf')                    
                    D = float('inf')                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN MIN PLATEAU
def min_min_plateau(data):
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
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = float('inf')                    
                    R = min(R_temp,min(D_temp,data[i-1]))                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = float('inf')                    
                    R = min(R_temp,min(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN MIN STRICTLY_INCREASING_SEQUENCE
def min_min_strictly_increasing_sequence(data):
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
                    C = min(min(D_temp,data[i-1]),data[i])                    
                    D = float('inf')                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = min(C_temp,min(D_temp,data[i]))                    
                    D = float('inf')                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('inf')                    
                    D = float('inf')                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('inf')                    
                    D = float('inf')                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
    return min(R,C)    

# MIN MIN VALLEY
def min_min_valley(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = min(D_temp,data[i-1])                    
                    D = float('inf')                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = min(C_temp,min(D_temp,data[i-1]))                    
                    D = float('inf')                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = float('inf')                    
                    D = float('inf')                    
                    R = min(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN MIN PROPER_PLAIN
def min_min_proper_plain(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = float('inf')                    
                    R = min(R_temp,min(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = float('inf')                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN MIN ZIGZAG
def min_min_zigzag(data):
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
                if currentState == 'a':                
                    currentState = 'a'                    
                elif currentState == 'c':                
                    C = float('inf')                    
                    D = float('inf')                    
                    R = min(R_temp,C_temp)                    
                    currentState = 'a'                    
                elif currentState == 'b':                
                    C = min(D_temp,data[i-1])                    
                    D = float('inf')                    
                    currentState = 'c'                    
                elif currentState == 'e':                
                    D = float('inf')                    
                    currentState = 'a'                    
                elif currentState == 'd':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'e'                    
                elif currentState == 'f':                
                    C = min(C_temp,min(D_temp,data[i-1]))                    
                    D = float('inf')                    
                    currentState = 'c'                    
                elif currentState == 's':                
                    currentState = 'a'                    
            elif data[i] < data[i-1]:            
                if currentState == 'a':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'b'                    
                elif currentState == 'c':                
                    C = min(C_temp,min(D_temp,data[i-1]))                    
                    D = float('inf')                    
                    currentState = 'f'                    
                elif currentState == 'b':                
                    currentState = 'd'                    
                elif currentState == 'e':                
                    C = min(D_temp,data[i-1])                    
                    D = float('inf')                    
                    currentState = 'f'                    
                elif currentState == 'd':                
                    currentState = 'd'                    
                elif currentState == 'f':                
                    C = float('inf')                    
                    D = float('inf')                    
                    R = min(R_temp,C_temp)                    
                    currentState = 'd'                    
                elif currentState == 's':                
                    currentState = 'd'                    
            elif data[i] == data[i-1]:            
                if currentState == 'a':                
                    currentState = 's'                    
                elif currentState == 'c':                
                    C = float('inf')                    
                    D = float('inf')                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
                elif currentState == 'b':                
                    D = float('inf')                    
                    currentState = 's'                    
                elif currentState == 'e':                
                    D = float('inf')                    
                    currentState = 's'                    
                elif currentState == 'd':                
                    currentState = 's'                    
                elif currentState == 'f':                
                    C = float('inf')                    
                    D = float('inf')                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
                elif currentState == 's':                
                    currentState = 's'                    
    return min(R,C)    

# MIN MIN INFLEXION
def min_min_inflexion(data):
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
                    D = min(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = float('inf')                    
                    R = min(R_temp,min(D_temp,data[i-1]))                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 't'                    
                elif currentState == 'r':                
                    D = float('inf')                    
                    R = min(R_temp,min(D_temp,data[i-1]))                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN MIN DECREASING_SEQUENCE
def min_min_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 't':                
                    C = float('inf')                    
                    D = float('inf')                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    C = min(min(D_temp,data[i-1]),data[i])                    
                    D = float('inf')                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = min(C_temp,min(D_temp,data[i]))                    
                    D = float('inf')                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
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
                    D = min(D_temp,data[i-1])                    
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
                    C = min(D_temp,data[i-1])                    
                    D = float('inf')                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = min(C_temp,min(D_temp,data[i-1]))                    
                    D = float('inf')                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN MIN DIP_ON_INCREASING_SEQUENCE
def min_min_dip_on_increasing_sequence(data):
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
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'v'                    
                elif currentState == 't':                
                    currentState = 't'                    
                elif currentState == 'v':                
                    D = float('inf')                    
                    R = min(R_temp,min(D_temp,data[i-1]))                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = float('inf')                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'v':                
                    D = float('inf')                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = float('inf')                    
                    currentState = 's'                    
                elif currentState == 't':                
                    currentState = 's'                    
                elif currentState == 'v':                
                    D = float('inf')                    
                    currentState = 's'                    
    return min(R,C)    

# MIN MIN DECREASING_TERRACE
def min_min_decreasing_terrace(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = float('inf')                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = float('inf')                    
                    R = min(R_temp,min(D_temp,data[i-1]))                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN MIN GORGE
def min_min_gorge(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = min(D_temp,data[i-1])                    
                    D = float('inf')                    
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = float('inf')                    
                    currentState = 's'                    
                elif currentState == 't':                
                    C = min(C_temp,min(D_temp,data[i-1]))                    
                    D = float('inf')                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 'u':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = float('inf')                    
                    D = float('inf')                    
                    R = min(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'u':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

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
                    R = min(R_temp,min(min(D_temp,data[i-1]),data[i]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return min(R,C)    

# MIN MIN PLAIN
def min_min_plain(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = float('inf')                    
                    R = min(R_temp,min(D_temp,data[i-1]))                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = float('inf')                    
                    R = min(R_temp,min(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = float('inf')                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN MIN STEADY
def min_min_steady(data):
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
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    D = float('inf')                    
                    R = min(R_temp,min(min(D_temp,data[i-1]),data[i]))                    
                    currentState = 's'                    
    return min(R,C)    

# MIN MIN SUMMIT
def min_min_summit(data):
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
                    C = min(D_temp,data[i-1])                    
                    D = float('inf')                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 'u':                
                    D = min(D_temp,data[i-1])                    
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
                    C = min(D_temp,data[i-1])                    
                    D = float('inf')                    
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = float('inf')                    
                    currentState = 's'                    
                elif currentState == 't':                
                    C = min(C_temp,min(D_temp,data[i-1]))                    
                    D = float('inf')                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'u':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 't':                
                    D = min(D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN MIN DECREASING
def min_min_decreasing(data):
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
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    D = float('inf')                    
                    R = min(R_temp,min(min(D_temp,data[i-1]),data[i]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return min(R,C)    

# MIN MIN STEADY_SEQUENCE
def min_min_steady_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('inf')                    
                    D = float('inf')                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('inf')                    
                    D = float('inf')                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    C = min(min(D_temp,data[i-1]),data[i])                    
                    D = float('inf')                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = min(C_temp,min(D_temp,data[i]))                    
                    D = float('inf')                    
                    currentState = 'r'                    
    return min(R,C)    

# ----- MIN MAX -----
# MIN MAX BUMP_ON_DECREASING_SEQUENCE
def min_max_bump_on_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = float('-inf')                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'v':                
                    D = float('-inf')                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'v'                    
                elif currentState == 't':                
                    currentState = 't'                    
                elif currentState == 'v':                
                    D = float('-inf')                    
                    R = min(R_temp,max(D_temp,data[i-1]))                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = float('-inf')                    
                    currentState = 's'                    
                elif currentState == 't':                
                    currentState = 's'                    
                elif currentState == 'v':                
                    D = float('-inf')                    
                    currentState = 's'                    
    return min(R,C)    

# MIN MAX STRICTLY_DECREASING_SEQUENCE
def min_max_strictly_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('inf')                    
                    D = float('-inf')                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    C = max(max(D_temp,data[i-1]),data[i])                    
                    D = float('-inf')                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = max(C_temp,max(D_temp,data[i]))                    
                    D = float('-inf')                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('inf')                    
                    D = float('-inf')                    
                    R = min(R_temp,C_temp)                    
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
                    R = min(R_temp,max(D_temp,data[i-1]))                    
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
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN MAX PROPER_PLATEAU
def min_max_proper_plateau(data):
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
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = float('-inf')                    
                    R = min(R_temp,max(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN MAX INCREASING_SEQUENCE
def min_max_increasing_sequence(data):
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
                    C = max(max(D_temp,data[i-1]),data[i])                    
                    D = float('-inf')                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,data[i]))                    
                    D = float('-inf')                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    C = float('inf')                    
                    D = float('-inf')                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN MAX PLATEAU
def min_max_plateau(data):
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
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = float('-inf')                    
                    R = min(R_temp,max(D_temp,data[i-1]))                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = float('-inf')                    
                    R = min(R_temp,max(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN MAX STRICTLY_INCREASING_SEQUENCE
def min_max_strictly_increasing_sequence(data):
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
                    C = max(max(D_temp,data[i-1]),data[i])                    
                    D = float('-inf')                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = max(C_temp,max(D_temp,data[i]))                    
                    D = float('-inf')                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('inf')                    
                    D = float('-inf')                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('inf')                    
                    D = float('-inf')                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
    return min(R,C)    

# MIN MAX VALLEY
def min_max_valley(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = max(D_temp,data[i-1])                    
                    D = float('-inf')                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,data[i-1]))                    
                    D = float('-inf')                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = float('inf')                    
                    D = float('-inf')                    
                    R = min(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN MAX PROPER_PLAIN
def min_max_proper_plain(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = float('-inf')                    
                    R = min(R_temp,max(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = float('-inf')                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN MAX ZIGZAG
def min_max_zigzag(data):
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
                if currentState == 'a':                
                    currentState = 'a'                    
                elif currentState == 'c':                
                    C = float('inf')                    
                    D = float('-inf')                    
                    R = min(R_temp,C_temp)                    
                    currentState = 'a'                    
                elif currentState == 'b':                
                    C = max(D_temp,data[i-1])                    
                    D = float('-inf')                    
                    currentState = 'c'                    
                elif currentState == 'e':                
                    D = float('-inf')                    
                    currentState = 'a'                    
                elif currentState == 'd':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'e'                    
                elif currentState == 'f':                
                    C = max(C_temp,max(D_temp,data[i-1]))                    
                    D = float('-inf')                    
                    currentState = 'c'                    
                elif currentState == 's':                
                    currentState = 'a'                    
            elif data[i] < data[i-1]:            
                if currentState == 'a':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'b'                    
                elif currentState == 'c':                
                    C = max(C_temp,max(D_temp,data[i-1]))                    
                    D = float('-inf')                    
                    currentState = 'f'                    
                elif currentState == 'b':                
                    currentState = 'd'                    
                elif currentState == 'e':                
                    C = max(D_temp,data[i-1])                    
                    D = float('-inf')                    
                    currentState = 'f'                    
                elif currentState == 'd':                
                    currentState = 'd'                    
                elif currentState == 'f':                
                    C = float('inf')                    
                    D = float('-inf')                    
                    R = min(R_temp,C_temp)                    
                    currentState = 'd'                    
                elif currentState == 's':                
                    currentState = 'd'                    
            elif data[i] == data[i-1]:            
                if currentState == 'a':                
                    currentState = 's'                    
                elif currentState == 'c':                
                    C = float('inf')                    
                    D = float('-inf')                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
                elif currentState == 'b':                
                    D = float('-inf')                    
                    currentState = 's'                    
                elif currentState == 'e':                
                    D = float('-inf')                    
                    currentState = 's'                    
                elif currentState == 'd':                
                    currentState = 's'                    
                elif currentState == 'f':                
                    C = float('inf')                    
                    D = float('-inf')                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
                elif currentState == 's':                
                    currentState = 's'                    
    return min(R,C)    

# MIN MAX INFLEXION
def min_max_inflexion(data):
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
                    D = max(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = float('-inf')                    
                    R = min(R_temp,max(D_temp,data[i-1]))                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 't'                    
                elif currentState == 'r':                
                    D = float('-inf')                    
                    R = min(R_temp,max(D_temp,data[i-1]))                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN MAX DECREASING_SEQUENCE
def min_max_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 't':                
                    C = float('inf')                    
                    D = float('-inf')                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    C = max(max(D_temp,data[i-1]),data[i])                    
                    D = float('-inf')                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,data[i]))                    
                    D = float('-inf')                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
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
                    D = max(D_temp,data[i-1])                    
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
                    C = max(D_temp,data[i-1])                    
                    D = float('-inf')                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,data[i-1]))                    
                    D = float('-inf')                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN MAX DIP_ON_INCREASING_SEQUENCE
def min_max_dip_on_increasing_sequence(data):
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
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'v'                    
                elif currentState == 't':                
                    currentState = 't'                    
                elif currentState == 'v':                
                    D = float('-inf')                    
                    R = min(R_temp,max(D_temp,data[i-1]))                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = float('-inf')                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'v':                
                    D = float('-inf')                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = float('-inf')                    
                    currentState = 's'                    
                elif currentState == 't':                
                    currentState = 's'                    
                elif currentState == 'v':                
                    D = float('-inf')                    
                    currentState = 's'                    
    return min(R,C)    

# MIN MAX DECREASING_TERRACE
def min_max_decreasing_terrace(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = float('-inf')                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = float('-inf')                    
                    R = min(R_temp,max(D_temp,data[i-1]))                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN MAX GORGE
def min_max_gorge(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = max(D_temp,data[i-1])                    
                    D = float('-inf')                    
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = float('-inf')                    
                    currentState = 's'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,data[i-1]))                    
                    D = float('-inf')                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 'u':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = float('inf')                    
                    D = float('-inf')                    
                    R = min(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'u':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

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
                    R = min(R_temp,max(max(D_temp,data[i-1]),data[i]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return min(R,C)    

# MIN MAX PLAIN
def min_max_plain(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = float('-inf')                    
                    R = min(R_temp,max(D_temp,data[i-1]))                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = float('-inf')                    
                    R = min(R_temp,max(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = float('-inf')                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN MAX STEADY
def min_max_steady(data):
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
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    D = float('-inf')                    
                    R = min(R_temp,max(max(D_temp,data[i-1]),data[i]))                    
                    currentState = 's'                    
    return min(R,C)    

# MIN MAX SUMMIT
def min_max_summit(data):
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
                    C = max(D_temp,data[i-1])                    
                    D = float('-inf')                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 'u':                
                    D = max(D_temp,data[i-1])                    
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
                    C = max(D_temp,data[i-1])                    
                    D = float('-inf')                    
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = float('-inf')                    
                    currentState = 's'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,data[i-1]))                    
                    D = float('-inf')                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'u':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN MAX DECREASING
def min_max_decreasing(data):
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
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    D = float('-inf')                    
                    R = min(R_temp,max(max(D_temp,data[i-1]),data[i]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return min(R,C)    

# MIN MAX STEADY_SEQUENCE
def min_max_steady_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('inf')                    
                    D = float('-inf')                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('inf')                    
                    D = float('-inf')                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    C = max(max(D_temp,data[i-1]),data[i])                    
                    D = float('-inf')                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = max(C_temp,max(D_temp,data[i]))                    
                    D = float('-inf')                    
                    currentState = 'r'                    
    return min(R,C)    

# ----- MIN SURFACE -----
# MIN SURFACE BUMP_ON_DECREASING_SEQUENCE
def min_surface_bump_on_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'v':                
                    D = 0                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'v'                    
                elif currentState == 't':                
                    currentState = 't'                    
                elif currentState == 'v':                
                    D = 0                    
                    R = min(R_temp,operator.add(D_temp,data[i-1]))                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    currentState = 's'                    
                elif currentState == 'v':                
                    D = 0                    
                    currentState = 's'                    
    return min(R,C)    

# MIN SURFACE STRICTLY_DECREASING_SEQUENCE
def min_surface_strictly_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('inf')                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    C = operator.add(operator.add(D_temp,data[i-1]),data[i])                    
                    D = 0                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = operator.add(C_temp,operator.add(D_temp,data[i]))                    
                    D = 0                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('inf')                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
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
                    R = min(R_temp,operator.add(D_temp,data[i-1]))                    
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
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN SURFACE PROPER_PLATEAU
def min_surface_proper_plateau(data):
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
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    R = min(R_temp,operator.add(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN SURFACE INCREASING_SEQUENCE
def min_surface_increasing_sequence(data):
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
                    C = operator.add(operator.add(D_temp,data[i-1]),data[i])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,data[i]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    C = float('inf')                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN SURFACE PLATEAU
def min_surface_plateau(data):
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
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = 0                    
                    R = min(R_temp,operator.add(D_temp,data[i-1]))                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    R = min(R_temp,operator.add(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN SURFACE STRICTLY_INCREASING_SEQUENCE
def min_surface_strictly_increasing_sequence(data):
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
                    C = operator.add(operator.add(D_temp,data[i-1]),data[i])                    
                    D = 0                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = operator.add(C_temp,operator.add(D_temp,data[i]))                    
                    D = 0                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('inf')                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('inf')                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
    return min(R,C)    

# MIN SURFACE VALLEY
def min_surface_valley(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = operator.add(D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,data[i-1]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = float('inf')                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN SURFACE PROPER_PLAIN
def min_surface_proper_plain(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    R = min(R_temp,operator.add(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN SURFACE ZIGZAG
def min_surface_zigzag(data):
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
                if currentState == 'a':                
                    currentState = 'a'                    
                elif currentState == 'c':                
                    C = float('inf')                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 'a'                    
                elif currentState == 'b':                
                    C = operator.add(D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 'c'                    
                elif currentState == 'e':                
                    D = 0                    
                    currentState = 'a'                    
                elif currentState == 'd':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'e'                    
                elif currentState == 'f':                
                    C = operator.add(C_temp,operator.add(D_temp,data[i-1]))                    
                    D = 0                    
                    currentState = 'c'                    
                elif currentState == 's':                
                    currentState = 'a'                    
            elif data[i] < data[i-1]:            
                if currentState == 'a':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'b'                    
                elif currentState == 'c':                
                    C = operator.add(C_temp,operator.add(D_temp,data[i-1]))                    
                    D = 0                    
                    currentState = 'f'                    
                elif currentState == 'b':                
                    currentState = 'd'                    
                elif currentState == 'e':                
                    C = operator.add(D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 'f'                    
                elif currentState == 'd':                
                    currentState = 'd'                    
                elif currentState == 'f':                
                    C = float('inf')                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 'd'                    
                elif currentState == 's':                
                    currentState = 'd'                    
            elif data[i] == data[i-1]:            
                if currentState == 'a':                
                    currentState = 's'                    
                elif currentState == 'c':                
                    C = float('inf')                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
                elif currentState == 'b':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 'e':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 'd':                
                    currentState = 's'                    
                elif currentState == 'f':                
                    C = float('inf')                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
                elif currentState == 's':                
                    currentState = 's'                    
    return min(R,C)    

# MIN SURFACE INFLEXION
def min_surface_inflexion(data):
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
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    R = min(R_temp,operator.add(D_temp,data[i-1]))                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 't'                    
                elif currentState == 'r':                
                    D = 0                    
                    R = min(R_temp,operator.add(D_temp,data[i-1]))                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN SURFACE DECREASING_SEQUENCE
def min_surface_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 't':                
                    C = float('inf')                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    C = operator.add(operator.add(D_temp,data[i-1]),data[i])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,data[i]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
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
                    D = operator.add(D_temp,data[i-1])                    
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
                    C = operator.add(D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,data[i-1]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN SURFACE DIP_ON_INCREASING_SEQUENCE
def min_surface_dip_on_increasing_sequence(data):
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
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'v'                    
                elif currentState == 't':                
                    currentState = 't'                    
                elif currentState == 'v':                
                    D = 0                    
                    R = min(R_temp,operator.add(D_temp,data[i-1]))                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'v':                
                    D = 0                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    currentState = 's'                    
                elif currentState == 'v':                
                    D = 0                    
                    currentState = 's'                    
    return min(R,C)    

# MIN SURFACE DECREASING_TERRACE
def min_surface_decreasing_terrace(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    R = min(R_temp,operator.add(D_temp,data[i-1]))                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN SURFACE GORGE
def min_surface_gorge(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = operator.add(D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,data[i-1]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 'u':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = float('inf')                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'u':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

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
                    R = min(R_temp,operator.add(operator.add(D_temp,data[i-1]),data[i]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return min(R,C)    

# MIN SURFACE PLAIN
def min_surface_plain(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = 0                    
                    R = min(R_temp,operator.add(D_temp,data[i-1]))                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    R = min(R_temp,operator.add(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN SURFACE STEADY
def min_surface_steady(data):
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
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    D = 0                    
                    R = min(R_temp,operator.add(operator.add(D_temp,data[i-1]),data[i]))                    
                    currentState = 's'                    
    return min(R,C)    

# MIN SURFACE SUMMIT
def min_surface_summit(data):
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
                    C = operator.add(D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 'u':                
                    D = operator.add(D_temp,data[i-1])                    
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
                    C = operator.add(D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,data[i-1]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'u':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN SURFACE DECREASING
def min_surface_decreasing(data):
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
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    D = 0                    
                    R = min(R_temp,operator.add(operator.add(D_temp,data[i-1]),data[i]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return min(R,C)    

# MIN SURFACE STEADY_SEQUENCE
def min_surface_steady_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('inf')                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('inf')                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    C = operator.add(operator.add(D_temp,data[i-1]),data[i])                    
                    D = 0                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = operator.add(C_temp,operator.add(D_temp,data[i]))                    
                    D = 0                    
                    currentState = 'r'                    
    return min(R,C)    

# ----- MIN ONE -----
# MIN ONE BUMP_ON_DECREASING_SEQUENCE
def min_one_bump_on_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 1                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = max(D_temp,0)                    
                    currentState = 'u'                    
                elif currentState == 'v':                
                    D = 1                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = max(D_temp,0)                    
                    currentState = 'v'                    
                elif currentState == 't':                
                    currentState = 't'                    
                elif currentState == 'v':                
                    D = 1                    
                    R = min(R_temp,max(D_temp,0))                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 1                    
                    currentState = 's'                    
                elif currentState == 't':                
                    currentState = 's'                    
                elif currentState == 'v':                
                    D = 1                    
                    currentState = 's'                    
    return min(R,C)    

# MIN ONE STRICTLY_DECREASING_SEQUENCE
def min_one_strictly_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 1                    
                    D = 1                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    C = max(max(D_temp,0),data[i])                    
                    D = 1                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = max(C_temp,max(D_temp,data[i]))                    
                    D = 1                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 1                    
                    D = 1                    
                    R = min(R_temp,C_temp)                    
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

# MIN ONE PROPER_PLATEAU
def min_one_proper_plateau(data):
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
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 1                    
                    R = min(R_temp,max(D_temp,0))                    
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

# MIN ONE INCREASING_SEQUENCE
def min_one_increasing_sequence(data):
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
                    C = max(max(D_temp,0),data[i])                    
                    D = 1                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,data[i]))                    
                    D = 1                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    C = 1                    
                    D = 1                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN ONE PLATEAU
def min_one_plateau(data):
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
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = 1                    
                    R = min(R_temp,max(D_temp,0))                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 1                    
                    R = min(R_temp,max(D_temp,0))                    
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

# MIN ONE STRICTLY_INCREASING_SEQUENCE
def min_one_strictly_increasing_sequence(data):
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
                    C = max(max(D_temp,0),data[i])                    
                    D = 1                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = max(C_temp,max(D_temp,data[i]))                    
                    D = 1                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 1                    
                    D = 1                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 1                    
                    D = 1                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
    return min(R,C)    

# MIN ONE VALLEY
def min_one_valley(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = max(D_temp,0)                    
                    D = 1                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,0))                    
                    D = 1                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
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

# MIN ONE PROPER_PLAIN
def min_one_proper_plain(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 1                    
                    R = min(R_temp,max(D_temp,0))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 1                    
                    currentState = 'r'                    
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

# MIN ONE ZIGZAG
def min_one_zigzag(data):
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
                if currentState == 'a':                
                    currentState = 'a'                    
                elif currentState == 'c':                
                    C = 1                    
                    D = 1                    
                    R = min(R_temp,C_temp)                    
                    currentState = 'a'                    
                elif currentState == 'b':                
                    C = max(D_temp,0)                    
                    D = 1                    
                    currentState = 'c'                    
                elif currentState == 'e':                
                    D = 1                    
                    currentState = 'a'                    
                elif currentState == 'd':                
                    D = max(D_temp,0)                    
                    currentState = 'e'                    
                elif currentState == 'f':                
                    C = max(C_temp,max(D_temp,0))                    
                    D = 1                    
                    currentState = 'c'                    
                elif currentState == 's':                
                    currentState = 'a'                    
            elif data[i] < data[i-1]:            
                if currentState == 'a':                
                    D = max(D_temp,0)                    
                    currentState = 'b'                    
                elif currentState == 'c':                
                    C = max(C_temp,max(D_temp,0))                    
                    D = 1                    
                    currentState = 'f'                    
                elif currentState == 'b':                
                    currentState = 'd'                    
                elif currentState == 'e':                
                    C = max(D_temp,0)                    
                    D = 1                    
                    currentState = 'f'                    
                elif currentState == 'd':                
                    currentState = 'd'                    
                elif currentState == 'f':                
                    C = 1                    
                    D = 1                    
                    R = min(R_temp,C_temp)                    
                    currentState = 'd'                    
                elif currentState == 's':                
                    currentState = 'd'                    
            elif data[i] == data[i-1]:            
                if currentState == 'a':                
                    currentState = 's'                    
                elif currentState == 'c':                
                    C = 1                    
                    D = 1                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
                elif currentState == 'b':                
                    D = 1                    
                    currentState = 's'                    
                elif currentState == 'e':                
                    D = 1                    
                    currentState = 's'                    
                elif currentState == 'd':                
                    currentState = 's'                    
                elif currentState == 'f':                
                    C = 1                    
                    D = 1                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
                elif currentState == 's':                
                    currentState = 's'                    
    return min(R,C)    

# MIN ONE INFLEXION
def min_one_inflexion(data):
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
                    D = 1                    
                    R = min(R_temp,max(D_temp,0))                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 't'                    
                elif currentState == 'r':                
                    D = 1                    
                    R = min(R_temp,max(D_temp,0))                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = max(D_temp,0)                    
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

# MIN ONE DECREASING_SEQUENCE
def min_one_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 't':                
                    C = 1                    
                    D = 1                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    C = max(max(D_temp,0),data[i])                    
                    D = 1                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,data[i]))                    
                    D = 1                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = max(D_temp,data[i])                    
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

# MIN ONE DIP_ON_INCREASING_SEQUENCE
def min_one_dip_on_increasing_sequence(data):
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
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = max(D_temp,0)                    
                    currentState = 'v'                    
                elif currentState == 't':                
                    currentState = 't'                    
                elif currentState == 'v':                
                    D = 1                    
                    R = min(R_temp,max(D_temp,0))                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 1                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = max(D_temp,0)                    
                    currentState = 'u'                    
                elif currentState == 'v':                
                    D = 1                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 1                    
                    currentState = 's'                    
                elif currentState == 't':                
                    currentState = 's'                    
                elif currentState == 'v':                
                    D = 1                    
                    currentState = 's'                    
    return min(R,C)    

# MIN ONE DECREASING_TERRACE
def min_one_decreasing_terrace(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 1                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 1                    
                    R = min(R_temp,max(D_temp,0))                    
                    currentState = 'r'                    
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

# MIN ONE GORGE
def min_one_gorge(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = max(D_temp,0)                    
                    D = 1                    
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = 1                    
                    currentState = 's'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,0))                    
                    D = 1                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = max(D_temp,0)                    
                    currentState = 'r'                    
                elif currentState == 'u':                
                    D = max(D_temp,0)                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = 1                    
                    D = 1                    
                    R = min(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,0)                    
                    currentState = 'u'                    
                elif currentState == 'u':                
                    D = max(D_temp,0)                    
                    currentState = 'u'                    
                elif currentState == 't':                
                    D = max(D_temp,0)                    
                    currentState = 't'                    
    return min(R,C)    

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
                    R = min(R_temp,max(max(D_temp,0),data[i]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return min(R,C)    

# MIN ONE PLAIN
def min_one_plain(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = 1                    
                    R = min(R_temp,max(D_temp,0))                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 1                    
                    R = min(R_temp,max(D_temp,0))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 1                    
                    currentState = 'r'                    
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

# MIN ONE STEADY
def min_one_steady(data):
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
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    D = 1                    
                    R = min(R_temp,max(max(D_temp,0),data[i]))                    
                    currentState = 's'                    
    return min(R,C)    

# MIN ONE SUMMIT
def min_one_summit(data):
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
                    C = max(D_temp,0)                    
                    D = 1                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = max(D_temp,0)                    
                    currentState = 'r'                    
                elif currentState == 'u':                
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
                elif currentState == 'u':                
                    D = 1                    
                    currentState = 's'                    
                elif currentState == 't':                
                    C = max(C_temp,max(D_temp,0))                    
                    D = 1                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = max(D_temp,0)                    
                    currentState = 'u'                    
                elif currentState == 'u':                
                    D = max(D_temp,0)                    
                    currentState = 'u'                    
                elif currentState == 't':                
                    D = max(D_temp,0)                    
                    currentState = 't'                    
    return min(R,C)    

# MIN ONE DECREASING
def min_one_decreasing(data):
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
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    D = 1                    
                    R = min(R_temp,max(max(D_temp,0),data[i]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return min(R,C)    

# MIN ONE STEADY_SEQUENCE
def min_one_steady_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 1                    
                    D = 1                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = 1                    
                    D = 1                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    C = max(max(D_temp,0),data[i])                    
                    D = 1                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = max(C_temp,max(D_temp,data[i]))                    
                    D = 1                    
                    currentState = 'r'                    
    return min(R,C)    

# ----- MIN WIDTH -----
# MIN WIDTH BUMP_ON_DECREASING_SEQUENCE
def min_width_bump_on_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'u'                    
                elif currentState == 'v':                
                    D = 0                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'v'                    
                elif currentState == 't':                
                    currentState = 't'                    
                elif currentState == 'v':                
                    D = 0                    
                    R = min(R_temp,operator.add(D_temp,1))                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    currentState = 's'                    
                elif currentState == 'v':                
                    D = 0                    
                    currentState = 's'                    
    return min(R,C)    

# MIN WIDTH STRICTLY_DECREASING_SEQUENCE
def min_width_strictly_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = len(data)                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    C = operator.add(operator.add(D_temp,1),1)                    
                    D = 0                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = operator.add(C_temp,operator.add(D_temp,1))                    
                    D = 0                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = len(data)                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
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

# MIN WIDTH PROPER_PLATEAU
def min_width_proper_plateau(data):
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
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    R = min(R_temp,operator.add(D_temp,1))                    
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

# MIN WIDTH INCREASING_SEQUENCE
def min_width_increasing_sequence(data):
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
                    C = operator.add(operator.add(D_temp,1),1)                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,1))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    C = len(data)                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,1)                    
                    currentState = 't'                    
    return min(R,C)    

# MIN WIDTH PLATEAU
def min_width_plateau(data):
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
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = 0                    
                    R = min(R_temp,operator.add(D_temp,1))                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    R = min(R_temp,operator.add(D_temp,1))                    
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

# MIN WIDTH STRICTLY_INCREASING_SEQUENCE
def min_width_strictly_increasing_sequence(data):
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
                    C = operator.add(operator.add(D_temp,1),1)                    
                    D = 0                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = operator.add(C_temp,operator.add(D_temp,1))                    
                    D = 0                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = len(data)                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = len(data)                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
    return min(R,C)    

# MIN WIDTH VALLEY
def min_width_valley(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = operator.add(D_temp,1)                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,1))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
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

# MIN WIDTH PROPER_PLAIN
def min_width_proper_plain(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    R = min(R_temp,operator.add(D_temp,1))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    currentState = 'r'                    
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

# MIN WIDTH ZIGZAG
def min_width_zigzag(data):
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
                if currentState == 'a':                
                    currentState = 'a'                    
                elif currentState == 'c':                
                    C = len(data)                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 'a'                    
                elif currentState == 'b':                
                    C = operator.add(D_temp,1)                    
                    D = 0                    
                    currentState = 'c'                    
                elif currentState == 'e':                
                    D = 0                    
                    currentState = 'a'                    
                elif currentState == 'd':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'e'                    
                elif currentState == 'f':                
                    C = operator.add(C_temp,operator.add(D_temp,1))                    
                    D = 0                    
                    currentState = 'c'                    
                elif currentState == 's':                
                    currentState = 'a'                    
            elif data[i] < data[i-1]:            
                if currentState == 'a':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'b'                    
                elif currentState == 'c':                
                    C = operator.add(C_temp,operator.add(D_temp,1))                    
                    D = 0                    
                    currentState = 'f'                    
                elif currentState == 'b':                
                    currentState = 'd'                    
                elif currentState == 'e':                
                    C = operator.add(D_temp,1)                    
                    D = 0                    
                    currentState = 'f'                    
                elif currentState == 'd':                
                    currentState = 'd'                    
                elif currentState == 'f':                
                    C = len(data)                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 'd'                    
                elif currentState == 's':                
                    currentState = 'd'                    
            elif data[i] == data[i-1]:            
                if currentState == 'a':                
                    currentState = 's'                    
                elif currentState == 'c':                
                    C = len(data)                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
                elif currentState == 'b':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 'e':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 'd':                
                    currentState = 's'                    
                elif currentState == 'f':                
                    C = len(data)                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
                elif currentState == 's':                
                    currentState = 's'                    
    return min(R,C)    

# MIN WIDTH INFLEXION
def min_width_inflexion(data):
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
                    D = 0                    
                    R = min(R_temp,operator.add(D_temp,1))                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 't'                    
                elif currentState == 'r':                
                    D = 0                    
                    R = min(R_temp,operator.add(D_temp,1))                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,1)                    
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

# MIN WIDTH DECREASING_SEQUENCE
def min_width_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 't':                
                    C = len(data)                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    C = operator.add(operator.add(D_temp,1),1)                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,1))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
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

# MIN WIDTH DIP_ON_INCREASING_SEQUENCE
def min_width_dip_on_increasing_sequence(data):
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
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'v'                    
                elif currentState == 't':                
                    currentState = 't'                    
                elif currentState == 'v':                
                    D = 0                    
                    R = min(R_temp,operator.add(D_temp,1))                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'u'                    
                elif currentState == 'v':                
                    D = 0                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    currentState = 's'                    
                elif currentState == 'v':                
                    D = 0                    
                    currentState = 's'                    
    return min(R,C)    

# MIN WIDTH DECREASING_TERRACE
def min_width_decreasing_terrace(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    R = min(R_temp,operator.add(D_temp,1))                    
                    currentState = 'r'                    
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

# MIN WIDTH GORGE
def min_width_gorge(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = operator.add(D_temp,1)                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,1))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'r'                    
                elif currentState == 'u':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = len(data)                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'u'                    
                elif currentState == 'u':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'u'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,1)                    
                    currentState = 't'                    
    return min(R,C)    

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
                    R = min(R_temp,operator.add(operator.add(D_temp,1),1))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return min(R,C)    

# MIN WIDTH PLAIN
def min_width_plain(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = 0                    
                    R = min(R_temp,operator.add(D_temp,1))                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    R = min(R_temp,operator.add(D_temp,1))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    currentState = 'r'                    
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

# MIN WIDTH STEADY
def min_width_steady(data):
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
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    D = 0                    
                    R = min(R_temp,operator.add(operator.add(D_temp,1),1))                    
                    currentState = 's'                    
    return min(R,C)    

# MIN WIDTH SUMMIT
def min_width_summit(data):
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
                    C = operator.add(D_temp,1)                    
                    D = 0                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'r'                    
                elif currentState == 'u':                
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
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    C = operator.add(C_temp,operator.add(D_temp,1))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'u'                    
                elif currentState == 'u':                
                    D = operator.add(D_temp,1)                    
                    currentState = 'u'                    
                elif currentState == 't':                
                    D = operator.add(D_temp,1)                    
                    currentState = 't'                    
    return min(R,C)    

# MIN WIDTH DECREASING
def min_width_decreasing(data):
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
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    D = 0                    
                    R = min(R_temp,operator.add(operator.add(D_temp,1),1))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return min(R,C)    

# MIN WIDTH STEADY_SEQUENCE
def min_width_steady_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = len(data)                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = len(data)                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    C = operator.add(operator.add(D_temp,1),1)                    
                    D = 0                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = operator.add(C_temp,operator.add(D_temp,1))                    
                    D = 0                    
                    currentState = 'r'                    
    return min(R,C)    

# ----- MIN RANGE -----
# MIN RANGE BUMP_ON_DECREASING_SEQUENCE
def min_range_bump_on_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'v':                
                    D = 0                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'v'                    
                elif currentState == 't':                
                    currentState = 't'                    
                elif currentState == 'v':                
                    D = 0                    
                    R = min(R_temp,(D_temp,data[i-1]))                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    currentState = 's'                    
                elif currentState == 'v':                
                    D = 0                    
                    currentState = 's'                    
    return min(R,C)    

# MIN RANGE STRICTLY_DECREASING_SEQUENCE
def min_range_strictly_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('inf')                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    C = ((D_temp,data[i-1]),data[i])                    
                    D = 0                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = (C_temp,(D_temp,data[i]))                    
                    D = 0                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('inf')                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
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
                    R = min(R_temp,(D_temp,data[i-1]))                    
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
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN RANGE PROPER_PLATEAU
def min_range_proper_plateau(data):
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
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    R = min(R_temp,(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN RANGE INCREASING_SEQUENCE
def min_range_increasing_sequence(data):
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
                    C = ((D_temp,data[i-1]),data[i])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = (C_temp,(D_temp,data[i]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    C = float('inf')                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = (D_temp,data[i])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN RANGE PLATEAU
def min_range_plateau(data):
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
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = 0                    
                    R = min(R_temp,(D_temp,data[i-1]))                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    R = min(R_temp,(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN RANGE STRICTLY_INCREASING_SEQUENCE
def min_range_strictly_increasing_sequence(data):
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
                    C = ((D_temp,data[i-1]),data[i])                    
                    D = 0                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = (C_temp,(D_temp,data[i]))                    
                    D = 0                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('inf')                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('inf')                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
    return min(R,C)    

# MIN RANGE VALLEY
def min_range_valley(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = (D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = (C_temp,(D_temp,data[i-1]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = float('inf')                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN RANGE PROPER_PLAIN
def min_range_proper_plain(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    R = min(R_temp,(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN RANGE ZIGZAG
def min_range_zigzag(data):
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
                if currentState == 'a':                
                    currentState = 'a'                    
                elif currentState == 'c':                
                    C = float('inf')                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 'a'                    
                elif currentState == 'b':                
                    C = (D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 'c'                    
                elif currentState == 'e':                
                    D = 0                    
                    currentState = 'a'                    
                elif currentState == 'd':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'e'                    
                elif currentState == 'f':                
                    C = (C_temp,(D_temp,data[i-1]))                    
                    D = 0                    
                    currentState = 'c'                    
                elif currentState == 's':                
                    currentState = 'a'                    
            elif data[i] < data[i-1]:            
                if currentState == 'a':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'b'                    
                elif currentState == 'c':                
                    C = (C_temp,(D_temp,data[i-1]))                    
                    D = 0                    
                    currentState = 'f'                    
                elif currentState == 'b':                
                    currentState = 'd'                    
                elif currentState == 'e':                
                    C = (D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 'f'                    
                elif currentState == 'd':                
                    currentState = 'd'                    
                elif currentState == 'f':                
                    C = float('inf')                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 'd'                    
                elif currentState == 's':                
                    currentState = 'd'                    
            elif data[i] == data[i-1]:            
                if currentState == 'a':                
                    currentState = 's'                    
                elif currentState == 'c':                
                    C = float('inf')                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
                elif currentState == 'b':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 'e':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 'd':                
                    currentState = 's'                    
                elif currentState == 'f':                
                    C = float('inf')                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
                elif currentState == 's':                
                    currentState = 's'                    
    return min(R,C)    

# MIN RANGE INFLEXION
def min_range_inflexion(data):
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
                    D = (D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    R = min(R_temp,(D_temp,data[i-1]))                    
                    currentState = 'r'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 't'                    
                elif currentState == 'r':                
                    D = 0                    
                    R = min(R_temp,(D_temp,data[i-1]))                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN RANGE DECREASING_SEQUENCE
def min_range_decreasing_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 't':                
                    C = float('inf')                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    C = ((D_temp,data[i-1]),data[i])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = (C_temp,(D_temp,data[i]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
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
                    D = (D_temp,data[i-1])                    
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
                    C = (D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 't':                
                    C = (C_temp,(D_temp,data[i-1]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN RANGE DIP_ON_INCREASING_SEQUENCE
def min_range_dip_on_increasing_sequence(data):
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
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'v'                    
                elif currentState == 't':                
                    currentState = 't'                    
                elif currentState == 'v':                
                    D = 0                    
                    R = min(R_temp,(D_temp,data[i-1]))                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'v':                
                    D = 0                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    currentState = 's'                    
                elif currentState == 'v':                
                    D = 0                    
                    currentState = 's'                    
    return min(R,C)    

# MIN RANGE DECREASING_TERRACE
def min_range_decreasing_terrace(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    R = min(R_temp,(D_temp,data[i-1]))                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN RANGE GORGE
def min_range_gorge(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = (D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    C = (C_temp,(D_temp,data[i-1]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 'u':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 't':                
                    C = float('inf')                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'u':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

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
                    R = min(R_temp,((D_temp,data[i-1]),data[i]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return min(R,C)    

# MIN RANGE PLAIN
def min_range_plain(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = 0                    
                    R = min(R_temp,(D_temp,data[i-1]))                    
                    currentState = 's'                    
                elif currentState == 't':                
                    D = 0                    
                    R = min(R_temp,(D_temp,data[i-1]))                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 'r'                    
                elif currentState == 'r':                
                    currentState = 'r'                    
                elif currentState == 't':                
                    D = 0                    
                    currentState = 'r'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN RANGE STEADY
def min_range_steady(data):
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
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    D = 0                    
                    R = min(R_temp,((D_temp,data[i-1]),data[i]))                    
                    currentState = 's'                    
    return min(R,C)    

# MIN RANGE SUMMIT
def min_range_summit(data):
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
                    C = (D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'r'                    
                elif currentState == 'u':                
                    D = (D_temp,data[i-1])                    
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
                    C = (D_temp,data[i-1])                    
                    D = 0                    
                    currentState = 't'                    
                elif currentState == 'u':                
                    D = 0                    
                    currentState = 's'                    
                elif currentState == 't':                
                    C = (C_temp,(D_temp,data[i-1]))                    
                    D = 0                    
                    currentState = 't'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 'u':                
                    D = (D_temp,data[i-1])                    
                    currentState = 'u'                    
                elif currentState == 't':                
                    D = (D_temp,data[i-1])                    
                    currentState = 't'                    
    return min(R,C)    

# MIN RANGE DECREASING
def min_range_decreasing(data):
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
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    D = 0                    
                    R = min(R_temp,((D_temp,data[i-1]),data[i]))                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
    return min(R,C)    

# MIN RANGE STEADY_SEQUENCE
def min_range_steady_sequence(data):
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
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('inf')                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] < data[i-1]:            
                if currentState == 's':                
                    currentState = 's'                    
                elif currentState == 'r':                
                    C = float('inf')                    
                    D = 0                    
                    R = min(R_temp,C_temp)                    
                    currentState = 's'                    
            elif data[i] == data[i-1]:            
                if currentState == 's':                
                    C = ((D_temp,data[i-1]),data[i])                    
                    D = 0                    
                    currentState = 'r'                    
                elif currentState == 'r':                
                    C = (C_temp,(D_temp,data[i]))                    
                    D = 0                    
                    currentState = 'r'                    
    return min(R,C)    

