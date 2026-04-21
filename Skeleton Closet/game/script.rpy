define m = Character("Mom")
define c = Character("Me")

image handMain:
    "handMain.png"
    zoom .3

image firstRoom:
    "test.png"
    zoom .5

image Mom:
    "mom.png"
    zoom .3






# The game starts here.

label start:


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
    scene test with fade:
        xysize(1920, 1080)
    show handMain:
        xalign 0.9
        yalign 0.8
        alpha 0.0
        linear 1.0 alpha 1.0
    c "blah"
