from SystemModule import System
# Import the System module.

# Create the different systems.
RaspberryPi = System('RPi-SYSTEM', 'Raspberry Pi Zero W', 'single-board desktop', 'ARM', 'Raspbian 10 \'Buster\'', False, True)
UbuntuSystem = System('UbuntuPC', 'Dell Precision 5720', 'desktop', 'amd64', 'Ubuntu 19.10 \'Eoan Ermine\'', True, True)
OldDOSpc = System('DOSSYS', 'IBM Personal Computer', 'desktop', 'i386', 'MS-DOS 6.22', True, False)
iPhone7 = System('John\'s iPhone', 'iPhone 7 Plus', 'mobile', 'Apple A10', 'iOS 13.1', False, False)
XPsystem = System('WINDOWS-12FX5', 'Dell Latitude D630', 'laptop', 'amd64', 'Windows XP', True, True)

# Call the GetInfo() function defined in the System object for each object to create.
RaspberryPi.GetInfo()
UbuntuSystem.GetInfo()
OldDOSpc.GetInfo()
iPhone7.GetInfo()
XPsystem.GetInfo()

# Use a function calling System's variables for specific objects without GetInfo().
print("The " + RaspberryPi.oem + " is a " + RaspberryPi.formfactor + " system, while the " + XPsystem.oem + " is a " + XPsystem.formfactor + " system.")
