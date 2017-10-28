# Time series pattern recognition using generated python code

Generated python code analysing time series and extracting patterns from it.

## Patterns

Pattern name | Regex
------------ | -------------
increasing | <
decreasing | >
increasing_sequence | <(<\|=)*<\|<
decreasing_sequence | >(>\|=)*>\|>
increasing_terrace | <=+<
decreasing_terrace | >=+>
summit | (<\|(<(=\|<)*<))(>\|(>(=\|>)*>))
gorge | (>\|(>(=\|>)*>))(<\|(<(=\|<)*<))
plateau | <=*>
plain | >=*<
proper_plateau | <=+>
proper_plain | >=+<
strictly_increasing_sequence | <+
strictly_decreasing_sequence | >+
peak | <(=\|<)*(>\|=)*>
valley | >(=\|>)*(<\|=)*<
inflexion | <(<\|=)*>\|>(>\|=)*<
steady | =
steady_sequence | =+
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

## How to generate functions

From **/src** execute the following command :

```
python code_generation.py    
```

This should generate **generated_functions.py** file.

## How to use generated functions

1. Once **generated_functions.py** file has been generated, import it in your python file :

```python
import generated_functions
```

2. Create or get your time series :

```python
import generated_functions

time_series_data = [4,4,2,2,3,5,5,6,3,1,1,2,2,2,2,2,2,1]
```

3. Use any generated function :

```python
import generated_functions

time_series_data = [4,4,2,2,3,5,5,6,3,1,1,2,2,2,2,2,2,1]

print 'peak one : '
print generated_functions.one_peak(raw_data)

print 'peak heights : '
print generated_functions.height_peak(raw_data)

print 'max peak height : '
print generated_functions.max_height_peak(raw_data)
```

# Contributors

- Florine Cercle
- Lisa Pasqualini
- Denis Allard