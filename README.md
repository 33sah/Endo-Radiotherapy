# Endo-Radiotherapy

Geant4 Simulation Code for Endo Radiotherapy Testing. 

Adapted from the MolecularDNA Geant4-DNA example, with a spherical emission of particles to simulate the radionuclide carriers. 



## Installation
 
- Download the files from the GitHub
- Ensure that CMake, Microsoft Visual Studio and Geant4 have been installed, if this is not the case we recommend the following tutorial: [Geant4 Installation](https://youtu.be/GykiM1lPON4?si=QznL75Rlii4i8V60) or the author's other tutorials for your relevant operating system.
- Build the example using CMake, make sure to uncomment the geometry building section if they have not previously been installed and then open project with Visual Studio and build the project.
- Finally build the installation, ensuring to copy the exectuable to your build folder with the relevant macro files.

## Usage

Following the build of the project, run the file using the command:

    ./cancer.exe -m {macro_file} -t {number_of_threads}- p {physics_list}

The macro files available are:
    - Cancer1.mac: For the simulation of cancer cell damage
    - Cancer2.mac For the simulation of fat / pancreatic cell damage
    - Vis.mac for the visualisation of the simulations. This can be run with the other macro files by uncommenting the line:
  
    /control/execute {macro_file}

The physics_list parameter is a choice of numbers between 2 and 6 with the main options being G4EmDNAPhysics_option2, G4EmDNAPhysics_option4 or G4EmDNAPhysics_option6

Option 2 is much more widely used and is significantly less taxing on your computer, but option 4 offers higher precision. Option 6 is unlikely to be used given that it uses more experimental features. 

Python File Generate.py is also available in order to run large numbers of the simulation while altering parameters. 
