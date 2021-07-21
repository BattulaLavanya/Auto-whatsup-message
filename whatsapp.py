import pywhatkit
Ph_number = input('+'+"Enter number ")
z=22
while True:
    z=z+1
    pywhatkit.sendwhatmsg(Ph_number, 'I Love You /n frm auto python message', 20, z)
