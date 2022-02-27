# Password-Generator

reused old project to create a password generator with a gui using PySimpleGui.

V0.02
 - BUGS

 - CHANGES:
	- Added tool tips to Password Length and Copy to Clipboard
	- Added feedback messages to users




V0.01
 - BUGS
	- There was no input validation
	- Password lengths have no limit
	- if fields are blank, program crashes
		- example.... making the "password length" input field blank, program crashes and command line provides error:
			Traceback (most recent call last):
			  File "D:\Programming\Programming\Python\Projects\Password Generator\v0.02\passgengui.py", line 58, in <module>
    				elif int(values['-b-']) > int(values['-d-']):
			ValueError: invalid literal for int() with base 10: ''
