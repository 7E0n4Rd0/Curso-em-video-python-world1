# n1 = int(input('Enter one number in meters:'))
n1 = float(input('Enter a number in meters:'))
cen = n1*100
mm = n1*1000
# print('This number in Meters is: {}m, on centimeters is {}cen and in millimeters is {}mm'.format(n1, cen, mm))
print('This number in Meters is: {:.0f}m, on centimeters is {:.0f}cen and in millimeters is {:.0f}mm'.format(n1, cen, mm))