# PyDRAC
Simple Python scripts to query a Dell Poweredge iDRAC.  
Written in Python 2.7.

#Best Practices
The username and password is in plain-text format.  
It may be worth creating a new read-only user on the iDRAC to prevent any unauthorized changes.

# 1 - PyDRACwattage.py
Queries the iDRAC for the current power draw in AC Watts.  
This is a self-contained script in which you must edit the following variables:  
"IDRAC ADDRESS" - The IP address or hostname of the iDRAC  
"IDRAC USERNAME" - The iDRAC username  
"IDRAC PASSWORD" - The iDRAC users password  


