# Despeckle filter for SAR images from Cassini

This repository contains a part of my thesis. Technological Educational Institute Of Athens - Department of Informatics.
The purpose of this thesis is to study the multiplicative noise model and tο develop the
despeckle filter "A despeckle filter for the Cassini synthetic aperture radar images of Titan’s
surface" (Emmanuel Bratsolis, Georgios Bampasidis, Anezina Solomonidou, Athena Coustenis,
2012) using the ISIS3 software.

## Getting Started


### Prerequisites
* Unix-base OS (GNU-Linux)
* Isis3 Installation (https://isis.astrogeology.usgs.gov/documents/InstallGuide/index.html)
* Python 3
* PyQt4


### Installing

A step by step installation guide

Copy/move the main directory (Despeckle_pyqt) to /opt
If it is located to home dir:

```
sudo cp -r ~/Despeckle_pyqt /opt
```

Create a symbolic link to /usr/bin

```
sudo ln -s /opt/Despeckle_pyqt/despeckle_start/sh /usr/bin/despeckle
```

### Using the software
* Using the GUI
```$ despeckle```
* Using as  script 
  * With default values ( l value=0.08, 100 iterations )
   ```$ despeckle input_image kernel.txt out.cub```
  
  * With custom values
  ```$ despeckle input_image kernel.txt out.cub -l 0.08 -i 10```



## Built With

* [ISIS 3](https://isis.astrogeology.usgs.gov/)- Image Processing Software
* [BASH](https://www.gnu.org/software/bash/) - Main shell scripting language
* [Python](https://www.python.org/) - Python v. 3
* [Qt4](http://doc.qt.io/archives/qt-4.8/) -  For the graphical user interface




## Authors

* **Emmanuel Bratsolis, Georgios Bampasidis, Anezina Solomonidou, Athena Coustenis **- *Initial work*  - [A despeckle filter for the Cassini synthetic aperture radar images of Titan's surface(2012)](https://www.sciencedirect.com/science/article/pii/S0032063311001127)



* **Charalampos Mageiridis **- *Thesis*  - [Image processing of SAR data of Titan, from the Cassini spacecraft, using Isis3 and other programming tools"(2015)]()






