def extract_colors():
  import colorgram
  rgb_colors = []
  image_colors = colorgram.extract('hirst_painting.jpg', 100)

  for color in image_colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    color_tuple = (r, g, b)
    rgb_colors.append(color_tuple)
  print(rgb_colors)
 
extract_colors()
color_list = [(233, 220, 226), (218, 223, 230), (230, 207, 91), (225, 149, 91), (122, 167, 187), (35, 110, 158), (163, 13, 22), (127, 177, 145), (233, 81, 49), (202, 67, 27), (192, 186, 23), (174, 18, 13), (33, 129, 49), (7, 99, 37), (13, 64, 39), (12, 41, 76), (242, 203, 4), (139, 79, 92), (88, 13, 20), (53, 166, 76), (51, 23, 19), (180, 134, 146), (6, 64, 137), (213, 68, 75), (230, 170, 161), (49, 151, 191), (77, 133, 186), (175, 204, 176), (165, 
202, 210), (223, 171, 176), (176, 187, 213), (253, 6, 5), (254, 4, 17), (37, 75, 86)]