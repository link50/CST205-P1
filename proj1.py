#Matt Guyadeen
#CST205-02
#2/7/17

#Learn Python
#How to work with pictures
#red-value -> red-variable, blue -> blue, green -> green?


from PIL import Image           #Start by importing all images from the project file
Img1 = Image.open('1.png')
Img2 = Image.open('2.png')
Img3 = Image.open('3.png')
Img4 = Image.open('4.png')
Img5 = Image.open('5.png')
Img6 = Image.open('6.png')
Img7 = Image.open('7.png')
Img8 = Image.open('8.png')
Img9 = Image.open('9.png')

photoList = [Img1, Img2, Img3, Img4, Img5, Img6, Img7, Img8, Img9]      #Create an array of all the images

width, height = photoList[0].size       #Find the dimensions of the images


def median(myList):
    median = 0
    sortedList = sorted(myList)
    listLength = len(sortedList)
    listCenter = listLength / 2
    if len(sortedList) == 1:
        for value in sortedList:
            median += value
        return median

    elif len(sortedList) % 2 == 0:
        temp = 0.0
        medianparties = []
        medianparties = sortedList[listCenter -1 : listCenter +1 ]
        for value in medianparties:
            temp += value
            median = temp / 2
        return median

    else:
        medianpart = []
        medianpart = [sortedList[listCenter]]
        for value in medianpart:
            median = value
        return median
        
redPixelList = []           #Create arrays to store color values of each pixel
greenPixelList = []
bluePixelList = []

pic = Image.new("RGB", (width, height))     #Create a new image to store median values of each pixel

for x in range(0, width):
    for y in range(0, height):    
        for picture in photoList:
            myRed, myGreen, myBlue = picture.getpixel((x,y))
            redPixelList.append(myRed)
            greenPixelList.append(myGreen)
            bluePixelList.append(myBlue)
                   
        medianRed = median(redPixelList)
        medianGreen = median(greenPixelList)# median of the pixelisted
        medianBlue = median(bluePixelList)
        
        pic.putpixel((x,y), (medianRed, medianGreen, medianBlue))
        
        redPixelList =[]
        greenPixelList =[]
        bluePixelList = []


pic.save("10.png")