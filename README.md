# IMPORTANT
This code is very old. I was dipping my feet into Python at the time. This will be revised soon.

# PyDRAC
- Simple Python scripts to query a Dell Poweredge iDRAC.  
  Written in Python 2.7.

#Best Practices
- The username and password is in plain-text format.  
  It may be worth creating a new read-only user on the iDRAC to prevent any unauthorized changes.

#Prerequisites
- DELL RACADM is required on the device running the script.  
  Visit DELL support site and download the OpenManage utility to install RACADM.  

#Future Plans
- Create "PyDRACtemperature.py" for temperature monitoring.
- Create "PyDRACfanspeed.py" for fan speed monitoring.
- Modify scripts to return JSON and XML values.
- Create CACTI template.
- Create PRTG sensor script.

# 1 - PyDRACwattage.py
Queries the iDRAC for the current power draw in AC Watts.  
This is a self-contained script in which you must edit the following variables:  
- "IDRAC ADDRESS" - The IP address or hostname of the iDRAC  
- "IDRAC USERNAME" - The iDRAC username  
- "IDRAC PASSWORD" - The iDRAC users password  


