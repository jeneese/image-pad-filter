# Applying Padding and Filter to an image

This program first applies a user-selected padding to an image followed by a user-selected filter.

## Installation

Use the package manager pip to install Opencv and Numpy

```bash
pip install opencv-python
pip install numpy
```

## Usage

After running the program in Python, several prompts will appear.

```
Type the path with file extension of the image file you'd like to test:
```

Enter an absolute or relative path for your image.

```
1 - Box Filter
2 - First Order Derivative Filter - Horizontal
3 - First Order Derivative Filter - Vertical
4 - Prewitt - Mx
5 - Prewitt - My
6 - Sobel - Mx
7 - Sobel - My
8 - Roberts - Mx
9 - Roberts - My
Type a number for the filter you'd like to select:
```

Enter a number between 1 and 8 to represent the filter you would like to apply to the image. Based on the selected filer, a kernel will be generated that evaluates each pixel within the kernel.  
The First Order Derivative Filter is a kernel of [-1,1] for Horizontal or [[-1],[1]] for Vertical
The following articles provide more information about each of the other filter types:  
[Box Filter](https://en.wikipedia.org/wiki/Box_blur)  
[Prewitt](https://en.wikipedia.org/wiki/Prewitt_operator)  
[Sobel](https://en.wikipedia.org/wiki/Sobel_operator)  
[Roberts](https://en.wikipedia.org/wiki/Roberts_cross)  
Mx refers to horizontal derivative of the filter and My refers to vertical derivative of the filter.

```
1 - Clip/Zero padding
2 - Wrap Around
3 - Copy Edge
4 - Reflect Across Edge
Type a number for the padding you'd like to select:
```

Enter a number between 1 and 4 to represent the padding you would like on the image before the filter is applied.  
Clip/Zero padding evaluates all pixels outside of the image as 0.  
Wrap Around evaluates all pixels outside of the image from the opposite side of the image.
Copy Edge evaulates all pixels outside of the image as the closest adjacent pixel.
Reflect Across Edge will evaluate all pixels outside of the image as a reflection of the closest adjacent pixels.

The program will then begin to evaluate the image and apply padding based on the selection. An image will be displayed of the image with the applied padding.

Once the image is closed, an image will be displayed of the selected filter applied to the padded image.
