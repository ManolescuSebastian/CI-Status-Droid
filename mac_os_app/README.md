# Droid-Status

Control droid servo motors and lights using menu bar application

<img align="center" src="https://github.com/ManolescuSebastian/Droid-Status/blob/master/macOS_app/images/Screenshot%202020-05-26%20at%2022.01.44.png" width="20%">

Libraries
-----

In order to communicate with the Arduino nano I've used **ORSSerial** library.      

More details related to ORSerial - [github source](https://github.com/armadsen/ORSSerialPort/wiki/Installing-ORSSerialPort)

Podfile   

```
platform :macos, '10.15'
use_frameworks!

target 'DroidStatus' do
  project 'DroidStatus'
 	pod "ORSSerialPort"
end

```
  
