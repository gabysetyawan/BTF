# Creates a conf file to be read by ConfigParser module

from configparser import ConfigParser

config_object = ConfigParser()

# TODO   We need a DEVICE_LIST to iterate on (has Devices)
#        Devices will have contents modeled in Device.py

# devices we have: BBB and raspberry pi

#Assume we ne need a sections in the config file for the devices, call them DEVICEINFO
config_object["DEVICEINFO"]={
    #fill in required device info here
}

#Write the above section to config.ini file
with open('config.ini', 'w') as conf:
    config_object.write(conf)


*generate_config.py 


