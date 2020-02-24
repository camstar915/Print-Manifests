from PIL import Image
import pytesseract
import pyautogui

# pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

gui = pyautogui

manifestSet = set()

def click(thing):
    region = None
    if thing == 'printButton':
        region = [1408, 235, 100, 50]
    if thing == 'printButton2':
        region = [7, 45, 60, 40]
    if thing == 'printButton3' or thing == 'cancelButton':
        region = [613, 573, 170, 50]
    if thing == 'closeWindow':
        region = [46, 60, 100, 30]
    if region == None:
        while not gui.locateOnScreen('resources/' + thing + '.png', grayscale=True):
            continue
        gui.moveTo(gui.locateCenterOnScreen('resources/' + thing + '.png', grayscale=True))
        gui.click()
    if region:
        while not gui.locateOnScreen('resources/' + thing + '.png', region=(region[0], region[1], region[2], region[3]), grayscale=True):
            continue
        gui.moveTo(gui.locateCenterOnScreen('resources/' + thing + '.png', grayscale=True))
        gui.click()

while gui.locateOnScreen('resources/previousButton.png', grayscale=True):

    img = gui.screenshot(region=(240, 930, 260, 50))
    resultString = pytesseract.image_to_string(img)
    length = len(resultString)
    manifest = resultString[length-4:length]

    while length == 0:
        img = gui.screenshot(region=(230, 910, 280, 100))
        resultString = pytesseract.image_to_string(img)
        length = len(resultString)
        manifest = resultString[length-4:length]


    if not manifest in manifestSet:
        manifestSet.add(manifest)
        print(manifest)
        click('printButton')
        click('printButton2')
        # comment out "click('printButton3') and enable click('cancelButton') to test changes"
        click('printButton3')
        # click('cancelButton')
        click('closeWindow')
        click('previousButton')
        gui.moveRel(0, 30)
        resultString = None
        img = None
        length = None

    elif manifest in manifestSet:
        click('previousButton')
        gui.moveRel(0, 30)
        resultString = None
        img = None
        length = None