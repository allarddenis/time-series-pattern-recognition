# --------------------------------------------------
# This file was auto-generated on 2017-11-23
# By Florine Cercle - Denis Allard
# --------------------------------------------------

import operator

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

