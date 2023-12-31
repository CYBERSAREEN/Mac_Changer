""" 
This python file is the ADVANCE module of the MAC Address changer for the linux system that work on the basic console commands + it has variables and conditional statements with updates 
"""
import subprocess as sb
import optparse as opt

parser = opt.OptionParser() # the class is bieng called

#it will return the user entering something in a certain way storing its value to the variables.

parser.add_option("-i","--interface",dest = "interface",help="Here to provide the interface name of network interface of your choice")

# here the parser is ordered to append values on gettting -i or --interface as a command to append the string value to the interface or the mentioned variable  
# dest= "interface" >>> directs the value to be stored at certain possition 

parser.add_option("-m","--mac",dest = "new_mac",help="This arggument is designed to change its MAC ADDRESS")
#creating for new_mac
#>>>parser.parse_args()
#it will go through every information entered by the user and will seperate the information in two parts
#it will take arguments
"""
>>> To make it address to the options availbale to the interface and new mack we need to update this to 
"""
# we need to make the parser understand that how the code will work and where to innitialise the value/string added to it 
(options,arguments) = parser.parse_args() #it will act as function 

#options will take <name of interface> ,<the new mac assigned> and the arguments will take -i or -m
# so we have to update this code to options.interface and options.newmac
sb.call("iwconfig",shell = True)
interface = options.interface
new_mac = options.new_mac

sb.call(["ifconfig",  interface , "down"])
sb.call(["ifconfig" , interface , "hw" , "ether",  new_mac])
sb.call(["ifconfig", interface  ,"up"])

print("[+] Changeing Mac Address for ",interface + " .......")
print("[+] Current MAc is changed to ",new_mac )
