# Time series pattern recognition using generated python code

Generated python code analysing time series and extracting patterns from it.

The generated functions are based on a model created by some researchers (see [reseachers](https://arxiv.org/abs/1609.08925)). 

The model uses accumulators to extract aggregations on features of a pattern occurrences in a time series.

All function generated are based on a aggregator_feature_pattern model (see [models](#models)).

# Summary
1. [Models](#models)
2. [How to](#how-to)
3. [Contributors](#contributors)

# Models

## Patterns

Pattern name | Regex
------------ | -------------
bump_on_decreasing_sequence | >><>>
decreasing | >
increasing | <
decreasing_sequence | >(>|=)*>|>
decreasing_terrace | >=+>
dip_on_increasing_sequence | <<><<
gorge | (>\|(>(=\|>)*>))(<\|(<(=\|<)*<))
increasing_sequence | <(<\|=)*<\|<
increasing_terrace | <=+<
inflexion | <(<\|=)*>\|>(>\|=)*<
peak | <(=\|<)*(>\|=)*>
plain | >=*<
plateau | <=*>
proper_plain | >=+<
proper_plateau | <=+>
steady | =
steady_sequence | =+
strictly_increasing_sequence | <+
strictly_decreasing_sequence | >+
summit | (<\|(<(=\|<)*<))(>\|(>(=\|>)*>))
valley | >(=\|>)*(<\|=)*<
zigzag | (<>)+(<\|<>)\|(><)+(>\|><)

Example :

```
Data : [4,4,2,2,3,5,5,6,3,1,1,2,2,2,2,2,2,1]
Signature : =>=<<=<>>=<=====>

Peak regex : <(=|<)*(>|=)*>

Peak pattern occurrences : <<=<>> & <=====>
```

## Features

Name | Meaning
------------ | -------------
one | Identity feature
width | Width of a pattern occurrence
height | Height of a pattern occurrence
max | Largest value among items of a pattern occurrence
min | Lowest value among items of a pattern occurrence
surface | Surface of a pattern occurrence

## Aggregators

Name | Meaning
------------ | -------------
max | Largest value among features of pattern occurrences
min | Lowest value among features of pattern occurrences
sum | Sum of feature values of pattern occurrences

# How to

## How to generate functions

From **/src** execute the following command :

```
python generator.py    
```

This should generate **generated.py** file in **/src/generated**.

## How to test

From **/src** execute the following command :

```
python test.py    
```

This should output test results in command window.

## How to use

Just pick up the desired function from **/src/generated/generated.py**.

All generated functions are **standalone**. It means you can just copy-paste them and use it. But, don't forget to **import operator** in your file as the function **operator.add()** is used.

Data inputs are expected to be an integer array :

```python
data = [0,1,2,3,4,5,6,7,8,9]
```

Here is an example of a python file using only **min_min_increasing_sequence** function :

```python

import operator

data = [4,3,5,5,2,1,1,3,3,4,6,6,3,1,3,3]

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

print min_min_increasing_sequence(data) 
# supposed to print '1'  
```

# Contributors

- Florine Cercle
- Denis Allard