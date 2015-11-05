color = ['red','blue','gree']
color2= ['orange','black','white']
print color + color2
len(color)
color[0] = 'yellow'
print color*2
'blue' in color2
total_color = color + color2
for each_color in total_color:
    print each_color

color.append("white")
color.extend(["black","purple"])
color.insert(0,"orange")

print color

color.remove("white")
del color[0]
print color
