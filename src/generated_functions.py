# -------------------------------------------------- 
# This file was auto-generated on 2017-10-27
# By Florine Cercle - Lisa Pasqualini - Denis Allard
# -------------------------------------------------- 
 
import pattern

# --------------- 
# zigzag
# --------------- 

zigzag = pattern.Pattern('zigzag', '(<>)+(<|<>)|(><)+(>|><)', 1, 1)

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
def height_zigzag(data): 
    matches = zigzag.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.height()) 
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
def max_height_zigzag(data): 
    return max(height_zigzag(data)) 
def max_max_zigzag(data): 
    return max(max_zigzag(data)) 
def max_min_zigzag(data): 
    return max(min_zigzag(data)) 
def max_surface_zigzag(data): 
    return max(surface_zigzag(data)) 
def min_width_zigzag(data): 
    return min(width_zigzag(data)) 
def min_height_zigzag(data): 
    return min(height_zigzag(data)) 
def min_max_zigzag(data): 
    return min(max_zigzag(data)) 
def min_min_zigzag(data): 
    return min(min_zigzag(data)) 
def min_surface_zigzag(data): 
    return min(surface_zigzag(data)) 
def sum_width_zigzag(data): 
    return sum(width_zigzag(data)) 
def sum_height_zigzag(data): 
    return sum(height_zigzag(data)) 
def sum_max_zigzag(data): 
    return sum(max_zigzag(data)) 
def sum_min_zigzag(data): 
    return sum(min_zigzag(data)) 
def sum_surface_zigzag(data): 
    return sum(surface_zigzag(data)) 

# --------------- 
# inflexion
# --------------- 

inflexion = pattern.Pattern('inflexion', '<(<|=)*>|>(>|=)*<', 1, 1)

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
def height_inflexion(data): 
    matches = inflexion.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.height()) 
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
def max_height_inflexion(data): 
    return max(height_inflexion(data)) 
def max_max_inflexion(data): 
    return max(max_inflexion(data)) 
def max_min_inflexion(data): 
    return max(min_inflexion(data)) 
def max_surface_inflexion(data): 
    return max(surface_inflexion(data)) 
def min_width_inflexion(data): 
    return min(width_inflexion(data)) 
def min_height_inflexion(data): 
    return min(height_inflexion(data)) 
def min_max_inflexion(data): 
    return min(max_inflexion(data)) 
def min_min_inflexion(data): 
    return min(min_inflexion(data)) 
def min_surface_inflexion(data): 
    return min(surface_inflexion(data)) 
def sum_width_inflexion(data): 
    return sum(width_inflexion(data)) 
def sum_height_inflexion(data): 
    return sum(height_inflexion(data)) 
def sum_max_inflexion(data): 
    return sum(max_inflexion(data)) 
def sum_min_inflexion(data): 
    return sum(min_inflexion(data)) 
def sum_surface_inflexion(data): 
    return sum(surface_inflexion(data)) 

# --------------- 
# peak
# --------------- 

peak = pattern.Pattern('peak', '<(=|<)*(>|=)*>', 1, 1)

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
def height_peak(data): 
    matches = peak.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.height()) 
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
def max_height_peak(data): 
    return max(height_peak(data)) 
def max_max_peak(data): 
    return max(max_peak(data)) 
def max_min_peak(data): 
    return max(min_peak(data)) 
def max_surface_peak(data): 
    return max(surface_peak(data)) 
def min_width_peak(data): 
    return min(width_peak(data)) 
def min_height_peak(data): 
    return min(height_peak(data)) 
def min_max_peak(data): 
    return min(max_peak(data)) 
def min_min_peak(data): 
    return min(min_peak(data)) 
def min_surface_peak(data): 
    return min(surface_peak(data)) 
def sum_width_peak(data): 
    return sum(width_peak(data)) 
def sum_height_peak(data): 
    return sum(height_peak(data)) 
def sum_max_peak(data): 
    return sum(max_peak(data)) 
def sum_min_peak(data): 
    return sum(min_peak(data)) 
def sum_surface_peak(data): 
    return sum(surface_peak(data)) 

# --------------- 
# increasing_terrace
# --------------- 

increasing_terrace = pattern.Pattern('increasing_terrace', '<=+<', 1, 1)

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
def height_increasing_terrace(data): 
    matches = increasing_terrace.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.height()) 
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
def max_height_increasing_terrace(data): 
    return max(height_increasing_terrace(data)) 
def max_max_increasing_terrace(data): 
    return max(max_increasing_terrace(data)) 
def max_min_increasing_terrace(data): 
    return max(min_increasing_terrace(data)) 
def max_surface_increasing_terrace(data): 
    return max(surface_increasing_terrace(data)) 
def min_width_increasing_terrace(data): 
    return min(width_increasing_terrace(data)) 
def min_height_increasing_terrace(data): 
    return min(height_increasing_terrace(data)) 
def min_max_increasing_terrace(data): 
    return min(max_increasing_terrace(data)) 
def min_min_increasing_terrace(data): 
    return min(min_increasing_terrace(data)) 
def min_surface_increasing_terrace(data): 
    return min(surface_increasing_terrace(data)) 
def sum_width_increasing_terrace(data): 
    return sum(width_increasing_terrace(data)) 
def sum_height_increasing_terrace(data): 
    return sum(height_increasing_terrace(data)) 
def sum_max_increasing_terrace(data): 
    return sum(max_increasing_terrace(data)) 
def sum_min_increasing_terrace(data): 
    return sum(min_increasing_terrace(data)) 
def sum_surface_increasing_terrace(data): 
    return sum(surface_increasing_terrace(data)) 

# --------------- 
# proper_plateau
# --------------- 

proper_plateau = pattern.Pattern('proper_plateau', '<=+>', 1, 1)

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
def height_proper_plateau(data): 
    matches = proper_plateau.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.height()) 
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
def max_height_proper_plateau(data): 
    return max(height_proper_plateau(data)) 
def max_max_proper_plateau(data): 
    return max(max_proper_plateau(data)) 
def max_min_proper_plateau(data): 
    return max(min_proper_plateau(data)) 
def max_surface_proper_plateau(data): 
    return max(surface_proper_plateau(data)) 
def min_width_proper_plateau(data): 
    return min(width_proper_plateau(data)) 
def min_height_proper_plateau(data): 
    return min(height_proper_plateau(data)) 
def min_max_proper_plateau(data): 
    return min(max_proper_plateau(data)) 
def min_min_proper_plateau(data): 
    return min(min_proper_plateau(data)) 
def min_surface_proper_plateau(data): 
    return min(surface_proper_plateau(data)) 
def sum_width_proper_plateau(data): 
    return sum(width_proper_plateau(data)) 
def sum_height_proper_plateau(data): 
    return sum(height_proper_plateau(data)) 
def sum_max_proper_plateau(data): 
    return sum(max_proper_plateau(data)) 
def sum_min_proper_plateau(data): 
    return sum(min_proper_plateau(data)) 
def sum_surface_proper_plateau(data): 
    return sum(surface_proper_plateau(data)) 

# --------------- 
# steady
# --------------- 

steady = pattern.Pattern('steady', '=', 0, 0)

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
def height_steady(data): 
    matches = steady.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.height()) 
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
def max_height_steady(data): 
    return max(height_steady(data)) 
def max_max_steady(data): 
    return max(max_steady(data)) 
def max_min_steady(data): 
    return max(min_steady(data)) 
def max_surface_steady(data): 
    return max(surface_steady(data)) 
def min_width_steady(data): 
    return min(width_steady(data)) 
def min_height_steady(data): 
    return min(height_steady(data)) 
def min_max_steady(data): 
    return min(max_steady(data)) 
def min_min_steady(data): 
    return min(min_steady(data)) 
def min_surface_steady(data): 
    return min(surface_steady(data)) 
def sum_width_steady(data): 
    return sum(width_steady(data)) 
def sum_height_steady(data): 
    return sum(height_steady(data)) 
def sum_max_steady(data): 
    return sum(max_steady(data)) 
def sum_min_steady(data): 
    return sum(min_steady(data)) 
def sum_surface_steady(data): 
    return sum(surface_steady(data)) 

# --------------- 
# increasing_sequence
# --------------- 

increasing_sequence = pattern.Pattern('increasing_sequence', '<(<|=)*<|<', 0, 0)

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
def height_increasing_sequence(data): 
    matches = increasing_sequence.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.height()) 
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
def max_height_increasing_sequence(data): 
    return max(height_increasing_sequence(data)) 
def max_max_increasing_sequence(data): 
    return max(max_increasing_sequence(data)) 
def max_min_increasing_sequence(data): 
    return max(min_increasing_sequence(data)) 
def max_surface_increasing_sequence(data): 
    return max(surface_increasing_sequence(data)) 
def min_width_increasing_sequence(data): 
    return min(width_increasing_sequence(data)) 
def min_height_increasing_sequence(data): 
    return min(height_increasing_sequence(data)) 
def min_max_increasing_sequence(data): 
    return min(max_increasing_sequence(data)) 
def min_min_increasing_sequence(data): 
    return min(min_increasing_sequence(data)) 
def min_surface_increasing_sequence(data): 
    return min(surface_increasing_sequence(data)) 
def sum_width_increasing_sequence(data): 
    return sum(width_increasing_sequence(data)) 
def sum_height_increasing_sequence(data): 
    return sum(height_increasing_sequence(data)) 
def sum_max_increasing_sequence(data): 
    return sum(max_increasing_sequence(data)) 
def sum_min_increasing_sequence(data): 
    return sum(min_increasing_sequence(data)) 
def sum_surface_increasing_sequence(data): 
    return sum(surface_increasing_sequence(data)) 

# --------------- 
# summit
# --------------- 

summit = pattern.Pattern('summit', '(<|(<(=|<)*<))(>|(>(=|>)*>))', 1, 1)

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
def height_summit(data): 
    matches = summit.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.height()) 
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
def max_height_summit(data): 
    return max(height_summit(data)) 
def max_max_summit(data): 
    return max(max_summit(data)) 
def max_min_summit(data): 
    return max(min_summit(data)) 
def max_surface_summit(data): 
    return max(surface_summit(data)) 
def min_width_summit(data): 
    return min(width_summit(data)) 
def min_height_summit(data): 
    return min(height_summit(data)) 
def min_max_summit(data): 
    return min(max_summit(data)) 
def min_min_summit(data): 
    return min(min_summit(data)) 
def min_surface_summit(data): 
    return min(surface_summit(data)) 
def sum_width_summit(data): 
    return sum(width_summit(data)) 
def sum_height_summit(data): 
    return sum(height_summit(data)) 
def sum_max_summit(data): 
    return sum(max_summit(data)) 
def sum_min_summit(data): 
    return sum(min_summit(data)) 
def sum_surface_summit(data): 
    return sum(surface_summit(data)) 

# --------------- 
# plateau
# --------------- 

plateau = pattern.Pattern('plateau', '<=*>', 1, 1)

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
def height_plateau(data): 
    matches = plateau.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.height()) 
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
def max_height_plateau(data): 
    return max(height_plateau(data)) 
def max_max_plateau(data): 
    return max(max_plateau(data)) 
def max_min_plateau(data): 
    return max(min_plateau(data)) 
def max_surface_plateau(data): 
    return max(surface_plateau(data)) 
def min_width_plateau(data): 
    return min(width_plateau(data)) 
def min_height_plateau(data): 
    return min(height_plateau(data)) 
def min_max_plateau(data): 
    return min(max_plateau(data)) 
def min_min_plateau(data): 
    return min(min_plateau(data)) 
def min_surface_plateau(data): 
    return min(surface_plateau(data)) 
def sum_width_plateau(data): 
    return sum(width_plateau(data)) 
def sum_height_plateau(data): 
    return sum(height_plateau(data)) 
def sum_max_plateau(data): 
    return sum(max_plateau(data)) 
def sum_min_plateau(data): 
    return sum(min_plateau(data)) 
def sum_surface_plateau(data): 
    return sum(surface_plateau(data)) 

# --------------- 
# strictly_increasing_sequence
# --------------- 

strictly_increasing_sequence= pattern.Pattern('strictly_increasing_sequence', '<+', 0, 0)

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
def height_strictly_increasing_sequence(data): 
    matches = strictly_increasing_sequence.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.height()) 
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
def max_height_strictly_increasing_sequence(data): 
    return max(height_strictly_increasing_sequence(data)) 
def max_max_strictly_increasing_sequence(data): 
    return max(max_strictly_increasing_sequence(data)) 
def max_min_strictly_increasing_sequence(data): 
    return max(min_strictly_increasing_sequence(data)) 
def max_surface_strictly_increasing_sequence(data): 
    return max(surface_strictly_increasing_sequence(data)) 
def min_width_strictly_increasing_sequence(data): 
    return min(width_strictly_increasing_sequence(data)) 
def min_height_strictly_increasing_sequence(data): 
    return min(height_strictly_increasing_sequence(data)) 
def min_max_strictly_increasing_sequence(data): 
    return min(max_strictly_increasing_sequence(data)) 
def min_min_strictly_increasing_sequence(data): 
    return min(min_strictly_increasing_sequence(data)) 
def min_surface_strictly_increasing_sequence(data): 
    return min(surface_strictly_increasing_sequence(data)) 
def sum_width_strictly_increasing_sequence(data): 
    return sum(width_strictly_increasing_sequence(data)) 
def sum_height_strictly_increasing_sequence(data): 
    return sum(height_strictly_increasing_sequence(data)) 
def sum_max_strictly_increasing_sequence(data): 
    return sum(max_strictly_increasing_sequence(data)) 
def sum_min_strictly_increasing_sequence(data): 
    return sum(min_strictly_increasing_sequence(data)) 
def sum_surface_strictly_increasing_sequence(data): 
    return sum(surface_strictly_increasing_sequence(data)) 

# --------------- 
# steady_sequence
# --------------- 

steady_sequence = pattern.Pattern('steady_sequence', '=+', 0, 0)

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
def height_steady_sequence(data): 
    matches = steady_sequence.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.height()) 
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
def max_height_steady_sequence(data): 
    return max(height_steady_sequence(data)) 
def max_max_steady_sequence(data): 
    return max(max_steady_sequence(data)) 
def max_min_steady_sequence(data): 
    return max(min_steady_sequence(data)) 
def max_surface_steady_sequence(data): 
    return max(surface_steady_sequence(data)) 
def min_width_steady_sequence(data): 
    return min(width_steady_sequence(data)) 
def min_height_steady_sequence(data): 
    return min(height_steady_sequence(data)) 
def min_max_steady_sequence(data): 
    return min(max_steady_sequence(data)) 
def min_min_steady_sequence(data): 
    return min(min_steady_sequence(data)) 
def min_surface_steady_sequence(data): 
    return min(surface_steady_sequence(data)) 
def sum_width_steady_sequence(data): 
    return sum(width_steady_sequence(data)) 
def sum_height_steady_sequence(data): 
    return sum(height_steady_sequence(data)) 
def sum_max_steady_sequence(data): 
    return sum(max_steady_sequence(data)) 
def sum_min_steady_sequence(data): 
    return sum(min_steady_sequence(data)) 
def sum_surface_steady_sequence(data): 
    return sum(surface_steady_sequence(data)) 

# --------------- 
# increasing
# --------------- 

increasing = pattern.Pattern('increasing', '<', 0, 0)

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
def height_increasing(data): 
    matches = increasing.findPatterns(data) 
    result = []
    for match in matches:
        result.append(match.height()) 
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
def max_height_increasing(data): 
    return max(height_increasing(data)) 
def max_max_increasing(data): 
    return max(max_increasing(data)) 
def max_min_increasing(data): 
    return max(min_increasing(data)) 
def max_surface_increasing(data): 
    return max(surface_increasing(data)) 
def min_width_increasing(data): 
    return min(width_increasing(data)) 
def min_height_increasing(data): 
    return min(height_increasing(data)) 
def min_max_increasing(data): 
    return min(max_increasing(data)) 
def min_min_increasing(data): 
    return min(min_increasing(data)) 
def min_surface_increasing(data): 
    return min(surface_increasing(data)) 
def sum_width_increasing(data): 
    return sum(width_increasing(data)) 
def sum_height_increasing(data): 
    return sum(height_increasing(data)) 
def sum_max_increasing(data): 
    return sum(max_increasing(data)) 
def sum_min_increasing(data): 
    return sum(min_increasing(data)) 
def sum_surface_increasing(data): 
    return sum(surface_increasing(data)) 

