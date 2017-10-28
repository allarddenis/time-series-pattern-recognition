# -------------------------------------------------- 
# This file was auto-generated on 2017-10-28
# By Florine Cercle - Lisa Pasqualini - Denis Allard
# -------------------------------------------------- 
 
from pattern import Pattern

# --------------------------------------------------------------------------- 
# PROPER_PLATEAU
# --------------------------------------------------------------------------- 

proper_plateau = Pattern('proper_plateau', '<=+>', 1, 1)

# --- proper_plateau features --- 
 
def one_proper_plateau(data): 
    matches = proper_plateau.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.one()) 
    return result 
def width_proper_plateau(data): 
    matches = proper_plateau.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.width()) 
    return result 
def range_proper_plateau(data): 
    matches = proper_plateau.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.range()) 
    return result 
def max_proper_plateau(data): 
    matches = proper_plateau.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.max()) 
    return result 
def min_proper_plateau(data): 
    matches = proper_plateau.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.min()) 
    return result 
def surface_proper_plateau(data): 
    matches = proper_plateau.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.surface()) 
    return result 

# --- proper_plateau aggregators --- 
 
def max_width_proper_plateau(data): 
    return max(width_proper_plateau(data)) 
def max_range_proper_plateau(data): 
    return max(range_proper_plateau(data)) 
def max_max_proper_plateau(data): 
    return max(max_proper_plateau(data)) 
def max_min_proper_plateau(data): 
    return max(min_proper_plateau(data)) 
def max_surface_proper_plateau(data): 
    return max(surface_proper_plateau(data)) 
def min_width_proper_plateau(data): 
    return min(width_proper_plateau(data)) 
def min_range_proper_plateau(data): 
    return min(range_proper_plateau(data)) 
def min_max_proper_plateau(data): 
    return min(max_proper_plateau(data)) 
def min_min_proper_plateau(data): 
    return min(min_proper_plateau(data)) 
def min_surface_proper_plateau(data): 
    return min(surface_proper_plateau(data)) 
def sum_width_proper_plateau(data): 
    return sum(width_proper_plateau(data)) 
def sum_range_proper_plateau(data): 
    return sum(range_proper_plateau(data)) 
def sum_max_proper_plateau(data): 
    return sum(max_proper_plateau(data)) 
def sum_min_proper_plateau(data): 
    return sum(min_proper_plateau(data)) 
def sum_surface_proper_plateau(data): 
    return sum(surface_proper_plateau(data)) 

# --------------------------------------------------------------------------- 
# ZIGZAG
# --------------------------------------------------------------------------- 

zigzag = Pattern('zigzag', '(<>)+(<|<>)|(><)+(>|><)', 1, 1)

# --- zigzag features --- 
 
def one_zigzag(data): 
    matches = zigzag.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.one()) 
    return result 
def width_zigzag(data): 
    matches = zigzag.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.width()) 
    return result 
def range_zigzag(data): 
    matches = zigzag.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.range()) 
    return result 
def max_zigzag(data): 
    matches = zigzag.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.max()) 
    return result 
def min_zigzag(data): 
    matches = zigzag.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.min()) 
    return result 
def surface_zigzag(data): 
    matches = zigzag.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.surface()) 
    return result 

# --- zigzag aggregators --- 
 
def max_width_zigzag(data): 
    return max(width_zigzag(data)) 
def max_range_zigzag(data): 
    return max(range_zigzag(data)) 
def max_max_zigzag(data): 
    return max(max_zigzag(data)) 
def max_min_zigzag(data): 
    return max(min_zigzag(data)) 
def max_surface_zigzag(data): 
    return max(surface_zigzag(data)) 
def min_width_zigzag(data): 
    return min(width_zigzag(data)) 
def min_range_zigzag(data): 
    return min(range_zigzag(data)) 
def min_max_zigzag(data): 
    return min(max_zigzag(data)) 
def min_min_zigzag(data): 
    return min(min_zigzag(data)) 
def min_surface_zigzag(data): 
    return min(surface_zigzag(data)) 
def sum_width_zigzag(data): 
    return sum(width_zigzag(data)) 
def sum_range_zigzag(data): 
    return sum(range_zigzag(data)) 
def sum_max_zigzag(data): 
    return sum(max_zigzag(data)) 
def sum_min_zigzag(data): 
    return sum(min_zigzag(data)) 
def sum_surface_zigzag(data): 
    return sum(surface_zigzag(data)) 

# --------------------------------------------------------------------------- 
# PLAIN
# --------------------------------------------------------------------------- 

plain = Pattern('plain', '>=*<', 1, 1)

# --- plain features --- 
 
def one_plain(data): 
    matches = plain.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.one()) 
    return result 
def width_plain(data): 
    matches = plain.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.width()) 
    return result 
def range_plain(data): 
    matches = plain.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.range()) 
    return result 
def max_plain(data): 
    matches = plain.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.max()) 
    return result 
def min_plain(data): 
    matches = plain.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.min()) 
    return result 
def surface_plain(data): 
    matches = plain.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.surface()) 
    return result 

# --- plain aggregators --- 
 
def max_width_plain(data): 
    return max(width_plain(data)) 
def max_range_plain(data): 
    return max(range_plain(data)) 
def max_max_plain(data): 
    return max(max_plain(data)) 
def max_min_plain(data): 
    return max(min_plain(data)) 
def max_surface_plain(data): 
    return max(surface_plain(data)) 
def min_width_plain(data): 
    return min(width_plain(data)) 
def min_range_plain(data): 
    return min(range_plain(data)) 
def min_max_plain(data): 
    return min(max_plain(data)) 
def min_min_plain(data): 
    return min(min_plain(data)) 
def min_surface_plain(data): 
    return min(surface_plain(data)) 
def sum_width_plain(data): 
    return sum(width_plain(data)) 
def sum_range_plain(data): 
    return sum(range_plain(data)) 
def sum_max_plain(data): 
    return sum(max_plain(data)) 
def sum_min_plain(data): 
    return sum(min_plain(data)) 
def sum_surface_plain(data): 
    return sum(surface_plain(data)) 

# --------------------------------------------------------------------------- 
# STEADY
# --------------------------------------------------------------------------- 

steady = Pattern('steady', '=', 0, 0)

# --- steady features --- 
 
def one_steady(data): 
    matches = steady.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.one()) 
    return result 
def width_steady(data): 
    matches = steady.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.width()) 
    return result 
def range_steady(data): 
    matches = steady.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.range()) 
    return result 
def max_steady(data): 
    matches = steady.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.max()) 
    return result 
def min_steady(data): 
    matches = steady.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.min()) 
    return result 
def surface_steady(data): 
    matches = steady.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.surface()) 
    return result 

# --- steady aggregators --- 
 
def max_width_steady(data): 
    return max(width_steady(data)) 
def max_range_steady(data): 
    return max(range_steady(data)) 
def max_max_steady(data): 
    return max(max_steady(data)) 
def max_min_steady(data): 
    return max(min_steady(data)) 
def max_surface_steady(data): 
    return max(surface_steady(data)) 
def min_width_steady(data): 
    return min(width_steady(data)) 
def min_range_steady(data): 
    return min(range_steady(data)) 
def min_max_steady(data): 
    return min(max_steady(data)) 
def min_min_steady(data): 
    return min(min_steady(data)) 
def min_surface_steady(data): 
    return min(surface_steady(data)) 
def sum_width_steady(data): 
    return sum(width_steady(data)) 
def sum_range_steady(data): 
    return sum(range_steady(data)) 
def sum_max_steady(data): 
    return sum(max_steady(data)) 
def sum_min_steady(data): 
    return sum(min_steady(data)) 
def sum_surface_steady(data): 
    return sum(surface_steady(data)) 

# --------------------------------------------------------------------------- 
# VALLEY
# --------------------------------------------------------------------------- 

valley = Pattern('valley', '>(=|>)*(<|=)*<', 1, 1)

# --- valley features --- 
 
def one_valley(data): 
    matches = valley.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.one()) 
    return result 
def width_valley(data): 
    matches = valley.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.width()) 
    return result 
def range_valley(data): 
    matches = valley.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.range()) 
    return result 
def max_valley(data): 
    matches = valley.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.max()) 
    return result 
def min_valley(data): 
    matches = valley.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.min()) 
    return result 
def surface_valley(data): 
    matches = valley.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.surface()) 
    return result 

# --- valley aggregators --- 
 
def max_width_valley(data): 
    return max(width_valley(data)) 
def max_range_valley(data): 
    return max(range_valley(data)) 
def max_max_valley(data): 
    return max(max_valley(data)) 
def max_min_valley(data): 
    return max(min_valley(data)) 
def max_surface_valley(data): 
    return max(surface_valley(data)) 
def min_width_valley(data): 
    return min(width_valley(data)) 
def min_range_valley(data): 
    return min(range_valley(data)) 
def min_max_valley(data): 
    return min(max_valley(data)) 
def min_min_valley(data): 
    return min(min_valley(data)) 
def min_surface_valley(data): 
    return min(surface_valley(data)) 
def sum_width_valley(data): 
    return sum(width_valley(data)) 
def sum_range_valley(data): 
    return sum(range_valley(data)) 
def sum_max_valley(data): 
    return sum(max_valley(data)) 
def sum_min_valley(data): 
    return sum(min_valley(data)) 
def sum_surface_valley(data): 
    return sum(surface_valley(data)) 

# --------------------------------------------------------------------------- 
# INFLEXION
# --------------------------------------------------------------------------- 

inflexion = Pattern('inflexion', '<(<|=)*>|>(>|=)*<', 1, 1)

# --- inflexion features --- 
 
def one_inflexion(data): 
    matches = inflexion.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.one()) 
    return result 
def width_inflexion(data): 
    matches = inflexion.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.width()) 
    return result 
def range_inflexion(data): 
    matches = inflexion.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.range()) 
    return result 
def max_inflexion(data): 
    matches = inflexion.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.max()) 
    return result 
def min_inflexion(data): 
    matches = inflexion.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.min()) 
    return result 
def surface_inflexion(data): 
    matches = inflexion.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.surface()) 
    return result 

# --- inflexion aggregators --- 
 
def max_width_inflexion(data): 
    return max(width_inflexion(data)) 
def max_range_inflexion(data): 
    return max(range_inflexion(data)) 
def max_max_inflexion(data): 
    return max(max_inflexion(data)) 
def max_min_inflexion(data): 
    return max(min_inflexion(data)) 
def max_surface_inflexion(data): 
    return max(surface_inflexion(data)) 
def min_width_inflexion(data): 
    return min(width_inflexion(data)) 
def min_range_inflexion(data): 
    return min(range_inflexion(data)) 
def min_max_inflexion(data): 
    return min(max_inflexion(data)) 
def min_min_inflexion(data): 
    return min(min_inflexion(data)) 
def min_surface_inflexion(data): 
    return min(surface_inflexion(data)) 
def sum_width_inflexion(data): 
    return sum(width_inflexion(data)) 
def sum_range_inflexion(data): 
    return sum(range_inflexion(data)) 
def sum_max_inflexion(data): 
    return sum(max_inflexion(data)) 
def sum_min_inflexion(data): 
    return sum(min_inflexion(data)) 
def sum_surface_inflexion(data): 
    return sum(surface_inflexion(data)) 

# --------------------------------------------------------------------------- 
# INCREASING_SEQUENCE
# --------------------------------------------------------------------------- 

increasing_sequence = Pattern('increasing_sequence', '<(<|=)*<|<', 0, 0)

# --- increasing_sequence features --- 
 
def one_increasing_sequence(data): 
    matches = increasing_sequence.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.one()) 
    return result 
def width_increasing_sequence(data): 
    matches = increasing_sequence.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.width()) 
    return result 
def range_increasing_sequence(data): 
    matches = increasing_sequence.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.range()) 
    return result 
def max_increasing_sequence(data): 
    matches = increasing_sequence.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.max()) 
    return result 
def min_increasing_sequence(data): 
    matches = increasing_sequence.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.min()) 
    return result 
def surface_increasing_sequence(data): 
    matches = increasing_sequence.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.surface()) 
    return result 

# --- increasing_sequence aggregators --- 
 
def max_width_increasing_sequence(data): 
    return max(width_increasing_sequence(data)) 
def max_range_increasing_sequence(data): 
    return max(range_increasing_sequence(data)) 
def max_max_increasing_sequence(data): 
    return max(max_increasing_sequence(data)) 
def max_min_increasing_sequence(data): 
    return max(min_increasing_sequence(data)) 
def max_surface_increasing_sequence(data): 
    return max(surface_increasing_sequence(data)) 
def min_width_increasing_sequence(data): 
    return min(width_increasing_sequence(data)) 
def min_range_increasing_sequence(data): 
    return min(range_increasing_sequence(data)) 
def min_max_increasing_sequence(data): 
    return min(max_increasing_sequence(data)) 
def min_min_increasing_sequence(data): 
    return min(min_increasing_sequence(data)) 
def min_surface_increasing_sequence(data): 
    return min(surface_increasing_sequence(data)) 
def sum_width_increasing_sequence(data): 
    return sum(width_increasing_sequence(data)) 
def sum_range_increasing_sequence(data): 
    return sum(range_increasing_sequence(data)) 
def sum_max_increasing_sequence(data): 
    return sum(max_increasing_sequence(data)) 
def sum_min_increasing_sequence(data): 
    return sum(min_increasing_sequence(data)) 
def sum_surface_increasing_sequence(data): 
    return sum(surface_increasing_sequence(data)) 

# --------------------------------------------------------------------------- 
# STRICTLY_INCREASING_SEQUENCE
# --------------------------------------------------------------------------- 

strictly_increasing_sequence = Pattern('strictly_increasing_sequence', '<+', 0, 0)

# --- strictly_increasing_sequence features --- 
 
def one_strictly_increasing_sequence(data): 
    matches = strictly_increasing_sequence.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.one()) 
    return result 
def width_strictly_increasing_sequence(data): 
    matches = strictly_increasing_sequence.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.width()) 
    return result 
def range_strictly_increasing_sequence(data): 
    matches = strictly_increasing_sequence.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.range()) 
    return result 
def max_strictly_increasing_sequence(data): 
    matches = strictly_increasing_sequence.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.max()) 
    return result 
def min_strictly_increasing_sequence(data): 
    matches = strictly_increasing_sequence.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.min()) 
    return result 
def surface_strictly_increasing_sequence(data): 
    matches = strictly_increasing_sequence.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.surface()) 
    return result 

# --- strictly_increasing_sequence aggregators --- 
 
def max_width_strictly_increasing_sequence(data): 
    return max(width_strictly_increasing_sequence(data)) 
def max_range_strictly_increasing_sequence(data): 
    return max(range_strictly_increasing_sequence(data)) 
def max_max_strictly_increasing_sequence(data): 
    return max(max_strictly_increasing_sequence(data)) 
def max_min_strictly_increasing_sequence(data): 
    return max(min_strictly_increasing_sequence(data)) 
def max_surface_strictly_increasing_sequence(data): 
    return max(surface_strictly_increasing_sequence(data)) 
def min_width_strictly_increasing_sequence(data): 
    return min(width_strictly_increasing_sequence(data)) 
def min_range_strictly_increasing_sequence(data): 
    return min(range_strictly_increasing_sequence(data)) 
def min_max_strictly_increasing_sequence(data): 
    return min(max_strictly_increasing_sequence(data)) 
def min_min_strictly_increasing_sequence(data): 
    return min(min_strictly_increasing_sequence(data)) 
def min_surface_strictly_increasing_sequence(data): 
    return min(surface_strictly_increasing_sequence(data)) 
def sum_width_strictly_increasing_sequence(data): 
    return sum(width_strictly_increasing_sequence(data)) 
def sum_range_strictly_increasing_sequence(data): 
    return sum(range_strictly_increasing_sequence(data)) 
def sum_max_strictly_increasing_sequence(data): 
    return sum(max_strictly_increasing_sequence(data)) 
def sum_min_strictly_increasing_sequence(data): 
    return sum(min_strictly_increasing_sequence(data)) 
def sum_surface_strictly_increasing_sequence(data): 
    return sum(surface_strictly_increasing_sequence(data)) 

# --------------------------------------------------------------------------- 
# STEADY_SEQUENCE
# --------------------------------------------------------------------------- 

steady_sequence = Pattern('steady_sequence', '=+', 0, 0)

# --- steady_sequence features --- 
 
def one_steady_sequence(data): 
    matches = steady_sequence.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.one()) 
    return result 
def width_steady_sequence(data): 
    matches = steady_sequence.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.width()) 
    return result 
def range_steady_sequence(data): 
    matches = steady_sequence.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.range()) 
    return result 
def max_steady_sequence(data): 
    matches = steady_sequence.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.max()) 
    return result 
def min_steady_sequence(data): 
    matches = steady_sequence.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.min()) 
    return result 
def surface_steady_sequence(data): 
    matches = steady_sequence.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.surface()) 
    return result 

# --- steady_sequence aggregators --- 
 
def max_width_steady_sequence(data): 
    return max(width_steady_sequence(data)) 
def max_range_steady_sequence(data): 
    return max(range_steady_sequence(data)) 
def max_max_steady_sequence(data): 
    return max(max_steady_sequence(data)) 
def max_min_steady_sequence(data): 
    return max(min_steady_sequence(data)) 
def max_surface_steady_sequence(data): 
    return max(surface_steady_sequence(data)) 
def min_width_steady_sequence(data): 
    return min(width_steady_sequence(data)) 
def min_range_steady_sequence(data): 
    return min(range_steady_sequence(data)) 
def min_max_steady_sequence(data): 
    return min(max_steady_sequence(data)) 
def min_min_steady_sequence(data): 
    return min(min_steady_sequence(data)) 
def min_surface_steady_sequence(data): 
    return min(surface_steady_sequence(data)) 
def sum_width_steady_sequence(data): 
    return sum(width_steady_sequence(data)) 
def sum_range_steady_sequence(data): 
    return sum(range_steady_sequence(data)) 
def sum_max_steady_sequence(data): 
    return sum(max_steady_sequence(data)) 
def sum_min_steady_sequence(data): 
    return sum(min_steady_sequence(data)) 
def sum_surface_steady_sequence(data): 
    return sum(surface_steady_sequence(data)) 

# --------------------------------------------------------------------------- 
# SUMMIT
# --------------------------------------------------------------------------- 

summit = Pattern('summit', '(<|(<(=|<)*<))(>|(>(=|>)*>))', 1, 1)

# --- summit features --- 
 
def one_summit(data): 
    matches = summit.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.one()) 
    return result 
def width_summit(data): 
    matches = summit.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.width()) 
    return result 
def range_summit(data): 
    matches = summit.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.range()) 
    return result 
def max_summit(data): 
    matches = summit.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.max()) 
    return result 
def min_summit(data): 
    matches = summit.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.min()) 
    return result 
def surface_summit(data): 
    matches = summit.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.surface()) 
    return result 

# --- summit aggregators --- 
 
def max_width_summit(data): 
    return max(width_summit(data)) 
def max_range_summit(data): 
    return max(range_summit(data)) 
def max_max_summit(data): 
    return max(max_summit(data)) 
def max_min_summit(data): 
    return max(min_summit(data)) 
def max_surface_summit(data): 
    return max(surface_summit(data)) 
def min_width_summit(data): 
    return min(width_summit(data)) 
def min_range_summit(data): 
    return min(range_summit(data)) 
def min_max_summit(data): 
    return min(max_summit(data)) 
def min_min_summit(data): 
    return min(min_summit(data)) 
def min_surface_summit(data): 
    return min(surface_summit(data)) 
def sum_width_summit(data): 
    return sum(width_summit(data)) 
def sum_range_summit(data): 
    return sum(range_summit(data)) 
def sum_max_summit(data): 
    return sum(max_summit(data)) 
def sum_min_summit(data): 
    return sum(min_summit(data)) 
def sum_surface_summit(data): 
    return sum(surface_summit(data)) 

# --------------------------------------------------------------------------- 
# DECREASING_SEQUENCE
# --------------------------------------------------------------------------- 

decreasing_sequence = Pattern('decreasing_sequence', '>(>|=)*>|>', 0, 0)

# --- decreasing_sequence features --- 
 
def one_decreasing_sequence(data): 
    matches = decreasing_sequence.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.one()) 
    return result 
def width_decreasing_sequence(data): 
    matches = decreasing_sequence.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.width()) 
    return result 
def range_decreasing_sequence(data): 
    matches = decreasing_sequence.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.range()) 
    return result 
def max_decreasing_sequence(data): 
    matches = decreasing_sequence.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.max()) 
    return result 
def min_decreasing_sequence(data): 
    matches = decreasing_sequence.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.min()) 
    return result 
def surface_decreasing_sequence(data): 
    matches = decreasing_sequence.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.surface()) 
    return result 

# --- decreasing_sequence aggregators --- 
 
def max_width_decreasing_sequence(data): 
    return max(width_decreasing_sequence(data)) 
def max_range_decreasing_sequence(data): 
    return max(range_decreasing_sequence(data)) 
def max_max_decreasing_sequence(data): 
    return max(max_decreasing_sequence(data)) 
def max_min_decreasing_sequence(data): 
    return max(min_decreasing_sequence(data)) 
def max_surface_decreasing_sequence(data): 
    return max(surface_decreasing_sequence(data)) 
def min_width_decreasing_sequence(data): 
    return min(width_decreasing_sequence(data)) 
def min_range_decreasing_sequence(data): 
    return min(range_decreasing_sequence(data)) 
def min_max_decreasing_sequence(data): 
    return min(max_decreasing_sequence(data)) 
def min_min_decreasing_sequence(data): 
    return min(min_decreasing_sequence(data)) 
def min_surface_decreasing_sequence(data): 
    return min(surface_decreasing_sequence(data)) 
def sum_width_decreasing_sequence(data): 
    return sum(width_decreasing_sequence(data)) 
def sum_range_decreasing_sequence(data): 
    return sum(range_decreasing_sequence(data)) 
def sum_max_decreasing_sequence(data): 
    return sum(max_decreasing_sequence(data)) 
def sum_min_decreasing_sequence(data): 
    return sum(min_decreasing_sequence(data)) 
def sum_surface_decreasing_sequence(data): 
    return sum(surface_decreasing_sequence(data)) 

# --------------------------------------------------------------------------- 
# PLATEAU
# --------------------------------------------------------------------------- 

plateau = Pattern('plateau', '<=*>', 1, 1)

# --- plateau features --- 
 
def one_plateau(data): 
    matches = plateau.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.one()) 
    return result 
def width_plateau(data): 
    matches = plateau.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.width()) 
    return result 
def range_plateau(data): 
    matches = plateau.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.range()) 
    return result 
def max_plateau(data): 
    matches = plateau.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.max()) 
    return result 
def min_plateau(data): 
    matches = plateau.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.min()) 
    return result 
def surface_plateau(data): 
    matches = plateau.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.surface()) 
    return result 

# --- plateau aggregators --- 
 
def max_width_plateau(data): 
    return max(width_plateau(data)) 
def max_range_plateau(data): 
    return max(range_plateau(data)) 
def max_max_plateau(data): 
    return max(max_plateau(data)) 
def max_min_plateau(data): 
    return max(min_plateau(data)) 
def max_surface_plateau(data): 
    return max(surface_plateau(data)) 
def min_width_plateau(data): 
    return min(width_plateau(data)) 
def min_range_plateau(data): 
    return min(range_plateau(data)) 
def min_max_plateau(data): 
    return min(max_plateau(data)) 
def min_min_plateau(data): 
    return min(min_plateau(data)) 
def min_surface_plateau(data): 
    return min(surface_plateau(data)) 
def sum_width_plateau(data): 
    return sum(width_plateau(data)) 
def sum_range_plateau(data): 
    return sum(range_plateau(data)) 
def sum_max_plateau(data): 
    return sum(max_plateau(data)) 
def sum_min_plateau(data): 
    return sum(min_plateau(data)) 
def sum_surface_plateau(data): 
    return sum(surface_plateau(data)) 

# --------------------------------------------------------------------------- 
# DECREASING
# --------------------------------------------------------------------------- 

decreasing = Pattern('decreasing', '>', 0, 0)

# --- decreasing features --- 
 
def one_decreasing(data): 
    matches = decreasing.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.one()) 
    return result 
def width_decreasing(data): 
    matches = decreasing.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.width()) 
    return result 
def range_decreasing(data): 
    matches = decreasing.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.range()) 
    return result 
def max_decreasing(data): 
    matches = decreasing.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.max()) 
    return result 
def min_decreasing(data): 
    matches = decreasing.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.min()) 
    return result 
def surface_decreasing(data): 
    matches = decreasing.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.surface()) 
    return result 

# --- decreasing aggregators --- 
 
def max_width_decreasing(data): 
    return max(width_decreasing(data)) 
def max_range_decreasing(data): 
    return max(range_decreasing(data)) 
def max_max_decreasing(data): 
    return max(max_decreasing(data)) 
def max_min_decreasing(data): 
    return max(min_decreasing(data)) 
def max_surface_decreasing(data): 
    return max(surface_decreasing(data)) 
def min_width_decreasing(data): 
    return min(width_decreasing(data)) 
def min_range_decreasing(data): 
    return min(range_decreasing(data)) 
def min_max_decreasing(data): 
    return min(max_decreasing(data)) 
def min_min_decreasing(data): 
    return min(min_decreasing(data)) 
def min_surface_decreasing(data): 
    return min(surface_decreasing(data)) 
def sum_width_decreasing(data): 
    return sum(width_decreasing(data)) 
def sum_range_decreasing(data): 
    return sum(range_decreasing(data)) 
def sum_max_decreasing(data): 
    return sum(max_decreasing(data)) 
def sum_min_decreasing(data): 
    return sum(min_decreasing(data)) 
def sum_surface_decreasing(data): 
    return sum(surface_decreasing(data)) 

# --------------------------------------------------------------------------- 
# DECREASING_TERRACE
# --------------------------------------------------------------------------- 

decreasing_terrace = Pattern('decreasing_terrace', '>=+>', 1, 1)

# --- decreasing_terrace features --- 
 
def one_decreasing_terrace(data): 
    matches = decreasing_terrace.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.one()) 
    return result 
def width_decreasing_terrace(data): 
    matches = decreasing_terrace.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.width()) 
    return result 
def range_decreasing_terrace(data): 
    matches = decreasing_terrace.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.range()) 
    return result 
def max_decreasing_terrace(data): 
    matches = decreasing_terrace.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.max()) 
    return result 
def min_decreasing_terrace(data): 
    matches = decreasing_terrace.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.min()) 
    return result 
def surface_decreasing_terrace(data): 
    matches = decreasing_terrace.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.surface()) 
    return result 

# --- decreasing_terrace aggregators --- 
 
def max_width_decreasing_terrace(data): 
    return max(width_decreasing_terrace(data)) 
def max_range_decreasing_terrace(data): 
    return max(range_decreasing_terrace(data)) 
def max_max_decreasing_terrace(data): 
    return max(max_decreasing_terrace(data)) 
def max_min_decreasing_terrace(data): 
    return max(min_decreasing_terrace(data)) 
def max_surface_decreasing_terrace(data): 
    return max(surface_decreasing_terrace(data)) 
def min_width_decreasing_terrace(data): 
    return min(width_decreasing_terrace(data)) 
def min_range_decreasing_terrace(data): 
    return min(range_decreasing_terrace(data)) 
def min_max_decreasing_terrace(data): 
    return min(max_decreasing_terrace(data)) 
def min_min_decreasing_terrace(data): 
    return min(min_decreasing_terrace(data)) 
def min_surface_decreasing_terrace(data): 
    return min(surface_decreasing_terrace(data)) 
def sum_width_decreasing_terrace(data): 
    return sum(width_decreasing_terrace(data)) 
def sum_range_decreasing_terrace(data): 
    return sum(range_decreasing_terrace(data)) 
def sum_max_decreasing_terrace(data): 
    return sum(max_decreasing_terrace(data)) 
def sum_min_decreasing_terrace(data): 
    return sum(min_decreasing_terrace(data)) 
def sum_surface_decreasing_terrace(data): 
    return sum(surface_decreasing_terrace(data)) 

# --------------------------------------------------------------------------- 
# GORGE
# --------------------------------------------------------------------------- 

gorge = Pattern('gorge', '(>|(>(=|>)*>))(<|(<(=|<)*<))', 1, 1)

# --- gorge features --- 
 
def one_gorge(data): 
    matches = gorge.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.one()) 
    return result 
def width_gorge(data): 
    matches = gorge.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.width()) 
    return result 
def range_gorge(data): 
    matches = gorge.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.range()) 
    return result 
def max_gorge(data): 
    matches = gorge.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.max()) 
    return result 
def min_gorge(data): 
    matches = gorge.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.min()) 
    return result 
def surface_gorge(data): 
    matches = gorge.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.surface()) 
    return result 

# --- gorge aggregators --- 
 
def max_width_gorge(data): 
    return max(width_gorge(data)) 
def max_range_gorge(data): 
    return max(range_gorge(data)) 
def max_max_gorge(data): 
    return max(max_gorge(data)) 
def max_min_gorge(data): 
    return max(min_gorge(data)) 
def max_surface_gorge(data): 
    return max(surface_gorge(data)) 
def min_width_gorge(data): 
    return min(width_gorge(data)) 
def min_range_gorge(data): 
    return min(range_gorge(data)) 
def min_max_gorge(data): 
    return min(max_gorge(data)) 
def min_min_gorge(data): 
    return min(min_gorge(data)) 
def min_surface_gorge(data): 
    return min(surface_gorge(data)) 
def sum_width_gorge(data): 
    return sum(width_gorge(data)) 
def sum_range_gorge(data): 
    return sum(range_gorge(data)) 
def sum_max_gorge(data): 
    return sum(max_gorge(data)) 
def sum_min_gorge(data): 
    return sum(min_gorge(data)) 
def sum_surface_gorge(data): 
    return sum(surface_gorge(data)) 

# --------------------------------------------------------------------------- 
# PEAK
# --------------------------------------------------------------------------- 

peak = Pattern('peak', '<(=|<)*(>|=)*>', 1, 1)

# --- peak features --- 
 
def one_peak(data): 
    matches = peak.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.one()) 
    return result 
def width_peak(data): 
    matches = peak.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.width()) 
    return result 
def range_peak(data): 
    matches = peak.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.range()) 
    return result 
def max_peak(data): 
    matches = peak.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.max()) 
    return result 
def min_peak(data): 
    matches = peak.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.min()) 
    return result 
def surface_peak(data): 
    matches = peak.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.surface()) 
    return result 

# --- peak aggregators --- 
 
def max_width_peak(data): 
    return max(width_peak(data)) 
def max_range_peak(data): 
    return max(range_peak(data)) 
def max_max_peak(data): 
    return max(max_peak(data)) 
def max_min_peak(data): 
    return max(min_peak(data)) 
def max_surface_peak(data): 
    return max(surface_peak(data)) 
def min_width_peak(data): 
    return min(width_peak(data)) 
def min_range_peak(data): 
    return min(range_peak(data)) 
def min_max_peak(data): 
    return min(max_peak(data)) 
def min_min_peak(data): 
    return min(min_peak(data)) 
def min_surface_peak(data): 
    return min(surface_peak(data)) 
def sum_width_peak(data): 
    return sum(width_peak(data)) 
def sum_range_peak(data): 
    return sum(range_peak(data)) 
def sum_max_peak(data): 
    return sum(max_peak(data)) 
def sum_min_peak(data): 
    return sum(min_peak(data)) 
def sum_surface_peak(data): 
    return sum(surface_peak(data)) 

# --------------------------------------------------------------------------- 
# INCREASING
# --------------------------------------------------------------------------- 

increasing = Pattern('increasing', '<', 0, 0)

# --- increasing features --- 
 
def one_increasing(data): 
    matches = increasing.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.one()) 
    return result 
def width_increasing(data): 
    matches = increasing.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.width()) 
    return result 
def range_increasing(data): 
    matches = increasing.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.range()) 
    return result 
def max_increasing(data): 
    matches = increasing.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.max()) 
    return result 
def min_increasing(data): 
    matches = increasing.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.min()) 
    return result 
def surface_increasing(data): 
    matches = increasing.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.surface()) 
    return result 

# --- increasing aggregators --- 
 
def max_width_increasing(data): 
    return max(width_increasing(data)) 
def max_range_increasing(data): 
    return max(range_increasing(data)) 
def max_max_increasing(data): 
    return max(max_increasing(data)) 
def max_min_increasing(data): 
    return max(min_increasing(data)) 
def max_surface_increasing(data): 
    return max(surface_increasing(data)) 
def min_width_increasing(data): 
    return min(width_increasing(data)) 
def min_range_increasing(data): 
    return min(range_increasing(data)) 
def min_max_increasing(data): 
    return min(max_increasing(data)) 
def min_min_increasing(data): 
    return min(min_increasing(data)) 
def min_surface_increasing(data): 
    return min(surface_increasing(data)) 
def sum_width_increasing(data): 
    return sum(width_increasing(data)) 
def sum_range_increasing(data): 
    return sum(range_increasing(data)) 
def sum_max_increasing(data): 
    return sum(max_increasing(data)) 
def sum_min_increasing(data): 
    return sum(min_increasing(data)) 
def sum_surface_increasing(data): 
    return sum(surface_increasing(data)) 

# --------------------------------------------------------------------------- 
# INCREASING_TERRACE
# --------------------------------------------------------------------------- 

increasing_terrace = Pattern('increasing_terrace', '<=+<', 1, 1)

# --- increasing_terrace features --- 
 
def one_increasing_terrace(data): 
    matches = increasing_terrace.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.one()) 
    return result 
def width_increasing_terrace(data): 
    matches = increasing_terrace.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.width()) 
    return result 
def range_increasing_terrace(data): 
    matches = increasing_terrace.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.range()) 
    return result 
def max_increasing_terrace(data): 
    matches = increasing_terrace.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.max()) 
    return result 
def min_increasing_terrace(data): 
    matches = increasing_terrace.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.min()) 
    return result 
def surface_increasing_terrace(data): 
    matches = increasing_terrace.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.surface()) 
    return result 

# --- increasing_terrace aggregators --- 
 
def max_width_increasing_terrace(data): 
    return max(width_increasing_terrace(data)) 
def max_range_increasing_terrace(data): 
    return max(range_increasing_terrace(data)) 
def max_max_increasing_terrace(data): 
    return max(max_increasing_terrace(data)) 
def max_min_increasing_terrace(data): 
    return max(min_increasing_terrace(data)) 
def max_surface_increasing_terrace(data): 
    return max(surface_increasing_terrace(data)) 
def min_width_increasing_terrace(data): 
    return min(width_increasing_terrace(data)) 
def min_range_increasing_terrace(data): 
    return min(range_increasing_terrace(data)) 
def min_max_increasing_terrace(data): 
    return min(max_increasing_terrace(data)) 
def min_min_increasing_terrace(data): 
    return min(min_increasing_terrace(data)) 
def min_surface_increasing_terrace(data): 
    return min(surface_increasing_terrace(data)) 
def sum_width_increasing_terrace(data): 
    return sum(width_increasing_terrace(data)) 
def sum_range_increasing_terrace(data): 
    return sum(range_increasing_terrace(data)) 
def sum_max_increasing_terrace(data): 
    return sum(max_increasing_terrace(data)) 
def sum_min_increasing_terrace(data): 
    return sum(min_increasing_terrace(data)) 
def sum_surface_increasing_terrace(data): 
    return sum(surface_increasing_terrace(data)) 

# --------------------------------------------------------------------------- 
# STRICTLY_DECREASING_SEQUENCE
# --------------------------------------------------------------------------- 

strictly_decreasing_sequence = Pattern('strictly_decreasing_sequence', '>+', 0, 0)

# --- strictly_decreasing_sequence features --- 
 
def one_strictly_decreasing_sequence(data): 
    matches = strictly_decreasing_sequence.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.one()) 
    return result 
def width_strictly_decreasing_sequence(data): 
    matches = strictly_decreasing_sequence.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.width()) 
    return result 
def range_strictly_decreasing_sequence(data): 
    matches = strictly_decreasing_sequence.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.range()) 
    return result 
def max_strictly_decreasing_sequence(data): 
    matches = strictly_decreasing_sequence.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.max()) 
    return result 
def min_strictly_decreasing_sequence(data): 
    matches = strictly_decreasing_sequence.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.min()) 
    return result 
def surface_strictly_decreasing_sequence(data): 
    matches = strictly_decreasing_sequence.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.surface()) 
    return result 

# --- strictly_decreasing_sequence aggregators --- 
 
def max_width_strictly_decreasing_sequence(data): 
    return max(width_strictly_decreasing_sequence(data)) 
def max_range_strictly_decreasing_sequence(data): 
    return max(range_strictly_decreasing_sequence(data)) 
def max_max_strictly_decreasing_sequence(data): 
    return max(max_strictly_decreasing_sequence(data)) 
def max_min_strictly_decreasing_sequence(data): 
    return max(min_strictly_decreasing_sequence(data)) 
def max_surface_strictly_decreasing_sequence(data): 
    return max(surface_strictly_decreasing_sequence(data)) 
def min_width_strictly_decreasing_sequence(data): 
    return min(width_strictly_decreasing_sequence(data)) 
def min_range_strictly_decreasing_sequence(data): 
    return min(range_strictly_decreasing_sequence(data)) 
def min_max_strictly_decreasing_sequence(data): 
    return min(max_strictly_decreasing_sequence(data)) 
def min_min_strictly_decreasing_sequence(data): 
    return min(min_strictly_decreasing_sequence(data)) 
def min_surface_strictly_decreasing_sequence(data): 
    return min(surface_strictly_decreasing_sequence(data)) 
def sum_width_strictly_decreasing_sequence(data): 
    return sum(width_strictly_decreasing_sequence(data)) 
def sum_range_strictly_decreasing_sequence(data): 
    return sum(range_strictly_decreasing_sequence(data)) 
def sum_max_strictly_decreasing_sequence(data): 
    return sum(max_strictly_decreasing_sequence(data)) 
def sum_min_strictly_decreasing_sequence(data): 
    return sum(min_strictly_decreasing_sequence(data)) 
def sum_surface_strictly_decreasing_sequence(data): 
    return sum(surface_strictly_decreasing_sequence(data)) 

# --------------------------------------------------------------------------- 
# PROPER_PLAIN
# --------------------------------------------------------------------------- 

proper_plain = Pattern('proper_plain', '>=+<', 1, 1)

# --- proper_plain features --- 
 
def one_proper_plain(data): 
    matches = proper_plain.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.one()) 
    return result 
def width_proper_plain(data): 
    matches = proper_plain.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.width()) 
    return result 
def range_proper_plain(data): 
    matches = proper_plain.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.range()) 
    return result 
def max_proper_plain(data): 
    matches = proper_plain.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.max()) 
    return result 
def min_proper_plain(data): 
    matches = proper_plain.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.min()) 
    return result 
def surface_proper_plain(data): 
    matches = proper_plain.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.surface()) 
    return result 

# --- proper_plain aggregators --- 
 
def max_width_proper_plain(data): 
    return max(width_proper_plain(data)) 
def max_range_proper_plain(data): 
    return max(range_proper_plain(data)) 
def max_max_proper_plain(data): 
    return max(max_proper_plain(data)) 
def max_min_proper_plain(data): 
    return max(min_proper_plain(data)) 
def max_surface_proper_plain(data): 
    return max(surface_proper_plain(data)) 
def min_width_proper_plain(data): 
    return min(width_proper_plain(data)) 
def min_range_proper_plain(data): 
    return min(range_proper_plain(data)) 
def min_max_proper_plain(data): 
    return min(max_proper_plain(data)) 
def min_min_proper_plain(data): 
    return min(min_proper_plain(data)) 
def min_surface_proper_plain(data): 
    return min(surface_proper_plain(data)) 
def sum_width_proper_plain(data): 
    return sum(width_proper_plain(data)) 
def sum_range_proper_plain(data): 
    return sum(range_proper_plain(data)) 
def sum_max_proper_plain(data): 
    return sum(max_proper_plain(data)) 
def sum_min_proper_plain(data): 
    return sum(min_proper_plain(data)) 
def sum_surface_proper_plain(data): 
    return sum(surface_proper_plain(data)) 
