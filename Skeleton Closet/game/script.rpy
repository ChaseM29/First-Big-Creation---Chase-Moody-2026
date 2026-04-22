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

image yodaHighlight:
    "yodaHighlight.png"
    xpos 466
    ypos 297
    
transform handWobble:
    yoffset 0
    linear 1 yoffset -8
    linear 1 yoffset 8
    linear 1 yoffset -8
    linear 1 yoffset 8
    repeat

screen yodaSelect():
    imagebutton:
        xpos 466
        ypos 297
        xsize 200
        ysize 200 
        idle Solid("#00000000")
        hover "yodaHighlight.png"
        action Jump("yodaClick")

label yodaClick:
    c "That's my lego yoda I built a while back."
    c "Better check out that closet."



# The game starts here.

label start:

    scene firstRoom with fade:
        xysize(1920,1080)
    show Mom at left

    c "I'm 16 at this point I'm too old for bedtime stories."

    m "Since you're all grown-up, how about I tell you this horror story from when I was growing up."

    c "Fine, at least sounds more inter-"

    m "THERE'S A SKELETON IN YOUR CLOSET!!"

    c "..."

    m "..."

    c "That's hardly a story."

    m "Goodnight honey."

    hide Mom

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
    scene secondRoom with fade
    show handMain at handWobble:
        xalign 0.9
        yalign 0.7
        alpha 0.0
        linear 0.5 alpha 1.0  
    call screen yodaSelect       
    c "blah"
