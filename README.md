# CHANGE MATRIX FOR COMPETING PRIORITIES AND DEMANDS
This project provides structures in the integration of competing demands and priorities during change implementation.
These integrations are abstracted into nodes of a graph data structure and different types of links between them.
Data structures hold information collected on nodes and relationships may be created for temporary or permanent use.
For example, the dependency table is used to record information on nodes and their dependencies.

### Integrating competing priorities and demands
In order to handle competing demands in an orderly fashion, we use the change matrix.
The vertical axis partitions the expected artifacts from the change process into processes (operations) or structures
 (components).
The factors on the horizontal axis corresponds to the broad dimensions (categories) of change sources identified.
The change process addresses them and so shape the artifacts obtained.
They represent abstractions and viewpoints that the change process, as a socio-technical system, must address and so 
help localise effort and focus.
Models, architectures and frameworks, and standards and protocols are the supporting instrucments used to effect change,
even if they have to be developed for, or adapted, to new scenarios.
 
### Installation of software
Most Operating systems have Python 3 pre-installed. Ensure that Python 3 is installed in your system.
```
$ python --version
$ pip --version 
```
Check www.python.org for downloading and installation instructions if your system does not have Python 3 installed.

### Run software
```
$ python main.py
```

### Packaging software
If you want a single executable file which you can run on other computers without the need to install Python.
You can install *pyinstaller* module which helps bundle your application into a single executable.
```
$ pip install pyinstaller
$ pyinstaller main.py
```
This will package your application for the OS which your using.