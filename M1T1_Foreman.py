# CSC-221-0001
# M1T1_Foreman
# Goal: Gold


# Author: William Foreman
# The program should ask the user for three pieces of information: 
# The length of the fishing pole
# The length of the box
# The width of the box 
#
# The program should then calculate the hypotenuse of a right triangle whose 
#sides match the size of the box. 
#
# It should tell the user that value (which is the largest fishing pole you 
#could place in the box diagonally). 
#
# And finally, it should tell the user whether or not their fishing pole will 
#fit in the box they specified.
#
#
import math

fishingPoleHeight = float(input('Please enter the Length of the Fishingpole: '))
boxLength = float(input('Please enter the Length of the Box: '))
boxWidth = float(input('Please enter the Width of the Box: '))

# Calculate the Hypotenuse (Third Side and Longest Side of the Triangle)
maxFishingPoleHeight = math.sqrt((boxWidth*boxWidth) + (boxLength*boxLength))

# Display the hypotenuse
print("The longest fishingpole you can put in your box is: %.2f" %maxFishingPoleHeight)

# Calculate whether or not the fishingpole will fit in the box
if fishingPoleHeight <= maxFishingPoleHeight:
    print("Your Fishingpole will fit in this box.")
else:
    print("Your Fishingpole will not fit in this box.")








