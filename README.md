# pibble
Pibble is a rubble interface for the Raspberry Pi (Model 2 for now)

##Hardware
You will need:
+ Raspberry Pi Model 2
+ MicroSD card w/adapter (if you don't have a microSD card reader)
+ Wi-Fi dongle
+ Ethernet cable

##Dependencies

+ Python 3.4

##Setup (Windows)

###Preparing the microSD card

**Download [Raspbian] (http://www.raspberrypi.org/downloads/)**

![alt text](http://i.imgur.com/KVmTC21.png "Raspbian Download")

It takes a while to download, so get some coffee.

When it is finished downloading, extract the image in your downloads folder by right-clicking and selecting "Extract Here". You can also
drag the image into the downloads folder from the ZIP browser.

**Download [Win32 Disk Imager] (http://sourceforge.net/projects/win32diskimager/) to write the image to the microSD card.**

Select the image file and make sure the correct drive is selected!

![alt text](http://i.imgur.com/1tcICOy.png "Win32 Disk Imager")

When it is completed load it into the Pi.

###Connecting Raspberry Pi to Wi-Fi

There are a ways to setup the Wi-Fi connection on the Raspberry Pi. We will use a headless installation, meaning
there will be no need to hook up the Pi to a monitor over HDMI.