#SPACE MONKEYS: The Mars Experience 

<img src="http://i.imgur.com/1d71AMV.png" />

## [Challenge description](https://2016.spaceappschallenge.org/challenges/solar-system/open-world-generation-using-nasa-mars-and-vesta-data) ![NASA Space Apps Challenge 2016](http://i.imgur.com/0xwKStM.png)

> ####Open World Generation using NASA Mars and Vesta Data

> **#openworldgeneration**

> Create a custom world map generator module using a gaming framework or engine of your choice that leverages altimeter, terrain and imagery data to render realistic worlds.  This will involve the use of a World Map Tile Service client to leverage over 1 TB of Mars and Vesta data for use in world generation.

#Bring it on!

## The idea

![Workflow](http://i.imgur.com/TWVXP8Z.png "Workflow")

## How we solved it

Over the course of the 48-hour challenge, we created an immersive experience using Google Cardboard and Unity3D to recreate Mars in virtual reality enviroment. Now **everyone can enjoy Mars**! [*](http://i.imgur.com/BT9tNyH.jpg)

The Virtual Red Planet was constructed using the terrain and map information extracted from Mars Trek WMTS Layer Service and JPT Maps. To make the experience educational we added information about the Moons of Mars and the Sun. The martian weather was created based on the data transmitted by the Curiosity Rover on Mars! We also added the Curiosity Rover as a 3D object to show info about it. You can even see the last image taken from [the real rover](http://i.imgur.com/SF302fs.jpg).

## Technical aspects

#### Accessing the WMTS Layer services

![Scripts Explained](http://i.imgur.com/BEdy1Qt.png)
This one is simple, but when you can not count on the internet service it might get a little tricky. So, we decided to make some python scripts to [get the tiles from the service](https://i.imgflip.com/139xde.jpg) and store them in our PC. With all the tiles in our file system, we then used [Image Magick](https://www.imagemagick.org/) to merge them all together to create our realistic texture. Script and textures available in **Scripts folder**

#### Running the app in crappy phones

Not all of us have [good phones](http://i.imgur.com/KGNwFN9.jpg). In order to make the app more accesible to everyone, we used the PC as main processor and then stream the contents to the phone. This allowed us to get a much better quality in our 3D models and terrain. The only setback is that the PC and the phone need to be on the same WiFi network.

##What we used from NASA

- [Mars Trek API](https://api.nasa.gov/mars-wmts/catalog/) - MAPS!
- [Jet Propulsion Laboratory](http://jpl.nasa.gov/) - [Maps](http://maps.jpl.nasa.gov/) and [Curiosity JSON feed](http://mars.jpl.nasa.gov/msl-raw-images/image/image_manifest.json)
- [Mars Global Surveyor - MOLA MEGDRs](http://pds-geosciences.wustl.edu/missions/mgs/megdr.html) - Heightmap/DEM for terrain references
- [Rover Environmental Monitoring Station - Centro de Astrobiologia (CSIC-INTA)](http://marsweather.ingenology.com/) - Mars Weather!
- [SoundCloud NASA](https://soundcloud.com/nasa) - Sounds!
- [NASA Solar System Exploration](https://solarsystem.nasa.gov/) - Planets info
- [NASA 3D Resources](http://nasa3d.arc.nasa.gov/) - 3D Models

##Other resources

- [Unity3D](https://unity3d.com/) - 3D Engine
- [Google Cardboard](https://www.google.com/get/cardboard/) - VR interface
- [Celestia Motherlode](http://www.celestiamotherlode.net/catalog/marsmoons.php) - 3D Models
- [JHT's Planetary Pixel](http://planetpixelemporium.com/mars.html) - Additional textures
- [TrinusVR](http://trinusvr.com/) - Connectivity (PC <-> Phone)


## Try it now on PC
 - `git-checkout` the **Demo folder** or download it from [our drive](https://drive.google.com/drive/u/0/folders/0B6HqfNqiajKVRVkzN1Y0SFhISXc)
 - Run **MarsExperience.exe** and enjoy!

## Try it with VR
 - `git-checkout` the **Demo folder** or download it from [our drive](https://drive.google.com/drive/u/0/folders/0B6HqfNqiajKVRVkzN1Y0SFhISXc)
 - Download and install TrinusVR [on your PC](http://trinusvr.com/) and [your smart phone](https://play.google.com/store/apps/details?id=com.loxai.trinus.test&hl=es_419). _(both must be **on the same WiFi network**)_
 - Start Trinus on your PC.
 - Run the recently checked out **MarsExperience.exe**
 - Make sure to check `[x] Windowed` and **hit Play!**
 - On your phone open Trinus, then place it in your [favorite VR kit](https://www.google.com/get/cardboard/)
 - **Enjoy the magic!**

## The money shot

<img src="http://i.imgur.com/F4MwGhs.jpg" width="800" />

##### Want to see more? [Gallery #1](http://imgur.com/a/euFz9) - [Gallery #2](http://imgur.com/a/B9t2J)

## Look into the future 

We choose **#openworldgeneration** challenge because we want all of you to live ***THE MARS EXPERIENCE***. Travel further than you ever have without leaving your room. Experience and learn about Mars in first person without difficulty, hazard or any inconvenience. ~~[In your face Matt Damon!](http://i.imgur.com/4zw8u9M.jpg)~~

### Mars is just the beginning. We have a whole universe to explore, and we don't even need to be astronauts!

___

## The monkeys

|   |
|---|
| <a href="mailto:lucianorighetti@gmail.com">![Luciano Righetti](http://i.imgur.com/Sowv9wH.png "Luciano") Luciano Righetti</a> is a monkey engineer and photographer. Works @ Fuerza Aérea Argentina |
| <a href="mailto:pmprete@gmail.com">![Pedro Prete](http://i.imgur.com/Sowv9wH.png "Pedro") Pedro Prete</a> is a monkey developer who's always looking for the next big thing. Works @ Kinetica Solutions |
| <a href="mailto:martinprete@gmail.com">![Martin Prete](http://i.imgur.com/Sowv9wH.png "Martin") Martin Prete</a> is a code wielding monkey. Works @ Fuerza Aérea Argentina |
|   |
