# Modern Analog Clock Project
![Python](https://img.shields.io/badge/Python-v3.9-blue.svg)
![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-Compatible-brightgreen.svg)
![Custom STL](https://img.shields.io/badge/Custom%20STLs-Tinkercad-blue.svg)
![Last Commit](https://img.shields.io/github/last-commit/apjp072/Analog-Servo-Clock)

## Overview
The **Modern Analog Clock** is an innovative timepiece that combines the classic look of an analog display with the precision and flexibility of digital control. Using servos and custom 3D-printed components, this project is a creative blend of engineering and artistry. Originating from [O.T. Vinta's project](https://www.otvinta.com/download14.html), it has been enhanced with additional features to improve user interaction and functionality.

## Key Features
- **Servo Position Adjustment:** Easy tuning of servo start and end positions using keyboard arrow keys, negating the need for a costly Maestro Control board as suggested on O.T. Vinta's website.
- **Wifi Connectivity:** Automatic wifi connection upon plugging in, removing the need for a mouse and keyboard setup.
- **Hourly Animation:** Eye-catching servo "animation" marking the hour by opening and closing all servos 3 times.
- **Improved STL Design:** Reworked 'shoe' designs for a snap-fit attachment to the black understructure, eliminating the need for glue.

## Technologies and Tools
This project is built using various technologies and tools:
- **Python:** The core programming language used for writing the clock's logic and control scripts.
- **ServoKit Library:** To interface with the servos via a Raspberry Pi.
- **Custom 3D Printing:** I designed updated "shoes" that can snap-fit onto the parts rather than needing to be glued.

## Getting Started
To get started with your own Modern Analog Clock, you'll need a Raspberry Pi, a set of servos, and the ability to print from the provided STL files. Clone this repository and follow the setup instructions to install the necessary libraries and deploy the code.

## Installation
1. Clone the repository to your Raspberry Pi.
2. Install the `adafruit_servokit` library using pip.
3. Execute the provided Python script to start the clock.

## Contributions
Contributions are what make the open-source community such a fantastic place to learn, inspire, and create. Any contributions you make are **greatly appreciated**. If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

## Acknowledgments
- [O.T. Vinta](https://www.otvinta.com/download14.html) for the original model and inspiration.
- The open-source community for continuous collaboration and support.
