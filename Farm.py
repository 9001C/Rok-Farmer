import pyautogui
import time
import keyboard
import mouse 
import cv2
import argparse
import random


#argparse arguments for type
parser = argparse.ArgumentParser()
parser.add_argument('-t','--resourcetype', type=int)
args = parser.parse_args()

#DON'T RUN 24/7
BasePath = r"C:\Users\J\Documents\Python" # file path to the image folder

RandomClickRange = 10 # amount of variance allowed in each click to avoid bot detection  
RandomTimeRange = 2 #Time variance to avoid bot detection 



def clearscreen():
  
  #search for x
    try:
        x = pyautogui.locateCenterOnScreen(BasePath+r"\Rok images\farm\x.png", confidence=.8)
        time.sleep(1+(random.randrange(0,RandomTimeRange)))(x[0]+random.randrange(0,RandomClickRange)),(x[1]+random.randrange(0,RandomClickRange))
    except:
        pass
    time.sleep(1+(random.randrange(0,RandomTimeRange)))
  #check if in city


def farm():
    type = args.resourcetype
    #check if in or out of city then push city button
    #click search button
    try:
        search = pyautogui.locateCenterOnScreen(BasePath+r"\Rok images\farm\search.png", confidence=.8)
        pyautogui.leftClick((search[0]+random.randrange(0,RandomClickRange)),(search[1]+random.randrange(0,RandomClickRange)))
    except:
        pass
    time.sleep(1+(random.randrange(0,RandomTimeRange)))
    if(type == 1):
    #search for food
        try:
            cropsearch = pyautogui.locateCenterOnScreen(BasePath+r"\Rok images\farm\cropland.png", confidence=.8)
            pyautogui.leftClick((cropsearch[0]+random.randrange(0,RandomClickRange)),(cropsearch[1]+random.randrange(0,RandomClickRange)))
            time.sleep(1+(random.randrange(0,RandomTimeRange)))
            try:
                searchnode = pyautogui.locateCenterOnScreen(BasePath+r"\Rok images\farm\searchnode.png", confidence=.8)
                pyautogui.leftClick((searchnode[0]+random.randrange(0,RandomClickRange)),(searchnode[1]+random.randrange(0,RandomClickRange)))
                time.sleep(3+(random.randrange(0,RandomTimeRange)))
                screen_width, screen_height = pyautogui.size()
                center_x = screen_width / 2
                center_y = screen_height / 2
                pyautogui.leftClick((center_x+random.randrange(0,RandomClickRange)), (center_y+random.randrange(0,RandomClickRange)))
                time.sleep(1+(random.randrange(0,RandomTimeRange)))
                try:
                    gather = pyautogui.locateCenterOnScreen(BasePath+r"\Rok images\farm\gather.png", confidence=.8)
                    pyautogui.leftClick((gather[0]+random.randrange(0,RandomClickRange)),(gather[1]+random.randrange(0,RandomClickRange)))
                    time.sleep(1+(random.randrange(0,RandomTimeRange)))
                    try:
                        newtroop = pyautogui.locateCenterOnScreen(BasePath+r"\Rok images\farm\newtroop.png", confidence=.8)
                        pyautogui.leftClick((newtroop[0]+random.randrange(0,RandomClickRange)),(newtroop[1]+random.randrange(0,RandomClickRange)))
                        time.sleep(1+(random.randrange(0,RandomTimeRange)))
                        try:
                            march = pyautogui.locateCenterOnScreen(BasePath+r"\Rok images\farm\march.png", confidence=.8)
                            pyautogui.leftClick((march[0]+random.randrange(0,RandomClickRange)),(march[1]+random.randrange(0,RandomClickRange)))
                        except:
                            pass
                    except:
                        screen_width, screen_height = pyautogui.size()
                        center_x = screen_width / 2
                        center_y = screen_height / 2
                        pyautogui.leftClick((center_x+random.randrange(0,RandomClickRange)), (center_y+random.randrange(0,RandomClickRange)))
                        time.sleep(1+(random.randrange(0,RandomTimeRange)))
                        pass
                except:
                    pass
            except:
                pass
        except:
            pass
    elif(type == 2):
        try:
            woodsearch = pyautogui.locateCenterOnScreen(BasePath+r"\Rok images\farm\logging.png", confidence=.8)
            pyautogui.leftClick((woodsearch[0]+random.randrange(0,RandomClickRange)),(woodsearch[1]+random.randrange(0,RandomClickRange)))
            time.sleep(1+(random.randrange(0,RandomTimeRange)))
            try:
                searchnode = pyautogui.locateCenterOnScreen(BasePath+r"\Rok images\farm\searchnode.png", confidence=.8)
                pyautogui.leftClick((searchnode[0]+random.randrange(0,RandomClickRange)),(searchnode[1]+random.randrange(0,RandomClickRange)))
                time.sleep(3+(random.randrange(0,RandomTimeRange)))
                screen_width, screen_height = pyautogui.size()
                center_x = screen_width / 2
                center_y = screen_height / 2
                pyautogui.leftClick((center_x+random.randrange(0,RandomClickRange)), (center_y+random.randrange(0,RandomClickRange)))
                time.sleep(1+(random.randrange(0,RandomTimeRange)))
                try:
                    gather = pyautogui.locateCenterOnScreen(BasePath+r"\Rok images\farm\gather.png", confidence=.8)
                    pyautogui.leftClick((gather[0]+random.randrange(0,RandomClickRange)),(gather[1]+random.randrange(0,RandomClickRange)))
                    time.sleep(1+(random.randrange(0,RandomTimeRange)))
                    try:
                        newtroop = pyautogui.locateCenterOnScreen(BasePath+r"\Rok images\farm\newtroop.png", confidence=.8)
                        pyautogui.leftClick((newtroop[0]+random.randrange(0,RandomClickRange)),(newtroop[1]+random.randrange(0,RandomClickRange)))
                        time.sleep(1+(random.randrange(0,RandomTimeRange)))
                        try:
                            march = pyautogui.locateCenterOnScreen(BasePath+r"\Rok images\farm\march.png", confidence=.8)
                            pyautogui.leftClick((march[0]+random.randrange(0,RandomClickRange)),(march[1]+random.randrange(0,RandomClickRange)))
                        except:
                            pass
                    except:
                        screen_width, screen_height = pyautogui.size()
                        center_x = screen_width / 2
                        center_y = screen_height / 2
                        pyautogui.leftClick((center_x+random.randrange(0,RandomClickRange)), (center_y+random.randrange(0,RandomClickRange)))
                        time.sleep(1+(random.randrange(0,RandomTimeRange)))
                        pass
                except:
                    pass
            except:
                pass
        except:
            pass
    #search for wood
    elif(type == 3):
        try:
            stonesearch = pyautogui.locateCenterOnScreen(BasePath+r"\Rok images\farm\stone.png", confidence=.8)
            pyautogui.leftClick((stonesearch[0]+random.randrange(0,RandomClickRange)),(stonesearch[1]+random.randrange(0,RandomClickRange)))
            time.sleep(1+(random.randrange(0,RandomTimeRange)))
            try:
                searchnode = pyautogui.locateCenterOnScreen(BasePath+r"\Rok images\farm\searchnode.png", confidence=.8)
                pyautogui.leftClick((searchnode[0]+random.randrange(0,RandomClickRange)),(searchnode[1]+random.randrange(0,RandomClickRange)))
                time.sleep(3+(random.randrange(0,RandomTimeRange)))
                screen_width, screen_height = pyautogui.size()
                center_x = screen_width / 2
                center_y = screen_height / 2
                pyautogui.leftClick((center_x+random.randrange(0,RandomClickRange)), (center_y+random.randrange(0,RandomClickRange)))
                time.sleep(1+(random.randrange(0,RandomTimeRange)))
                try:
                    gather = pyautogui.locateCenterOnScreen(BasePath+r"\Rok images\farm\gather.png", confidence=.8)
                    pyautogui.leftClick((gather[0]+random.randrange(0,RandomClickRange)),(gather[1]+random.randrange(0,RandomClickRange)))
                    time.sleep(1+(random.randrange(0,RandomTimeRange)))
                    try:
                        newtroop = pyautogui.locateCenterOnScreen(BasePath+r"\Rok images\farm\newtroop.png", confidence=.8)
                        pyautogui.leftClick((newtroop[0]+random.randrange(0,RandomClickRange)),(newtroop[1]+random.randrange(0,RandomClickRange)))
                        time.sleep(1+(random.randrange(0,RandomTimeRange)))
                        try:
                            march = pyautogui.locateCenterOnScreen(BasePath+r"\Rok images\farm\march.png", confidence=.8)
                            pyautogui.leftClick((march[0]+random.randrange(0,RandomClickRange)),(march[1]+random.randrange(0,RandomClickRange)))
                        except:
                            pass
                    except:
                        screen_width, screen_height = pyautogui.size()
                        center_x = screen_width / 2
                        center_y = screen_height / 2
                        pyautogui.leftClick((center_x+random.randrange(0,RandomClickRange)), (center_y+random.randrange(0,RandomClickRange)))
                        time.sleep(1+(random.randrange(0,RandomTimeRange)))
                        pass
                except:
                    pass
            except:
                pass
        except:
            pass
    #search for stone 
    elif(type == 4):
        print("4")
    #search for gold
    else:
      print("1:food | 2:wood | 3:stone |4:gold(not yet added)")
      quit()

while True:
    time.sleep(5+random.randrange(0,10))
    clearscreen()
    farm()
