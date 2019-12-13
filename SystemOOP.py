class System:

    """The System object allows you to create a variety of computer systems.

To create a system:

    var = System(name, oem, formfactor, architecture, os, keyboard, mouse)

name - A string variable. Defines the system's name.
oem - A string variable. Defines the OEM manufacturer's name for the system.
formfactor - A string variable. Defines the system's form factor (desktop, laptop, mobile)
architecture - A string variable. Defines the CPU architecture (ARM, i386, amd64, etc)
os - A string variable. Defines the operating system name. (e.g. Windows 10 1903, Ubuntu 16.04 'Xenial Xerus')
keyboard - A boolean variable. Defines whether or not the system features a keyboard.
mouse - A boolean variable. Defines whether or not the system features a mouse.
"""
    
    def __init__(self, name, oem, formfactor, architecture, os, keyboard, mouse):
        '''Defines the object variables.'''
        self.name = str(name)
        self.oem = str(oem)
        self.formfactor = str(formfactor)
        self.architecture = str(architecture)
        self.os = str(os)
        self.keyboard = bool(keyboard)
        self.mouse = bool(mouse)

    def GetInfo(self):
        """Prints out the object variables in a stylised format.
        Example: PC Name's OEM name is PC, using the amd64 architecture and running Windows 7.
        Calls the 'name', 'oem', 'architecture' and 'os' variables."""
        print(self.name + "'s OEM name is " + self.oem + ", using the " + self.architecture + " architecture and running " + self.os + ".")

        """If the system has a keyboard, print the correct message. Ditto for mouse.
        Calls the 'keyboard' and 'mouse' variables."""
        if self.keyboard == True:
            print("A keyboard is connected, and", end=' ')
        else:
            print("A keyboard is not connected, and", end=' ')
            
        if self.mouse == True:
            print("a mouse is connected.", end=' ')
        else:
            print("a mouse is not connected.", end=' ')
            
        """Prints out what form factor the system is in.
        Calls the 'formfactor' variable."""
        print("This system is in a " + self.formfactor + " form factor.\n")

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
