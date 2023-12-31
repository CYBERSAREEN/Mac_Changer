""" 
algorythm based macChanger that reads the output and checks if the mac is changed or not 
"""


#fucntions we need in  a mac changer
import subprocess as sb #>>>this will import subprocess to perform terminal commands
import optparse as opt #>>>this will import the manual liberary to project manual on terminal 
import re #>>> reg ex to search any string vallue apon certain value inputs


def get_arguments():
    parser = opt.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Here to provide the interface name of the network interface of your choice")
    parser.add_option("-m", "--mac", dest="new_mac", help="This argument is designed to change its MAC ADDRESS")
    (options, arguments) = parser.parse_args()

    if not options.interface:
        # code to handle error
        # if the user didn't put any value show error <no interface provided>
        parser.error("[-] <please specify the interface, use --help for info>")
        
    elif not options.new_mac:
        # code to handle error
        # if the user didn't put any value show error <no mac address provided>
        parser.error("[-] <please specify the mac address, use --help for info>")
    
    return options  # Always return options

def change_mac(interface, new_mac):
    sb.call(["ifconfig", interface, "down"])
    sb.call(["ifconfig", interface, "hw", "ether", new_mac])
    sb.call(["ifconfig", interface, "up"])
    print("[+] Changing Mac Address for " + interface + " .......")
    print("[+] Current MAC is changed to " + new_mac ) 

def get_current_mac(interface):
    ifconfig_result = sb.check_output(["ifconfig", interface])
    MacAdrResult = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    
    if MacAdrResult:
        return MacAdrResult.group(0)
    else:
        print("[-] COULD NOT READ MAC ADDRESS")   

options = get_arguments()

if options:
    current_mac = get_current_mac(options.interface)
    print("current MAC = " + str(current_mac))

    change_mac(options.interface, options.new_mac)

    current_mac = get_current_mac(options.interface)

    if current_mac == options.new_mac:
        print("[+] MAC ADDRESS WAS SUCCESSFULLY CHANGED TO " + current_mac)
    else:
        print("[-] MAC address did not get changed")
