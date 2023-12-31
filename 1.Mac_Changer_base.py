""" 
This python file is the BASIC module of the MAC address changer for the linux system that work on the basic console commands 
"""
import subprocess as sb
sb.call("ifconfig eth0 down", shell = True)
sb.call("ifconfig eth0 hw ether 00:11:22:33:44:66", shell = True)
sb.call("ifconfig eth0 up", shell = True)