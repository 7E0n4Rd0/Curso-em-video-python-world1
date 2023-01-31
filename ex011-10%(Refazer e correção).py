# lar = int(input('What is the width? (In Meters)'))
# alt = int(input('What is the height? (In Meters)'))
# area = lar*alt
# oneliter = 2 ** 2
# ink = oneliter
# print('You can paint {} meters square here with {} ink buckets'.format(area, oneliter))
lar = float(input('What is the width?'))
alt = float(input('What is the height?'))
area = lar*alt
print('Your wall has a dimension of {}x{} and its area of {}m²'.format(lar,alt,area ))
ink = area/2
print('To paint this wall, you will need {}l of paint.'.format(ink))