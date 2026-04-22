define m = Character("Mom")
define c = Character("Me")
define s = Character("Skeleton")

image handMain:
    "handMain.png"
    zoom .3

image handScared:
    "handScared.png"
    zoom .2

image skeleton:
    "skeleton.png"
    zoom.15

image Mom:
    "mom.png"
    zoom .3

image firstRoom:
    "firstRoom.png"
    zoom .5

image secondRoom:
    "secondRoom.png"

image thirdRoom:
    "thirdRoom.png"

image fourthRoom:
    "fourthRoom.png"

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


transform handFadeIn:
    alpha 0.0
    linear 0.5 alpha 1.0

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

screen clickableArea2():
    imagebutton:
        idle "clothesStill.png"
        hover "clothesHighlight.png"
        focus_mask True
        action Return("clothes")
    add "handMain.png" at handWobble, handFadeIn:
        xalign 0.9
        yalign 0.7
        zoom .3

screen clickableArea3():
    imagebutton:
        idle "skeletonStill.png"
        hover "skeletonHighlight.png"
        focus_mask True
        action Return("skeleton")

    

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

label clothesClick:
    scene black with fade
    play sound "audio/movingClothes.mp3"
    scene fourthRoom with fade
    show handScared at handWobble:
        xalign 1.0
        yalign 0.7
        alpha 0.0
        linear 0.5 alpha 1.0  
    return

label skeletonClick:
    scene black with fade
    c "blah"
    




# The game starts here.

label start:

    scene firstRoom with fade:
        xysize(1920,1080)
    
    c "I'll be sleeping soon"

    play sound "audio/knock.mp3"

    pause 1

    c "Come in"

    play sound "audio/door.mp3"

    show Mom at left with dissolve

    m "What do you wanna read this time?"

    c "Not this again."

    c "I'm 16 at this point I'm too old for bedtime stories."

    m "Oh, well since you're all grown-up, how about I tell you this horror story from when I was growing up."

    c "Fine, that at least sounds more interesting."

    play sound "audio/momScream.mp3"
    pause 1
    m "{b}THERE'S A SKELETON IN YOUR CLOSET!!{/b}"

    c "WOAH"

    m "..."

    c "That's hardly a story! Why would you scream like that!"

    m "Goodnight honey."

    hide Mom with dissolve

    play sound "audio/door.mp3"

    c "What the heck was that."

    c "Dammit now I don't think I can sleep, let me check the closet."

    menu:
        "Go to sleep":
            jump sleep

        "Check the closet":
            jump checking
    return


label sleep:
    scene black with fade
    "{b}Best ending.{/b}."
    return

label checking:
    scene black with fade
    play sound "audio/gettingup.mp3"
    play music "audio/backgroundmusic.mp3" fadein 5 fadeout 20 volume 0.03 loop
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

    call screen clickableArea2 
    $ choice = _return
    if choice == "clothes":
        call clothesClick
    play sound "audio/yell.mp3"
    c "Damn!!! Mom must've put this here." 
    c "But I don't know, it looks almost..."
    hide handScared with dissolve
    show handMain at handWobble:
        xalign 0.9
        yalign 0.7
        alpha 0.0
        linear 0.5 alpha 1.0 

    menu:
        "Touch it":
            jump touched
        "No way":
            jump noTouch
    
    label touched:
        call screen clickableArea3
        $ choice = _return
        if choice == "skeleton":
            call skeletonClick
        

    label noTouch:
        s "Where are you going..."
        s "You remember me...?"
        s "Or rather... Actually... Maybe not"
        s "I remember you..."
        s "Unfortunately I am inescapable..."
        c "..."
        c "WHAT THE HELL"
        c "WHAT IS THIS!?"
        c "I didn't do anything!"
        c "Leave me the hell alo-"
        scene black
        c "blah"

        
