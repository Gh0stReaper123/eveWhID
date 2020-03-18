import guizero
import ctypes

wormholeEyeLocations = {
    1:"C1 wormhole space",
    2:"C2 wormhole space",
    3:"C3 wormhole space",
    4:"C4 wormhole space",
    5:"C5 wormhole space",
    6:"C6 wormhole space",
}

wormholeAuroraMeanings = {
    1:"Only frigate sized ships",
    2:"Medium sized ships including: cruisers, battlecruisers and industrial ships",
    3:"Every ship but not capital class ships",
    4:"Every ship including capital class ships"
}



user32 = ctypes.windll.user32
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

MAIN_APP_TITLE = "Wormhole Identifier"
MAIN_APP_LAYOUT = "grid"

mainApp = guizero.App(
    MAIN_APP_TITLE,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    MAIN_APP_LAYOUT)

mainApp.tk.wm_iconbitmap('images/space.ico')

titleText = guizero.Text(
    mainApp,
    "Adjust the sliders to match the wormhole you're looking at:",
    size=20,
    grid=[0,0]
)

wormholeEyeImage = guizero.Picture(
    mainApp,
    "images/c1.bmp",
    grid=[0,1],
    width=250,
    height=250)

def switchWormholeEye():
    wormholeEyeImage.image = "images/c{}.bmp".format(wormholeEyeSlider.value)
wormholeEyeSlider = guizero.Slider(
    mainApp,
    start = 1,
    end = 6,
    horizontal = True,
    command=switchWormholeEye,
    grid=[0,2]
)

wormholeAuroraImage =  guizero.Picture(
    mainApp,
    "images/a1.bmp",
    grid=[0,3],
    width=698,
    height=291)

def switchWormholeAurora():
    wormholeAuroraImage.image = "images/a{}.bmp".format(wormholeAuroraSlider.value)
wormholeAuroraSlider = guizero.Slider(
    mainApp,
    start = 1,
    end = 4,
    horizontal = True,
    command=switchWormholeAurora,
    grid=[0,4]
)

def results():

    whDestination = wormholeEyeLocations[wormholeEyeSlider.value]
    whMassLimit = wormholeAuroraMeanings[wormholeAuroraSlider.value]

    guizero.info(
        "Type of wormhole: ",
        f"This wormhole leads to:\n{whDestination}\n\nThis wormhole can transport:\n{whMassLimit}",
        master=mainApp
    )

submitButton = guizero.PushButton(
    mainApp,
    command=results,
    text="Submit",
    grid=[0,5])

mainApp.display()
