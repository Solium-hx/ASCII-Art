# ASCII_Art Project
# Image Transformation Tool

This is an image transformation tool that gives the user the option to convert any image to a pencil sketch of that image or the ASCII art version of it.

## Requirements
- Python3
- NumPy
```bash
pip install numpy
```
- OpenCV
```bash
pip install opencv-python
```
- Pillow
```bash
pip install Pillow
```

## How to Run
### Follow These steps
1. Make sure all the requirements are complete.
2. Make sure the files start.py, ascify.py, sketchify.py, blockify.py and the folder fonts is in the same directory.
3. Run the start.py python script.
4. On the new window that just opened, click the 'Upload Image' button.
5. Select the desired image you wish to transform.
6. Select the transformation type you want.
7. To save the transformed image, click on the 'Save' button, go to the desired location and save the image.!

### Video Demo

https://user-images.githubusercontent.com/103517557/174804301-229c63ea-5ea8-4b9e-8035-766724576edf.mp4


## Workings

### start.py - Provides GUI using tkinter
- using the filedialog() method in tkinter, the user is asked for path to the image file.
- This path is saved and it becomes the input for any of the transformation feature that the user may require.
- Each of the transformation option returns the transformed image, the size of which is adjusted to fit in the window, and then it is displayed on the user interface.
- The save option uses the filedialog() method to ask for the location and name of the file.

### sketchify.py - Converts image to pencil sketch
- The input image is turned to grayscale image using OpenCV.
- This grayed image is blured out to reduce sharpness.
- now each element in the gray image array is divided by the corresponding element of the blurred-out gray image, this ensures that the sharp features (which are black with the value 0), remain constant while others increase their value to white as they are divided by a smaller number in the corresponding array.
- This becomes the pencil sketch image.

### ascify.py - Converts image to ASCII art
- The output image properties are determined taking the number of columns to be 300
- After determining these properties, a blank image is created which will later be filled with characters
- For of each cell, the selection of character is done by taking the luminosity of that cell, scaling it down to the number of characters that are used, and then taking the character that matches the scaled luminosity among the available characters
- For the color of the cell, the BGR value of each pixel of the cell is averaged out for the area of the cell. This average value becomes the color of the character that will reside in that cell
- Using the PIL.ImageDraw.text() method from Pillow, this character with the color is placed in the cell.

### blockify.py - Converts images to pixel art
- Very similar to ascify.py
- The size of each pixel square block is taken to be 10
- A blank image is created which will later be filled with colored blocks.
- For each block, the BGR value is averaged out, then using the PIL.ImageDraw.rectangle() method from Pillow, the block is filled with this color at the correct block.

## Learnings
- How images are stored in a computer and how to get their properties.
- Image manipulations using OpenCV and Pillow.
- How to use tkinter to provide GUI in python.

## To Dos
- [ ] Improve UI
- [ ] Multiple font options for ASCII Art transformation
- [ ] Multiple character sets for ASCII Art transformation
- [ ] Custom character sets for ASCII Art transformation

## Resources/References
- stackoverflow  - getting reasons for errors and their solution
- geeksforgeeks  - parameters of different functions and their return values
- delftshaft     - general ways to achieve a result
- pillow documentation     - https://pillow.readthedocs.io/en/stable/reference/Image.html
- realpython (for tkinter) - realpython.com/python-gui-tkinter/
