define m = Character("Mom")
define c = Character("Me")

image handMain:
    "handMain.png"
    zoom .3

image firstRoom:
    "firstRoom.png"
    zoom .5

image Mom:
    "mom.png"
    zoom .3

image secondRoom:
    "secondRoom.png"

image thirdRoom:
    "thirdRoom.png"

image yodaHighlight:
    "yodaHighlight.png"
    xanchor 0.0
    yanchor 0.0

image yodaStill:
    "yodaStill.png"
    xanchor 0.0
    yanchor 0.0

image closetStill:
    "closetStill.png"
    xanchor 0.0
    yanchor 0.0

image closetHighlight:
    "closetHighlight.png"
    xanchor 0.0
    yanchor 0.0

transform handWobble:
    yoffset 0
    linear 1 yoffset -8
    linear 1 yoffset 8
    linear 1 yoffset -8
    linear 1 yoffset 8
    repeat

screen clickableArea():
    imagebutton:
        idle "yodaStill.png"
        hover "yodaHighlight.png"
        focus_mask True
        action Return("yoda")

    imagebutton:
        idle "closetStill.png"
        hover "closetHighlight.png"
        focus_mask True
        action Return("closet")

    imagebutton:
        idle "doorStill.png"
        hover "doorHighlight.png"
        focus_mask True
        action Return("door")

    imagebutton:
        idle "boneStill.png"
        hover "boneHighlight.png"
        focus_mask True
        action Return("bone")
    
    imagebutton:
        idle "dogStill.png"
        hover "dogHighlight.png"
        focus_mask True
        action Return("dog")

    

label closetClick:
    scene black with fade
    play sound "audio/twosteps.mp3"
    scene thirdRoom with fade
    show handMain at handWobble:
        xalign 0.9
        yalign 0.7
        alpha 0.0
        linear 0.5 alpha 1.0  
    return
    
    




# The game starts here.

label start:

    scene firstRoom with fade:
        xysize(1920,1080)
    
    c "I'll be sleeping soon"

    play sound "audio/knock.mp3"

    c "come in"

    show Mom at left with dissolve

    c "I'm 16 at this point I'm too old for bedtime stories."

    m "Since you're all grown-up, how about I tell you this horror story from when I was growing up."

    c "Fine, at least sounds more inter-"

    m "THERE'S A SKELETON IN YOUR CLOSET!!"

    c "..."

    m "..."

    c "That's hardly a story."

    m "Goodnight honey."

    hide Mom with dissolve

    c "What the heck was that."

    c "I can't sleep on that note. I think I should check."

    menu:
        "Go to sleep":
            jump sleep

        "Check the closet":
            jump checking
    return


label sleep:
    scene black with fade
    "{b}Game over{/b}."
    return

label checking:
    scene black with fade
    play sound "audio/gettingup.mp3"
    play music "audio/backgroundmusic.mp3" fadein 5 fadeout 5 volume 0.03 loop
    scene secondRoom with fade
    show handMain at handWobble:
        xalign 0.9
        yalign 0.7
        alpha 0.0
        linear 0.5 alpha 1.0  
    call screen clickableArea 
    $ choice = None

    while choice != "closet":

        call screen clickableArea
        $ choice = _return

        if choice == "yoda":
            play sound "audio/neutralGrunt.mp3" volume 0.5
            c "That's my lego yoda I built a while back."
        if choice == "door":
            play sound "audio/nogrunt.mp3" volume 0.1
            c "I'm either sleeping scared or double checking the closet."
        if choice == "bone":
            c "One of my dogs chew toys... where is he?"
        if choice == "dog":
            play sound "audio/neutralGrunt.mp3" volume 0.5
            c "There you are boy."
            play sound "audio/bark.mp3" volume 0.3
    if choice == "closet":
        call closetClick
    c "blah"
