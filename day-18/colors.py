import colorgram

# colorization
url = './test.jpg'
extracted_colors = colorgram.extract(url, 100)
colors = []

for _ in extracted_colors:
    r = _.rgb[0]
    g = _.rgb[1]
    b = _.rgb[2]
    color_tup = (r, g, b)
    colors.append(color_tup)

