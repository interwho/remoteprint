import urllib2
import serial

printer = serial.Serial('/dev/ttyS1')
kill = False

if !(printer.isOpen()):
    print "Printer 1 Not Connected"
    kill = True

while kill == False:
    gcode = urllib2.urlopen("http://localhost/server.php").read()

    gcode = gcode.split("\n")
    readytosend = []
    for i in gcode:
        x = i.split(";")[0]
        if x != "":
            readytosend.append(x)

    for i in readytosend:
        printer.write(i)
        response = printer.readline()
        if response[0] != 'o':
            print "ERROR - " + response
