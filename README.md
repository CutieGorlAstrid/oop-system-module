# oop-system-module

The System module allows you to create a variety of computer systems.

## Getting started

### Importing the module
`from SystemModule import System`

### Creating a system
`var = System(name, oem, formfactor, architecture, os, keyboard, mouse)`

`name` - A string variable. Defines the system's name.
`oem` - A string variable. Defines the OEM manufacturer's name for the system.
`formfactor` - A string variable. Defines the system's form factor (desktop, laptop, mobile)
`architecture` - A string variable. Defines the CPU architecture (ARM, i36, amd64, etc)
`os` - A string variable. Defines the operating system name. (e.g. Windows 10 1903, Ubuntu 16.04 'Xenial Xerus')
`keyboard` - A boolean variable. Defines whether or not the system features a keyboard.
`mouse` - A boolean variable. Defines whether or not the system features a mouse.

## Functions

### `GetInfo()`

Prints out the objects variables in a stylised format.

##### Example
```
PC Name's OEM name is PC, using the amd64 architecture and running Windows 7. A keyboard is connected, and a mouse is not connected. This system is in a laptop form factor.
```
