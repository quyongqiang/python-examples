====
Menu
====

Menu is used for easily creating command-line menus.

Included Files
==============

* menu/menu.py
  - python module used for creating command-line menus


Installation
============

Python must be installed in order for Menu to be imported. Install python at https://www.python.org/download/. In the terminal type “cd path/to/this/directory” and then “python setup.py install”. This will add the menu module to your site-packages.


How to Use
==========

Import menu
-----------

Import::

	import menu


Create a Menu
-------------

The Menu constructor takes one non-optional argument, the title, and one optional argument, an update function that gets called every time the menu is show::

	mainMenu = menu.Menu(title,update=updateFunction)

To make a submenu make a property of the main menu another menu::

	mainMenu.submenu = menu.Menu(title,update=updateFunction)

Add options to a menu::

	options = [{"name":"firstOption","function":firstFunc},
	           {"name":"secondOption","function":secondFunc},
	           {"name":"thirdOption","function":thirdFunc}]
	mainMenu.addOptions(options)

Change the way options are added to a menu::

	mainMenu.explicit()
	options = [{"name":"firstOption","function":firstFunc},
		   {"name":"secondOption","function":secondFunc},
		   {"name":"thirdOption","function":thirdFunc}]
	mainMenu.addOptions(options)
	
	mainMenu.clearOptions()
	
	mainMenu.implicit()
	options = [("firstOption",firstFunc),
                   ("secondOption",secondFunc),
                   ("thirdOption",thirdFunc)]
	mainMenu.addOptions(options)

Display a menu, wait for user input, and call a corresponding function::

	mainMenu.open()
	
	###
	would look like this
	
	title
	
	1. firstOption
	2. secondOption
	3. thirdOption
	
	>>>
	###

Change the user input indicator::

	mainMenu.indicator(":")
	mainMenu.indicator(">>>")
	mainMenu.indicator(">")

	


