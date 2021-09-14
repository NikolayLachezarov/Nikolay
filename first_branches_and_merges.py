#This is for group 2 and 3 to learn how to use github source control, branching and merging
#I have specific challenge for each person
'''Each person will:
*clone the repo
*make a branch named after themselves
*use several commits to show progress on branch
*test that your function works and print results
*add a file named after youself that you are proud to share
*make a pull request for it to be merged to main branch
'''




#Challenge for Tomy
# https://edabit.com/challenge/Y5Ji2HDnQTX7MxeHt























#Challenge for William
# https://edabit.com/challenge/eADRy5SA5QbasA3Qt























#Challenge for Geogrs
# https://edabit.com/challenge/Aj377wZtxWya7gjK9























#Challenge for Nikolay
# https://edabit.com/challenge/fNQEi9Y2adsERgn98

from math import sqrt

def perimator(point1, point2, point3):
    # I will need to calaculate the distance of the actuall points 
    # the formula d = √(xy - x1)^2 + (y2 - y1)^2 will do it
    d1 = sqrt((point[1][0] - point[0][0]) ** 2 +
              (point[1][1] - point[0][1]) ** 2)
    d2 = sqrt((point[2][0] - point[1][0]) ** 2 +
              (point[2][1] - point[1][1]) ** 2)
    d3 = sqrt((point[0][0] - point[1][0]) ** 2 +
              (point[0][1] - point[1][1]) ** 2)
    return d1 + d2 + d3


print(perimator([[15, 7], [5, 22], [11, 1]]))





















#Challenge for Cooper
# https://edabit.com/challenge/Xkc2iAjwCap2z9N5D























#Challenge for Krisjanis
# https://edabit.com/challenge/peezjw73G8BBGfHdW























