# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Mom")
define c = Character("Me")

image Mom:
    "mom.svg"
    zoom 2

image Money:
    "money.png"
    zoom .3




# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene Money

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Mom

    # These display lines of dialogue.

    c "I'm 16 at this point I'm too old for bedtime stories."

    m "Since you're all grown-up, how about I tell you this horror story from when I was growing up."

    c "Fine, at least sounds more inter-"

    m "THERE'S A SKELETON IN YOUR CLOSET!!"

    c "..."

    m "..."

    c "C'mon mom that's hardly a story."

    m "Goodnight honey."

    hide Mom

    c "What the heck was that."

    c "I can't sleep on that note. I think I should check."

    menu:
        "Go to sleep":
            jump choice_1

        "Check the closet":
            jump choice_2
    return


label choice_1:
    scene black with fade
    "{b}Game over{/b}."
    return

label choice_2:
    play sound "audio/gettingup.mp3"
    c "blah"
    return
