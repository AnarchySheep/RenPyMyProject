image bg peachbackground = "peachbackground.jpg"

label peach:
    show bg peachbackground
    show peach
    peach "Oh hi there!"
    $ peachVisited += 1

    $ fill = "STILL" if peachVisited > 1 else ""



    "You blush because you [fill] have never seen a girl this pretty, besides Joyce"
    $ motivation += 10
    "Motivation +10"
    python:
        if motivation <= 30:
            renpy.say( "", "She's [fill] extremely pretty and you [fill] get scared")
            renpy.say( me, "This is too much....")
            renpy.say( "", "You run away like a little baby")

        else:
            renpy.say("" , "I finally have the courage to talk to her")
            renpy.say(me, "What up Peach")
    hide bg peachbackground
    hide peach
    jump map
