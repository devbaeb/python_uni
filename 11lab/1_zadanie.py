import math

print([math.sin(i) for i in [math.pi/6, math.pi/4, math.pi/3]])

print([math.sin(i) for i in (math.pi/6, math.pi/4, math.pi/3)])

print([[math.sin(i), math.cos(i)] for i in (math.pi/6, math.pi/4, math.pi/3)])
