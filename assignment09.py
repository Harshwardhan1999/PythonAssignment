#question9
#Script to ping and check whether any given IPs are active, also whether given set of
#software are installed in the existing system ( like java, kubectl, aws etc)

import subprocess
import os
import winapps

def check_ip(ip_address):
    with open(os.devnull, "wb") as limbo:
        result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip_address], stdout=limbo, stderr=limbo).wait()
        if result:
            print (ip_address, "inactive")

        else:
            print (ip_address, "active")


def check_software(software_name):
    for item in winapps.search_installed(software_name):
        print(item)

given_ip='192.168.0.1'
software_name='chrome'
check_ip(given_ip)
check_software(software_name)