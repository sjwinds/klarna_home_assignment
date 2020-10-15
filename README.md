# klarna_home_assignment

What is required to install for this project:

Install Visual Studio Code if not installed

From Visual Studio Code, create a folder "Flask"(you can name it as you like) to store the attached document

Mac, press contrl + tilde or click Terminal


steps:
    1- create virtualenv with the command: 
            pip3 install virtualenv
Running this command creates the target directory called "env". Under "env" ,  a pyvenv.cfg file is placed in it with         a home key pointing to the Python installation from which the command was run. It also creates a bin (or Scripts on           Windows) subdirectory containing a copy of the python binary (or binaries, in the case of Windows). It also creates an (initially empty) lib/pythonX.Y/site-packages subdirectory (on Windows, this is Lib\site-packages).The code is verified only Mac. 

    2- activate the env with source /env/bin/activate 

    3- create sub folder "template' under "Flask" to store document "indexd.html"
    4 - Under folder "Flask", store files, "main_2.py", "fibonacci_n_value.py", "validate_fraction.py" and "ackermann.py"
    5 - Under Terminal, change the directory under "Flask" and run "Python main_2.py"
    6 - open Chrome or Safari, on address line type:localhost:5000

Addtional infomration:
1. __main__ is run under debug mode. Because it is efficient to debug, also I can view status and runtime when I run the code.
2. Because of the heavy computation by ackermann algorithm, m = 3 and n = 7 have been tested. On "indexd.html" the placeholder the form input has shown what number to input. Larger numbers, such as m = 6 and n = 6, have been tested on Jupyter notebook, while it takes very long time and I have cancel the operation.
3. fibonacci and factorial have been tested with large numbers and they are ok.
4. When main_2.py is run, "indexd.html" just shows the calculation result. The validation is shown on Terminal. The reason to do this is to have clear and neat html, also bring directive view to the user.
5. The runtime of 3 math functions is shown on Terminal as well. I have thought about using csv to log the runtime, eventually I decide to show that on Terminal. Because people like to check instantly what is going on. The same for validation, is also shown on Terminal for same purpose.
