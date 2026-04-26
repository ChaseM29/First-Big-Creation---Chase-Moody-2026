define m = Character("Mom")
define c = Character("Me")
define s = Character("Skeleton")
define h = Character("Him")

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
    zoom .27

image firstRoom:
    "firstRoom.png"
    zoom .5

image secondRoom:
    "secondRoom.png"

image thirdRoom:
    "thirdRoom.png"

image fourthRoom:
    "fourthRoom.png"

image fifthRoom:
    "fifthRoom.png"

image sixthRoom:
    "sixthRoom.png"

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

screen clickableArea4():
    imagebutton:
        idle "printerStill.png"
        hover "printerHighlight.png"
        focus_mask True
        action Return("printer")
    imagebutton:
        idle "deskStill.png"
        hover "deskHighlight.png"
        focus_mask True
        action Return("desk")
    imagebutton:
        idle "windowStill.png"
        hover "windowHighlight.png"
        focus_mask True
        action Return("window")


init python:
    def drag_placed(drags, drop):
        if not drop:
            return
        store.draggable = drags[0].drag_name
        store.droppable = drop.drag_name
        return True

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
    jump officeStart

label deskClick:
    scene black with fade
    scene sixthRoom with fade
    jump search

label ringClick:
        jump continue



define longFade = Fade(0.5, 0.0, 6)

screen dragArea: 
    imagebutton:
        xpos 150 ypos 300
        idle Transform("ringStill.png", zoom=.1)
        hover Transform("ringHighlight.png", zoom=.1)
        focus_mask True
        action Return("ring")
    draggroup:
        drag:
            droppable False
            dragged drag_placed
            xpos 100 ypos 100
            drag_offscreen(50, -50, 50, -400)
            add "test.png" zoom .3
        drag:
            droppable False
            dragged drag_placed
            xpos 1000 ypos 1
            drag_offscreen(50, -50, 0, -450)
            add "paperC.png" zoom .3
        drag:
            droppable False
            dragged drag_placed
            xpos 500 ypos 100
            drag_offscreen(50, -50, 50, -440)
            add "notebook.png" zoom .3
        drag:
            droppable False
            dragged drag_placed
            xpos 500 ypos 100
            drag_offscreen(50, -50, 50, -440)
            add "backpack.png" zoom .6


        


    




# The game starts here.

label start:

    scene firstRoom with fade:
        xysize(1920,1080)
    
    play music "audio/crickets.mp3" volume 0.01 fadein 2

    c "I'll be sleeping soon"

    play sound "audio/knock.mp3"

    pause 1

    c "Come in."

    play sound "audio/door.mp3"

    show Mom at left with dissolve


    m "What do you wanna read this time?"

    c "Not this again mom. I'm 16 at this point I'm too old for bedtime stories."

    m "Oh, well since you're all grown-up, how about I tell you this horror story from when I was growing up."

    c "Hmmm."
    c "Go on."

    play sound "audio/momScream.mp3" volume 0.2
    pause 1.2
    m "{b}THERE'S A SKELETON IN YOUR CLOSET!{/b}"

    c "{b}WOAH!{\b}"

    m "..."

    c "That- That's not even a story. Why would you scream like that?"

    m "Goodnight honey."

    hide Mom with dissolve

    play sound "audio/door.mp3"

    c "What in the world was that dude."

    c "I don't think I can sleep now. Maybe I should check the closet."

    menu:
        "Go to sleep":
            jump sleep

        "Check the closet":
            jump checking
    return


label sleep:
    c "Whatever."
    #add yawn
    scene black with fade
    play music "audio/lowWarble.mp3" fadein 5
    show skeleton with longFade
    s "WAKE UP" with None
    stop music fadeout 0.5
    scene firstRoom:
        xysize(1920, 1080)
    c "What the HELL!"
    play sound "audio/ugh.mp3"
    c "Now I've {i}gotta{\i} check."
    jump checking

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
            play sound "audio/nogrunt.mp3" volume 0.3
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
    c "But, should I...?"
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
            jump officeStart
        

    label noTouch:
        stop music fadeout 7
        s "Where are you going?"
        s "You remember me?"
        s "Or rather... Actually... Maybe not. But {b}probably{\b}!"
        s "I remember {b}you{\b}."
        s "I am inescapable."
        c "NO!"
        c "WHAT THE HELL!?"
        c "WHAT IS THIS!?"
        c "I didn't do anything!"
        c "Leave me the hell alo-"
        scene black
        jump officeStart
    
    label officeStart:
        play music "audio/lowWarble.mp3" volume 1 fadein 10
        scene fifthRoom with longFade
        c "Where..."
        c "I feel weak."
        c "Oh no..."
        c "Not here."
        c "I'm sorry."
        
        s "You seemed so forgetful {b}EARLIER{\b}."

        c "please..."

        #Make hand less confident

        show handMain at handWobble:
            xalign 0.9
            yalign 0.7
            alpha 0.0
            linear 0.5 alpha 1.0  
        
        h "Find it."

        #After click to go to desk

        c "please no..."

        play sound "audio/growl.mp3"
        h "{b}FIND IT{\b}."

        call screen clickableArea4
        while choice != "desk":
            call screen clickableArea4
            $ choice = _return

            if choice == "window":
                s "It was a sunny day. Broad daylight didn't scare you."
            if choice == "printer":
                s "I loved that printer."
        if choice == "desk":
            jump deskClick

        label search:
            call screen dragArea
            $ choice = _return
            if choice == "ring":
                jump ringClick

        label continue:
            menu:
                "Take it.":
                    jump taken
                "Dont take it.":
                    jump notTaken
        
        label taken:
            c "I needed it."
            s "Did you need what comes next?"
        label notTaken:
            s "You serve only to anger me with lying."
            s "That is not how it went."
            jump continue



        



        
