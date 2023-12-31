""" 
another advance model for mac address changer which handles error when user will not put anything to increment the main things such as interface or new mac add.
also it checks whether the prompt is on kali or bieng used in windows 
"""
import subprocess as sb #>>>this will import subprocess to perform terminal commands
import optparse as opt #>>>this will import the manual liberary to project manual on terminal 
def get_arguments():
    parser = opt.OptionParser()
    parser.add_option("-i","--interface",dest = "interface",help="Here to provide the interface name of network interface of your choice")
    parser.add_option("-m","--mac",dest = "new_mac",help="This arggument is designed to change its MAC ADDRESS")
    (options,arguments) =  parser.parse_args() 
    if not options.interface:
        #code to handle error
        #if the user didn't put any value show error <no interface provided>
        parser.error("[-]<please specify the interface ,use --help for info>")
        
    elif not options.new_mac:
        #code to handle error
        #if the user didnt put any value show error <no mac address provided>
        parser.error("[-]<please specify the mac adderess ,use --help for info>")
        return options
def change_mac(interface,new_mac):
    sb.call(["ifconfig",  interface , "down"])
    sb.call(["ifconfig" , interface , "hw" , "ether",  new_mac])
    sb.call(["ifconfig", interface  ,"up"])
    print("[+] Changeing Mac Address for ",interface + " .......")
    print("[+] Current MAc is changed to ",new_mac )    
options = get_arguments()
change_mac(options.interface, options.new_mac)

