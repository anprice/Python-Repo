#!usr/bin/python3

import platform
import subprocess
import psutil

def Connectivity_test(specs, host):
    #do a ping test (the command for windows is different than other platforms) 
    
    if specs[0]=='Windows':
        command = ["ping", "-n", "10", host]
    else:
        command = ["ping", "-c", "10", host]
        
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True,  )
        print(result.stdout)
            
    except subprocess.CalledProcessError as err:
        print(f"Error: {err}")
        print(err.stderr)

def Display_info(specs):
    #Print details nicely
    
    print(f"Operating System:\t {specs[0]}")
    print(f"OS version:\t\t {specs[1]}")
    print(f"Computer Name:\t\t {specs[2]}")
    for interface_name, interface_addr in specs[3].items():
        for address in interface_addr:
            if "Wireless" in interface_name:  # Filter WLAN interfaces
                if address.family == psutil.AF_INET:  # IPv4
                    print(f"WLAN Interface: {interface_name}")
                    print(f"  IP Address: {address.addr}")
                    print(f"  MAC Address: {address.addr}")
                    print()
            else:
                print("No interface found")
                break
            break
        break
    

def get_comp_info():
    #Get the os name, version, computer name, and interface information
    os_name = platform.system()
    os_version = platform.version()    
    comp_name = platform.node()
    interface = psutil.net_if_addrs()
    #print(interface) - get the list of interfaces so you can filter based on the name which can be OS specific

    return os_name, os_version, comp_name, interface

if __name__ == "__main__":
    
    
    specs = get_comp_info()
    
    Display_info(specs)
    Connectivity_test(specs, "www.google.com")
    
    
