import json

def init_ntc():
    for i in range(len(ntc["names"])):
        color = "#" + ntc["names"][i][0]
        rgb = rgb_from_color(color)
        hsl = hsl_from_color(color)
        ntc["names"][i].extend(rgb)
        ntc["names"][i].extend(hsl)

def name(color):
    color = color.upper()
    if len(color) < 3 or len(color) > 7:
        return ["#000000", "Invalid Color: " + color, False]
    if len(color) % 3 == 0:
        color = "#" + color
    if len(color) == 4:
        color = "#" + color[1] * 2 + color[2] * 2 + color[3] * 2

    rgb = rgb_from_color(color)
    r, g, b = rgb
    hsl = hsl_from_color(color)
    h, s, l = hsl
    ndf1 = 0
    ndf2 = 0
    ndf = 0
    cl = -1
    df = -1

    for i in range(len(ntc["names"])):
        if color == "#" + ntc["names"][i][0]:
            return ["#" + ntc["names"][i][0], ntc["names"][i][1], True]

        ndf1 = (r - ntc["names"][i][2]) ** 2 + (g - ntc["names"][i][3]) ** 2 + (b - ntc["names"][i][4]) ** 2
        ndf2 = (h - ntc["names"][i][5]) ** 2 + (s - ntc["names"][i][6]) ** 2 + (l - ntc["names"][i][7]) ** 2
        ndf = ndf1 + ndf2 * 2
        if df < 0 or df > ndf:
            df = ndf
            cl = i

    return (
        ["#000000", "Invalid Color: " + color, False]
        if cl < 0
        else ["#" + ntc["names"][cl][0], ntc["names"][cl][1], False]
    )

def hsl_from_color(color):
    rgb = [int(color[i : i + 2], 16) / 255 for i in range(1, 7, 2)]
    r, g, b = rgb
    min_val = min(rgb)
    max_val = max(rgb)
    delta = max_val - min_val
    l = (min_val + max_val) / 2

    s = 0
    if 0 < l < 1:
        s = delta / (2 * l if l < 0.5 else 2 - 2 * l)

    h = 0
    if delta > 0:
        if max_val == r and max_val != g:
            h += (g - b) / delta
        if max_val == g and max_val != b:
            h += 2 + (b - r) / delta
        if max_val == b and max_val != r:
            h += 4 + (r - g) / delta
        h /= 6

    return [int(h * 255), int(s * 255), int(l * 255)]

def rgb_from_color(color):
    return [
        int(color[i : i + 2], 16) for i in range(1, 7, 2)
    ]  # Extract R, G, B components from color string

json_url = "color_names.json"
color_names = None

with open(json_url, 'r') as f:
    color_names = json.load(f)

ntc = {
    "init": init_ntc,
    "name": name,
    "hsl": hsl_from_color,
    "rgb": rgb_from_color,
    "names": color_names,
}

# Initialize the ntc object
ntc["init"]()

# Use name("#001B1C")

# background_color = ['#006f51',  '#c41130',  '#fbfafc',  '#027252',]
# for i in range(len(background_color)):
#     print(name(background_color[i]))
# n_match = name("#001B1C")[1]
# print(n_match)
