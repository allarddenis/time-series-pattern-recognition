# --------------------------------------------------
# This file was auto-generated on 2017-11-22
# By Florine Cercle - Denis Allard
# --------------------------------------------------

def min_width_peak(data):
    C = len(data)    
    D = 0    
    R = len(data)    
    currentState = 's'    
    for i in xrange(1,len(data)):    
        semantic = ''        
        if(i < len(data)):        
            if data[i] > data[i-1]:            
                C_temp = C                
                D_temp = D                
                R_temp = R                
                if currentState == 's':                
                    semantic = 'out'                    
                    currentState = 'r'                    
                if currentState == 'r':                
                    semantic = 'maybe_b'                    
                    currentState = 'r'                    
                if currentState == 't':                
                    semantic = 'out_a'                    
                    C = len(data)                    
                    currentState = 'r'                    
