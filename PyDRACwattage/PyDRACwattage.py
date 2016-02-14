import subprocess
import re

#opens command shell, runs command and defines result as output
output = subprocess.check_output("racadm -r <IDRAC ADDRESS> -u <IDRAC USERNAME> -p <IDRAC PASSWORD> getconfig -g cfgServerPower -o cfgServerPowerLastMinAvg", shell=True)

#splits lines in output and singles out line with result
#defines line as result
for line in output.split('\n'):
    if 'AC' in line:
		result = line

#splits the result into two strings
wattold, btuold = result.split('|')

#isolates the integer values of the split strings
wattage = int(re.search(r'\d+', wattold).group())
btuhr = int(re.search(r'\d+', btuold).group())

#prints the final results
print 'Wattage:'
print wattage
print ' '
print 'BTU/hr:'
print btuhr