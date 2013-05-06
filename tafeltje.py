#!/usr/bin/python

vakje = (27, 27) # size in mm
marges = (2, 2) #padding in mm
vakjes = (16, 16) #number of
frees = 6 # diameter of tool
dikte = 16 # depth of material
speed = 1500 # speed of tool in mm/min

# substract tool size from vakjes and marges
vakje = (vakje[0] - frees/2,
         vakje[1] - frees/2)

marges = (marge[0] + frees/2,
          marge[1] + frees/2)

print """G90
F%d""" % speed
for x in xrange(0, vakjes[0]):
  for y in xrange(0, vakjes[1]):
    coords = ((x*(vakje[0]+(2*marges[0]))),
              (y*(vakje[1]+(2*marges[1]))))

    print 'G00 X%d Y%d' % (coords[0],
                           coords[1])

    print 'G01 Z%d' % dikte/2
    print 'G01 X%d Y%d' % (coords[0]+vakje[0],
                           coords[1])

    print 'G01 X%d Y%d' % (coords[0]+vakje[0],
                           coords[1]+vakje[1])

    print 'G01 X%d Y%d' % (coords[0],
                           coords[1]+vakje[1])

    print 'G01 X%d Y%d' % (coords[0],
                           coords[1])

    print 'G01 Z0'
    print 'G01 X%d Y%d' % (coords[0]+vakje[0],
                           coords[1])

    print 'G01 X%d Y%d' % (coords[0]+vakje[0],
                           coords[1]+vakje[1])

    print 'G01 X%d Y%d' % (coords[0],
                           coords[1]+vakje[1])

    print 'G01 X%d Y%d' % (coords[0],
                           coords[1])

    print 'G00 Z%d' % dikte*frees

print 'M02'
