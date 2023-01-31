kmrun = float(input('How many kilometers did you travel?'))
drun = int(input('How many days did you travel?'))
vkm = kmrun * 0.15
vdr = drun * 60
fv = vkm + vdr
print('The payment amount for the rental car will be RS{:.2f}.'.format(fv))