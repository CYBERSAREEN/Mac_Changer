#fucntions we need in  a mac changer
import subprocess as sb #>>>this will import subprocess to perform terminal commands
import optparse as opt #>>>this will import the manual liberary to project manual on terminal 

def get_arguments():#>>> to get the values to be parsed into 
    parser = opt.OptionParser() #>>> to call the predifined liberary and to call the value 
    parser.add_option("-i","--interface",dest = "interface",help="Here to provide the interface name of network interface of your choice")
    parser.add_option("-m","--mac",dest = "new_mac",help="This arggument is designed to change its MAC ADDRESS")
    #>>> assigning the values to parse to which variable to be stored it as
        
    return parser.parse_args() 

def change_mac(interface,new_mac):#>>>it caries two value that is is interface and new_mac
    #>>> The major concern over her is why we mentioned the interface and new_mac is because the parser is parsing outside the function  
    sb.call(["ifconfig",  interface , "down"])
    sb.call(["ifconfig" , interface , "hw" , "ether",  new_mac])
    sb.call(["ifconfig", interface  ,"up"])
    print("[+] Changeing Mac Address for ",interface + " .......")
    print("[+] Current MAc is changed to ",new_mac )    

(options,arguments) = get_arguments()#>>>here we can just mention options
change_mac(options.interface, options.new_mac)#>>> here the parser is addressing the interface and the new mac as options.interface and options.new_mac 


"""
This Python code is for changing the MAC address of a network interface. Here's a detailed explanation of the code:

The code starts with importing the subprocess module as sb and the optparse module as opt. The subprocess module allows the program to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. The optparse module is used for parsing command-line options.

The get_arguments function is defined to parse the command-line arguments. It creates an instance of OptionParser and adds two options: -i or --interface for specifying the network interface and -m or --mac for specifying the new MAC address. The function then returns the parsed arguments.

The change_mac function is defined to change the MAC address of the specified network interface. It takes two parameters: interface and new_mac. Inside the function, it uses the subprocess.call function to execute terminal commands to bring down the interface, change the MAC address, and bring the interface back up. It also prints messages indicating the MAC address change.

The get_arguments function is called to parse the command-line arguments, and the returned options and arguments are unpacked into options and arguments.

Finally, the change_mac function is called with the interface and new_mac values obtained from the parsed options.

In summary, this code uses the subprocess module to execute terminal commands for changing the MAC address of a network interface based on the command-line arguments provided.

"""
