def rgb_to_hex(rgb):
  """
  Takes in a tuple with 3 values and returns a hexadecimal hash string.
  """
  return '#{:02x}{:02x}{:02x}'.format(*rgb).upper()

def hex_to_rgb(hex_color):
  """
  Takes in a hexadecimal hash string and returns a tuple with 3 values.
  """
  if hex_color.startswith('#'):
    hex_color = hex_color.lstrip('#')
  r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
  return (r, g, b)

def inverted_hex(hex_color):
  """
  Takes in a hexadecimal hash string and returns the inverted color in hexadecimal hash string.
  """
  r, g, b = hex_to_rgb(hex_color)
  r, g, b = 255 - r, 255 - g, 255 - b
  return rgb_to_hex((r, g, b))
