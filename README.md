# Power Of 2 Image Resizer - *Optimize Game Engine Textures*

**About**
---

**CURRENTLY WINDOWS ONLY** - *you can still use the python script on any OS if you have the Python and the dependencies installed (pyGame and Pillow), but there is no shell extension, installer, or binary.*

This program resizes images to a power of 2 (256, 512, 1024, 2048, etc.). Many game engines cannot use textures without them being a power of 2. Some game engines will use them with poor optimization and limited features. For example, in Unreal Engine, textures that are not a power of 2 cannot use texture streaming and will appear horribly jarring from a distance.
This program will take an image, find the closest power of 2 (using a user-defined threshold), and resize that image. So an image that is 1080x1200 would be resized (stretched in this case - images are never cut or cropped) to 1024x1024. Then they are ready to be used in a game engine.

As images are not cut or cropped, seemless textures will still be seemless, so no worries.

I made this program for my own use, as when working on game projects, I stumbled across thousands of wonderful free textures. The problem was that basically none of them were power of 2. Some would be 1000x1000 or 1200x1200 for example. So I found myself constantly opening bulky image editing programs, navigating through menus, finding the image resizing tool, manually typing in the new dimensions, and saving it. The whole process taking around 10 clicks and 30 seconds per file (if I was going fast). Going through hundreds of these, let alone thousands, is tedious, mind and finger numbing, and time-consuming. This takes care of everything for you *automatically!*

***How to Use:***

After installing, simply right click on an image file or multiple selected image files and click "Resize Image(s) to Power of 2". Easy! 

@

It will resize all selected images to the closest power of 2. You can also use it from the command line by using any number of images as the parameters.

@

**Supported Image Types:**
* JPG
* PNG
* GIF
* BMP
* TGA*

*Targa files cannot be compressed.

There are more file types supported (anything supported by Pillow) like ICO, but they really won't be used for textures so I won't bother listing them

This program is written in Python and uses [Pillow](https://github.com/python-pillow/Pillow) and [pyGame](https://www.pygame.org/docs/) (for Targa support).

***Installing:***

Just run the po2ir-installer.exe. It contains all dependencies and will be installed in your Program Files in "po2r" folder.
The installer will add the following windows registry keys (needed for right-click context menu resizing):

* HKEY_CLASSES_ROOT\SystemFileAssociations\image\shell\Resize Image(s) to Power of 2
  * MultiSelectModel = Player     (Needed for multiple selected context menu)
* HKEY_CLASSES_ROOT\SystemFileAssociations\image\shell\Resize Image(s) to Power of 2\command
* HKEY_CLASSES_ROOT\SystemFileAssociations\.tga\shell\Resize Image(s) to Power of 2
  * MultiSelectModel = Player     (Needed for multiple selected context menu)
* HKEY_CLASSES_ROOT\SystemFileAssociations\.tga\shell\Resize Image(s) to Power of 2\command

***Uninstalling:***

Run the uninstaller exe in the po2r folder. The uninstaller will also delete the registry keys.
