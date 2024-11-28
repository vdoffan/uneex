from fractions import Fraction
from math import floor

class Sausage:
    def __init__(self, *args):
        if len(args) == 0:
            self.meat = 'pork!'
            self.volume = Fraction(1)
        elif len(args) == 1:
            self.meat = args[0]
            self.volume = Fraction(1)
        elif len(args) == 2:
            self.meat = args[0]
            self.volume = Fraction(args[1])
        else:
            raise ValueError("Invalid number of arguments")
        if self.volume < 0:
            self.volume = Fraction(0)
    
    def __add__(self, other):
        if isinstance(other, Sausage):
            new_volume = self.volume + other.volume
            return Sausage(self.meat, new_volume)
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, Sausage):
            new_volume = self.volume - other.volume
            if new_volume < 0:
                new_volume = Fraction(0)
            return Sausage(self.meat, new_volume)
        return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, (int, float, Fraction)):
            new_volume = self.volume * Fraction(other)
            if new_volume < 0:
                new_volume = Fraction(0)
            return Sausage(self.meat, new_volume)
        return NotImplemented
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self, other):
        if isinstance(other, (int, float, Fraction)):
            new_volume = self.volume / Fraction(other)
            if new_volume < 0:
                new_volume = Fraction(0)
            return Sausage(self.meat, new_volume)
        return NotImplemented
    
    def __abs__(self):
        return self.volume
    
    def __bool__(self):
        return self.volume != 0
    
    def __str__(self):
        if self.volume <= 0:
            # Empty sausage
            s = '/|\n||\n||\n||\n\\|'
            return s
        else:
            n_full = int(self.volume)
            fractional_part = self.volume - n_full

            meat_len = floor(fractional_part * 12)
            if meat_len > 0:
                has_fractional = True
            else:
                meat_len = 0
                has_fractional = False

            segments = []

            # Add full sausages
            for i in range(n_full):
                segment = {}
                segment['type'] = 'full'
                segment['top'] = '/------------\\'
                segment['bottom'] = '\\------------/'
                meat_content = (self.meat * ((12 + len(self.meat) - 1) // len(self.meat)))[:12]
                segment['meat'] = ['|' + meat_content + '|' for _ in range(3)]
                segments.append(segment)

            # Add incomplete sausage if any
            if has_fractional:
                segment = {}
                segment['type'] = 'incomplete'
                casing = '-' * meat_len
                segment['top'] = '/' + casing + '|'
                segment['bottom'] = '\\' + casing + '|'
                meat_content = (self.meat * ((meat_len + len(self.meat) - 1) // len(self.meat)))[:meat_len]
                segment['meat'] = ['|' + meat_content + '|' for _ in range(3)]
                segments.append(segment)

            if not segments:
                # Volume is positive but too small to create any meat
                # Return empty sausage
                s = '/|\n||\n||\n||\n\\|'
                return s

            # Build the final strings
            top_line = segments[0]['top']
            bottom_line = segments[0]['bottom']
            meat_lines = segments[0]['meat']

            for idx in range(1, len(segments)):
                prev_segment = segments[idx - 1]
                segment = segments[idx]

                # Adjust casings between segments
                top_line = top_line[:-1] + '\\/' + segment['top'][1:]
                bottom_line = bottom_line[:-1] + '/\\' + segment['bottom'][1:]

                # Adjust meat lines
                for i in range(3):
                    meat_lines[i] = meat_lines[i][:-1] + '||' + segment['meat'][i][1:]

            # Adjust ending casing if last segment is incomplete
            last_segment = segments[-1]
            if last_segment['type'] == 'incomplete':
                top_line = top_line[:-1] + '|'
                bottom_line = bottom_line[:-1] + '|'

            return '\n'.join([top_line] + meat_lines + [bottom_line])


