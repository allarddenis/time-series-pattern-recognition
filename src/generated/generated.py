# ----------------------------------------------------------------------------
# This file was auto-generated on 2017-11-27
# By Florine Cercle - Denis Allard
# Source code : https://github.com/allarddenis/time-series-pattern-recognition
# ----------------------------------------------------------------------------

import operator

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

