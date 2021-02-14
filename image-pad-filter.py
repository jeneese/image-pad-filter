import cv2
import numpy as np

def conv2(f, w, pad):
    """  Function performs convolution between the image and kernel. Padding is also added before convolution.
     params:
        f: the input image selected by the user
        w: the kernel selected by the user
        pad: the type of padding selected by the user
     """

    image = f
    imageWidth = image.shape[1]  #Saves the number of horizontal pixels to imageWidth
    imageHeight = image.shape[0]  #Saves the number of vertical pixels to imageHeight

    kernel = w

    padSelection = pad

    padImage = np.zeros((imageHeight + 6, imageWidth + 6, 3), np.uint8) #padded image has a 3 pixel border and filled with black pixels
    padImageWidth = padImage.shape[1]  #Saves the number of horizontal pixels to padImageWidth
    padImageHeight = padImage.shape[0]  #Saves the number of vertical pixels to padImageHeight

    xPosition = 0
    yPosition = 0

    #The pixel value of each column and row in the orignal image is added to the corresponding location in the padded image
    while (xPosition < imageWidth):  # Loops through each row
        while (yPosition < imageHeight):  # Loops through each column
            padImage[yPosition+3][xPosition+3] = image[yPosition][xPosition]
            yPosition = yPosition + 1
        yPosition = 0
        xPosition = xPosition + 1

    if(padSelection == '1'):
        cv2.imshow('Padded Image', padImage)  # Displays the padded image and displays the image as 'Padded Image'
        cv2.waitKey(0)  # Sets no expiration on the displayed image
        print("Please wait...")

    #If padSelection = 2, the border is filled with pixels on opposite sides of the image
    if (padSelection == '2'):
        padImageUpdate = np.copy(padImage)
        #Top and bottom borders are updated first
        padImageUpdate[[0,1,2], :] = padImage[[padImageHeight-6, padImageHeight-5, padImageHeight-4], :]
        padImageUpdate[[padImageHeight-3, padImageHeight-2, padImageHeight-1], :] = padImage[[3, 4, 5], :]
        #Left and right borders are updated after
        padImageUpdate[:, [0,1,2]] = padImageUpdate[:, [padImageWidth-6, padImageWidth-5, padImageWidth-4]]
        padImageUpdate[:, [padImageWidth-3, padImageWidth-2, padImageWidth-1]] = padImageUpdate[:, [3, 4, 5]]
        padImage = np.copy(padImageUpdate)
        cv2.imshow('Padded Image', padImage)  # Displays the padded image and displays the image as 'Padded Image'
        cv2.waitKey(0)  # Sets no expiration on the displayed image
        print("Please wait...")


    #If padSelection is 3, image is filled in padImage and the border is filled with the image pixel closest to the border
    if(padSelection == '3'):
        padImageUpdate = np.copy(padImage)
        # Top and bottom borders are updated first
        padImageUpdate[[0,1,2], :] = padImage[[3], :]
        padImageUpdate[[padImageHeight - 3, padImageHeight - 2, padImageHeight - 1], :] = padImage[[padImageHeight-4], :]
        # Left and right borders are updated after
        padImageUpdate[:, [0,1,2]] = padImageUpdate[:, [3]]
        padImageUpdate[:, [padImageWidth - 3, padImageWidth - 2, padImageWidth - 1]] = padImageUpdate[:, [padImageWidth-4]]
        padImage = np.copy(padImageUpdate)
        cv2.imshow('Padded Image', padImage)  # Displays the padded image and displays the image as 'Padded Image'
        cv2.waitKey(0)  # Sets no expiration on the displayed image
        print("Please wait...")

    # If padSelection is 4, image is filled in padImage and the border is filled with adjacent pixels in the image
    if(padSelection == '4'):
        padImageUpdate = np.copy(padImage)
        # Top and bottom borders are updated first
        padImageUpdate[[0,1,2], :] = padImage[[5,4,3], :]
        padImageUpdate[[padImageHeight - 3, padImageHeight - 2, padImageHeight - 1], :] = padImage[[padImageHeight - 4, padImageHeight - 5, padImageHeight - 6], :]
        # Left and right borders are updated after
        padImageUpdate[:, [0,1,2]] = padImageUpdate[:, [5,4,3]]
        padImageUpdate[:, [padImageWidth - 3, padImageWidth - 2, padImageWidth - 1]] = padImageUpdate[:, [padImageWidth - 4, padImageWidth - 5, padImageWidth - 6]]
        padImage = np.copy(padImageUpdate)
        cv2.imshow('Padded Image', padImage)  # Displays the padded image and displays the image as 'Padded Image'
        cv2.waitKey(0)  # Sets no expiration on the displayed image
        print("Please wait...")

    output = np.copy(image) #The original image is copied to output
    image = np.copy(padImage) #The padded image is copied to image for processing

    imageWidth = image.shape[1]  #Saves the new number of horizontal pixels from the padded image
    imageHeight = image.shape[0]  #Saves the new number of vertical pixels from the padded image

    xPosition = 0
    yPosition = 0

    if(kernel.shape == (3,3)):
        while (xPosition < imageWidth):  # Loops through each row
            while (yPosition < imageHeight):  # Loops through each column

                #Since image now contains the padded image, evaluation starts at (3,3)
                if (xPosition > 2 and xPosition < imageWidth - 3):
                    if (yPosition > 2 and yPosition < imageHeight - 3):

                        #The upper set of pixels are evaluated against the kernel values
                        blueUpper = image[yPosition - 1, xPosition - 1, 0] * kernel[0][0] + image[yPosition - 1, xPosition,0] * kernel[0][1] + image[yPosition - 1, xPosition + 1,0] * kernel[0][2]
                        #The middle set of pixels are evaluated against the kernel values
                        blueMiddle = image[yPosition, xPosition - 1,0] * kernel[1][0] + image[yPosition, xPosition,0] * kernel[1][1] + image[yPosition, xPosition + 1,0] * kernel[1][2]
                        #The bottom set of pixels are evaluated against the kernel values
                        blueBottom = image[yPosition + 1, xPosition - 1,0] * kernel[2][0] + image[yPosition + 1, xPosition,0] * kernel[2][1] + image[yPosition + 1, xPosition + 1,0] * kernel[2][2]
                        #The results are summed together and blue is set to the appropriate value if it is greater than 255 or less than 0
                        blue = (blueUpper + blueMiddle + blueBottom)
                        if(blue>255):
                            blue = 255
                        if(blue<0):
                            blue = 0
                        #The pixel in output is updated with the number generated and the process is repeated for green and red
                        output[yPosition-3, xPosition-3, 0] = int(blue)


                        greenUpper = image[yPosition - 1, xPosition - 1, 1] * kernel[0][0] + image[yPosition - 1, xPosition, 1] * kernel[0][1] + image[yPosition - 1, xPosition + 1, 1] * kernel[0][2]
                        greenMiddle = image[yPosition, xPosition - 1, 1] * kernel[1][0] + image[yPosition, xPosition, 1] * kernel[1][1] + image[yPosition, xPosition + 1, 1] * kernel[1][2]
                        greenBottom = image[yPosition + 1, xPosition - 1, 1] * kernel[2][0] + image[yPosition + 1, xPosition, 1] * kernel[2][1] + image[yPosition + 1, xPosition + 1, 1] * kernel[2][2]
                        green = (greenUpper + greenMiddle + greenBottom)
                        if (green > 255):
                            green = 255
                        if (green < 0):
                            green = 0
                        output[yPosition-3, xPosition-3, 1] = int(green)

                        redUpper = image[yPosition - 1, xPosition - 1, 2] * kernel[0][0] + image[yPosition - 1, xPosition, 2] * kernel[0][1] + image[yPosition - 1, xPosition + 1, 2] * kernel[0][2]
                        redMiddle = image[yPosition, xPosition - 1, 2] * kernel[1][0] + image[yPosition, xPosition, 2] * kernel[1][1] + image[yPosition, xPosition + 1, 2] * kernel[1][2]
                        redBottom = image[yPosition + 1, xPosition - 1, 2] * kernel[2][0] + image[yPosition + 1, xPosition, 2] * kernel[2][1] + image[yPosition + 1, xPosition + 1, 2] * kernel[2][2]
                        red = (redUpper + redMiddle + redBottom)
                        if (red > 255):
                            red = 255
                        if (red < 0):
                            red = 0
                        output[yPosition-3, xPosition-3, 2] = int(red)

                yPosition = yPosition + 1
            yPosition = 0
            xPosition = xPosition + 1

    if (kernel.shape == (2,2)):
        while (xPosition < imageWidth):  # Loops through each row
            while (yPosition < imageHeight):  # Loops through each column

                # Since image now contains the padded image, evaluation starts at (3,3)
                if (xPosition > 2 and xPosition < imageWidth - 3):
                    if (yPosition > 2 and yPosition < imageHeight - 3):

                        # The upper set of pixels are evaluated against the kernel values
                        blueUpper = image[yPosition - 1, xPosition - 1, 0] * kernel[0][0] + image[yPosition - 1, xPosition, 0] * kernel[0][1]
                        # The bottom set of pixels are evaluated against the kernel values
                        blueBottom = image[yPosition, xPosition - 1, 0] * kernel[1][0] + image[yPosition, xPosition, 0] * kernel[1][1]
                        # The results are summed together and blue is set to the appropriate value if it is greater than 255 or less than 0
                        blue = (blueUpper + blueBottom)
                        if (blue > 255):
                            blue = 255
                        if (blue < 0):
                            blue = 0
                        # The pixel in output is updated with the number generated and the process is repeated for green and red
                        output[yPosition-3, xPosition-3, 0] = int(blue)

                        greenUpper = image[yPosition - 1, xPosition - 1, 1] * kernel[0][0] + image[yPosition - 1, xPosition, 1] * kernel[0][1]
                        greenBottom = image[yPosition, xPosition - 1, 1] * kernel[1][0] + image[yPosition, xPosition, 1] * kernel[1][1]
                        green = (greenUpper + greenBottom)
                        if (green > 255):
                            green = 255
                        if (green < 0):
                            green = 0
                        output[yPosition-3, xPosition-3, 1] = int(green)

                        redUpper = image[yPosition - 1, xPosition - 1, 2] * kernel[0][0] + image[yPosition - 1, xPosition, 2] * kernel[0][1]
                        redBottom = image[yPosition, xPosition - 1, 2] * kernel[1][0] + image[yPosition, xPosition, 2] * kernel[1][1]
                        red = (redUpper + redBottom)
                        if (red > 255):
                            red = 255
                        if (red < 0):
                            red = 0
                        output[yPosition-3, xPosition-3, 2] = int(red)

                yPosition = yPosition + 1
            yPosition = 0
            xPosition = xPosition + 1

    if (kernel.shape == (1,2)): #For First Order Derivative Horizontal Filter
        while (xPosition < imageWidth):  # Loops through each row
            while (yPosition < imageHeight):  # Loops through each column

                # Since image now contains the padded image, evaluation starts at (3,3)
                if (xPosition > 2 and xPosition < imageWidth - 3):
                    if (yPosition > 2 and yPosition < imageHeight - 3):

                        # The left neighbor and the current pixel are evaluated
                        blue = image[yPosition, xPosition - 1, 0] * kernel[0][0] + image[yPosition, xPosition, 0] * kernel[0][1]
                        if (blue > 255):
                            blue = 255
                        if (blue < 0):
                            blue = 0
                        # The pixel in output is updated with the number generated and the process is repeated for green and red
                        output[yPosition-3, xPosition-3, 0] = int(blue)

                        green = image[yPosition, xPosition - 1, 1] * kernel[0][0] + image[yPosition, xPosition, 1] * kernel[0][1]
                        if (green > 255):
                            green = 255
                        if (green < 0):
                            green = 0
                        output[yPosition-3, xPosition-3, 1] = int(green)

                        red = image[yPosition, xPosition - 1, 2] * kernel[0][0] + image[yPosition, xPosition, 2] * kernel[0][1]
                        if (red > 255):
                            red = 255
                        if (red < 0):
                            red = 0
                        output[yPosition-3, xPosition-3, 2] = int(red)

                yPosition = yPosition + 1
            yPosition = 0
            xPosition = xPosition + 1

    if (kernel.shape == (2,1)): #For First Order Derivative Vertical Filter
        while (xPosition < imageWidth):  # Loops through each row
            while (yPosition < imageHeight):  # Loops through each column

                # Since image now contains the padded image, evaluation starts at (3,3)
                if (xPosition > 0 and xPosition < imageWidth - 3):
                    if (yPosition > 0 and yPosition < imageHeight - 3):

                        # The upper pixel is evaluated against the kernel value
                        blueUpper = image[yPosition - 1, xPosition - 1, 0] * kernel[0][0]
                        # The bottom pixel is evaluated against the kernel value
                        blueBottom = image[yPosition, xPosition - 1, 0] * kernel[1][0]
                        # The results are summed together and blue is set to the appropriate value if it is greater than 255 or less than 0
                        blue = (blueUpper + blueBottom)
                        if (blue > 255):
                            blue = 255
                        if (blue < 0):
                            blue = 0
                        # The pixel in output is updated with the number generated and the process is repeated for green and red
                        output[yPosition-3, xPosition-3, 0] = int(blue)

                        greenUpper = image[yPosition - 1, xPosition - 1, 1] * kernel[0][0]
                        greenBottom = image[yPosition, xPosition - 1, 1] * kernel[1][0]
                        green = (greenUpper + greenBottom)
                        if (green > 255):
                            green = 255
                        if (green < 0):
                            green = 0
                        output[yPosition-3, xPosition-3, 1] = int(green)

                        redUpper = image[yPosition - 1, xPosition - 1, 2] * kernel[0][0]
                        redBottom = image[yPosition, xPosition - 1, 2] * kernel[1][0]
                        red = (redUpper + redBottom)
                        if (red > 255):
                            red = 255
                        if (red < 0):
                            red = 0
                        output[yPosition-3, xPosition-3, 2] = int(red)

                yPosition = yPosition + 1
            yPosition = 0
            xPosition = xPosition + 1

    return output



def main(): #Main begins
    file = input("Type the path with file extension of the image file you'd like to test:") #User enter .png file for testing
    image = cv2.imread(file) #Saves the image input typed in by the user to image

    print("1 - Box Filter")
    print("2 - First Order Derivative Filter - Horizontal")
    print("3 - First Order Derivative Filter - Vertical")
    print("4 - Prewitt - Mx")
    print("5 - Prewitt - My")
    print("6 - Sobel - Mx")
    print("7 - Sobel - My")
    print("8 - Roberts - Mx")
    print("9 - Roberts - My")
    kernelSelection = input("Type a number for the filter you'd like to select:") #Options for filter selection are offered above and user enters a number to select

    #The two functions below were used for testing greyscale images
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)

    #Kernels are generated below based on the user selection.
    if(kernelSelection == '1'):
        kernel = np.array([[1,1,1], [1,1,1], [1,1,1]]) / 9

    if (kernelSelection == '2'):
        kernel = np.array([[-1, 1]])

    if (kernelSelection == '3'):
        kernel = np.array([[-1], [1]])

    if (kernelSelection == '4'):
        kernel = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])

    if (kernelSelection == '5'):
        kernel = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])

    if (kernelSelection == '6'):
        kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

    if (kernelSelection == '7'):
        kernel = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

    if (kernelSelection == '8'):
        kernel = np.array([[0, 1], [-1, 0]])

    if (kernelSelection == '9'):
        kernel = np.array([[1, 0], [0, -1]])

    print("1 - Clip/Zero padding")
    print("2 - Wrap Around")
    print("3 - Copy Edge")
    print("4 - Reflect Across Edge")
    padSelection = input("Type a number for the padding you'd like to select:") #User selects padding they would like to use

    output = conv2(f=image, w=kernel, pad=padSelection) #conv2 function with image, kernel, and padding as inputs

    cv2.imshow('Filtered image', output)  # Displays the image received after conv2 is executed and titles the image 'Filtered Image'
    cv2.waitKey(0)  # Sets no expiration on the displayed image

if __name__ == "__main__":
    main()