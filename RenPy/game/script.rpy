default pick_mistake = False
default pick_mistake_2 = False

label start:
    show screen display_stats

    #jump map

    scene black
    with dissolve

    "Hey, before we get started with the game, I need to ask you a few questions."

    "Nothing too scary, mind you. But it will help with making this game as fun for you as possible!"

    "First of all, can I get your first name?"

    "If you would prefer not to give out your name, you can just leave it blank and I can just give you the default."

label nameselect:

    python:
        fn = renpy.input("Enter Name.").strip()

        if not fn:
            fn = "Rien"

    "And what is your last name?"

    python:
        ln = renpy.input ("Enter surname.").strip()

        if not ln:
            ln = "Williams"

    "Your name is [fn] [ln], is that correct?"

    menu:
        "Yes":
            jump confirmname

        "No, let me change it.":
            jump nameselect


label confirmname:

    "Pleased to meet you, [fn]!"

    jump pronouns

label pronouns:

    "Are you a guy, gal, or a non-binary pal?"

    menu:

        "Guy":
            $ gender = "male"
            $ they = "he"
            $ them = "him"
            $ their = "his"
            $ theirs = "his"
            $ themself = "himself"
            $ they_cap = "He"
            $ them_cap = "Him"
            $ their_cap = "His"
            $ theirs_cap = "His"
            $ themself_cap = "Himself"
            $ mx = "Mr."

        "Gal":
            $ gender = "female"
            $ they = "she"
            $ them = "her"
            $ their = "her"
            $ theirs = "hers"
            $ themself = "herself"
            $ they_cap = "She"
            $ them_cap = "Her"
            $ their_cap = "Her"
            $ theirs_cap = "Hers"
            $ themself_cap = "Herself"
            $ mx = "Ms."

        "Non-Binary Pal":
            $ gender = "non-binary"
            $ they = "they"
            $ them = "them"
            $ their = "their"
            $ theirs = "theirs"
            $ themself = "themself"
            $ they_cap = "They"
            $ them_cap = "Them"
            $ their_cap = "Their"
            $ theirs_cap = "Theirs"
            $ themself_cap = "Themself"
            $ mx = "Mx."

    "Okay, so you are [gender] and you use [they]/[them] pronouns. Is that correct?"

    menu:

        "Yes, take me to the game.":

            jump disclaimer

        "No, let me change my name.":

            jump nameselect

        "No, let me change my pronouns.":

            jump pronouns

label disclaimer:

    "Terrific!"

    "Let me remind you that I am not affiliated with the real Thomas Sanders and this dating sim is supposed to be for funsies."

    "That being said, none of the events that occur accurately portray him and should not be taken too seriously."

    "That's all from me, so enjoy the game!"

label gamestart:

    scene player room morning
    with blinds

    "The sun filters thourgh the blinds, shining directly into my eyes as if to spite me personally."

    "It's really comfortable, swaddled in my nest of blankets like a burrito but made of down and fabric."

    "..."

    "All of this talk about burritos made me hungry. Which reminds me, it's time to get up and get breakfast."

    yn "Urgh..."

    "With a majority of my face currently smooshed on you pillow, I can't really see my clock."

    "But the sun doesn't seem too high up and it's just too comfy..."

    "Surely a few extra minutes of sleep would be fine."

    menu:

        "Sleep a little bit more.":
            $ motivation -=1
            $ strength +=1
            jump late

        "Get up already, you lazy butt.":
            $ motivation +=1
            $ charisma +=1
            jump ready

label ready:

    scene player room morning
    with vpunch

    yn "Ow."

    "It's a little awkward trying to detangle myself from the sheets, but I manage to free myself and head for the kitchen."

    "The house is quiet, since my parents always leave for work early. Most of the time, I get the house to myself."

    menu:

        "Which is fine. I can take care of myself.":
            $ strength +=2
            $ motivation +=1
            $ charisma +=1

        "It's a little hard, but I'm really good at making do by myself.":

            $ strength +=1
            $ intel +=1
            $ creativity +=1

        "I can barely take care of myself without them.":

            $ strength -=1
            $ motivation +=1
            $ intel -=1

    "In any case, I finished eating breakfast pretty quickly. Maybe I'll try to put effort into my appearance today."

    "Hm.."

    "What mood am I going for today?"

    menu:

        "What mood am I going for today?"

        "Proper and smart":

            "First impressions are pretty important. I need to show that I mean business."

            "Button-up shirt, clean pants, polished shoes..."

            "Maybe the bowtie is a little excessive."

            "But hey, I look smart as hell."

            yn "Time to go."

            $ lorom +=1
            $ intel +=1
            $ outfit = "smart"

            jump firstbusearly

        "Flashy and trendy":

            "I bought some brand clothing during the summer when I moved in."

            "They were a little expensive, but I look amazing in it."

            "It's a little flashy, but hey. I've got goods to show."

            yn "Ready to go!"

            $ rorom +=1
            $ anxrom -=1
            $ charisma +=1
            $ outfit = "trendy"

            jump firstbusearly

        "Ready for death":

            "It's important to be true to yourself. {w}So, I throw on the darkest pieces of clothing in my closet."

            "It kind of looks like I just came straight out of a funeral in Hot Topic, but that's the kind of look I'm going for."

            yn "Time to go."

            $ anxrom +=1
            $ motivation -=1
            $ strength +=1
            $ outfit = "emo"

            jump firstbusearly

        "Just whatever's comfortable and clean.":

            "I'm not trying to impress anyone."

            "It's still kind of warm out, so I'll just put on a shirt and some shorts."

            "Comfy."

            yn "Time to go!"

            $ morom +=1
            $ motivation +=1
            $ outfit = "comfy"

            jump firstbusearly

label late:

    "Yeah, I can probably get away with a couple more hours."

    "I'll just close my eyes for a bit and...{w}just..."

    scene black
    with fade

    "..."

    scene player room midday
    with dissolve

    "Crap."

    "Somehow, I knew this would happen."

    "But I did it anyways."

    "What is {i}wrong{/i} with me?!"

    "Whatever. The past is the past."

    "Just put on whatever and go. {w}Hopefully, I didn't miss the bus."

    jump firstbuslate

label firstbusearly:

    scene bus morning
    with dissolve

    "Honestly, I'm a little nervous."

    "I haven't been a new student in forever and from previous experience, most of the other students probably already conglomerated into their own cliques."

    "I hope that I'll at least make one new friend or something."

    "It'll suck having to go though the school year without anyone to talk to."

    "..."

    "Oh!"

    "They said that I would have a guide to show me around school."

    "I'm not exactly sure what they look like."

    "They only gave me a name and a pretty sparse description."

    "'Thomas Sanders.'"

    "Apparently, I just have to look for a guy with brown hair near the entrance.{p}As if there aren't a million of those in the world."

    "I guess I'll find out when I get there??"

    jump dayone

label firstbuslate:

    scene bus morning
    with dissolve

    $ strength +=1

    yn "Huff...ugh..."

    "That's the last time I'm sleeping in. I can't feel my legs."

    "Gross, now I'm all sweaty."

    "This'll be a great first impression. Nice job, [fn]."

    "They said that I would have a guide to show me around school."

    "I'm not exactly sure what they look like."

    "They only gave me a name and a pretty sparse description."

    "'Thomas.'"

    "Apparently, I just have to look for a guy with brown hair near the entrance.{p}As if there aren't a million of those in the world."

    "I guess I'll find out when I get there??"

    "I hope he's still there. I'm pretty late."

    jump dayonelate

label dayone:

    "Thankfully, there aren't a lot of students out and about. I {i}am{/i} pretty early."

    "Even so, the crappy description they gave me doesn't help at all..."

    show thomas distant at right
    show logic distant at left
    with dissolve

    "There are two guys that fit that description that I can see right away."

    "But one of them looks like a teacher. Do they assign teachers to show students around?"

    "This school is weird."

    "I guess I'll go approach..."

label earlychoice:
    python:
        if pick_mistake:
            renpy.say(yn, "Let me pick the right person this time")


    "I guess I'll go approach..."
    $option1 = "Go back to the glasses guy." if pick_mistake else "The one with the glasses and tie."


    menu:
        "[option1]" :
            jump logicguide

        "The one with the bomber jacket.":
            jump thomasguide

label dayonelate:

    $ late = True

    "I guess I'm later than I thought. There aren't a lot of students left in front of the school."

    "Well, at least this makes it easier to find the guy I`m looking for."

    "That is, if he's still here. {w}I'm so late."

    "..."

    show anx distant on right
    show thomas distant on left
    with dissolve

    "Oh!"

    "...I see two guys fitting the description they gave me."

    "I wonder which one's my guide?"

label latechoice:
    $option1 = "I guess I'll go pick again?" if pick_mistake else "I wonder which one's my guide?"

    menu:
        "The guy in the hoodie.":
            jump anxguide

        "The one in the bomber jacket.":
            jump thomasguide

label logicguide:

    show logic distant
    with dissolve

    yn "Hi, excuse me?"

    show logic neutral

    u "Hm?"

    if pick_mistake:

        u "Oh, it's you again."

        yn "Yeah, um..."

    menu:

        "I'm [fn]. Are you Thomas?":
            $ motivation +=1

            show logan confused
            u "..."

            "...?"

            show logic neutral talk

            u "Ah, you must be new. {w}I suppose that explains the mix-up."

            show logic neutral

            u "No, I am not Thomas."

            yn "Oh, sorry! I'm just going to go, then."

            "So much for first impressions. But could it have hurt them to give me a better description?"

            u "Wait."

            yn "Huh?"

            u "If you want, I may still serve as a guide for you."

            yn "Oh, I don't want to impose. Don't you have a class for first period?"

            lo "No worries. I have that period free."

            yn "Oh. Well in that case, sure. Thanks."

            show logic neutral talk

            lo "It's no trouble."

            show logic neutral

            lo "My name is Logan Sanders. What's yours?"

            "He's pretty friendly for a teacher. Usually they just tell me their last name."

            yn "My name's [fn]. Nice to meet you, Mr. Sanders."

            show logic shocked blush

            lo "...!"

            show logic blush

            lo "Just 'Logan' is fine, [fn]."

            yn "Oh. Sorry, Logan."

            "That was a weird reaction..."

            show logic neutral

            lo "It's alright. Follow me."

            hide logic neutral
            with fade

            $ sir_kink = True

            jump logictour

        "I'm a new student here. Do you mind showing me around?":
            $ charisma +=1

            show logic shocked

            "filler text"

            return

            if pick_mistake:
                show logic confused

                u "Um...alright?"

                u "Are you sure you don't need anything?"

                yn "Yes!!! I'm sure!!"

                hide logic confused
                with fade

                "What the heck was I thinking???"

                "There's no way I'm going back to that guy."

                $ pick_mistake_2 = True

                jump earlychoice

            else:

                "Sorry, I thought you were someone else."

                u "I see. That's quite alright."

                yn "Yeah, I'll just...go."

                hide logic neutral
                with fade

                "Well, that was embarrassing."

                $ charisma -=1
                $ pick_mistake = True

                jump earlychoice

label thomasguide:

    show thomas surprised
    with dissolve

    yn "Thomas Sanders?"

    u "Huh?"

    show thomas happy

    ts "Oh, you must be [fn]! Glad to finally meet you."

    "He's holding his hand out for a handshake."

    "Ah, looks like I chose the right guy after all."

    menu:

        "Shake his hand.":
            $ thomasfriend +=1

            "He's really friendly."

        "Do nothing.":

            "He kind of stands there awkwardly for a bit."

            ts "Oh! Sorry, are you uncomfortable with physical contact?"

            menu:

                "Yeah, sorry.":

                    ts "No, it's okay. I understand."

                "No.":
                    $ thomasfriend -=1

                    ts "..."

                    ts "Th-That's fine."

    if late == True:

        yn "Sorry I'm late, by the way. I kind of slept in."

        ts "Don't worry about it. I got the first two periods off so I can show you around."

        yn "Oh. Well in that case, I take it back. That extra hour felt amazing."

        "Thomas laughs. It sounds like what sunshine would sound like if it could laugh."

        ts "Goodness, I know what that's like. Come on, I'll show you around."

    else:

        ts "Anyways, let me show you around!"

        jump thomastour

return

label anxguide:

    yn "Um..."

    show anx glare

    yn "...!"

    "Goodness, he's really terrifying."

    u "What do you want?"

    yn "Oh, um..."

    menu:

        "Are you Thomas?":

            u "No."

            yn "Oh, sorry."

            yn "I'll just go, then."

            u "Whatever."

            hide anx glare
            with fade

            "Geez, what's his problem?"

            $ pick_mistake = True

            jump latechoice

        "I'm new here. Do you mind showing me around?":
            $ motivation +=1
            $ anxrom = +1

            u "..."

            "He looks really uncomfortable. Maybe I should just--"

            u "Um, yeah. I guess."

            "!!"

            "Wow. Not gonna lie, I didn't expect that at all."

            yn "Thanks."

            u "Yeah, whatever."

            u "I was a new kid once too, y'know."

            yn "I know how much it can suck."

            u "Follow me."

            jump anxtour

        "Nevermind. I thought you were someone else.":

            u "..."

            yn "I'm just...gonna go."

            hide anx glare
            with fade

            "How scary..."

            jump latechoice

label logictour:

    show hallway morning
    with fade

    "Logan spends the next period showing me around The School. Class is still going on, so he just points to them and tells them what they are for."

    lo "The School is not overly large. I trust that you won't have too much trouble navigating it."

    lo "But if you do end up getting lost, feel free to contact me on my cellphone."

    yn "Oh, thanks."

    yn "Are you sure you're supposed to be giving out your number to random students, though?"

    lo "...?"

    lo "Well, friends give each other their phone numbers, no?"

    menu:

        "We aren't friends.":
            $ lorom -=1

            lo "Oh, I apologize. I just thought..."

            lo "..."

            lo "It's almost lunchtime. Let me show you some of the clubs we have here."

            jump meetmorality

        "I guess so.":

            lo "Excellent. Can you show me your phone for a second?"

            "I hand him my phone and he puts in his number."

        "Can teachers and students be friends?":
            $ lorom +=1

            lo "What do you..."

            "He trails off for a moment."

            lo "Do you...think I am a teacher?"

            yn "?????"

            yn "Wait."

            if sirkink == True:

                lo "Well, that would explain why you referred to me as Mr. Sanders earlier."

            else:

                lo "It seems that there was a bit of a misunderstanding."


label map:
    hide screen display_stats
    call screen example_imagemap
    $ result = _return
    show screen display_stats

    if result == "bowserjr":
        jump bowserjr
    elif result == "peach":
        jump peach
    elif result == "center":
        jump start

label mario:
    show bg marioland
    $ mario_rel = 0

    show mario happy
    # These display lines of dialogue.
    e "James senpai ur so kewl! [stats]"
    jump map

    show mario dab
    e "I wish I was as cool as you!"
    show mario punch
    "Bam!!" with vpunch
    show mario

    me "I'm gonna get you back for that"
    menu:
        "Beat him":
            show mario hurt
            e "Ouch Senpai that hurt"
            $ mario_rel -= 1
            hide bg mario
            jump neutralend
        "Pat him":
            e "Thanks Senpai"
            python:
                mario_rel += 1
            hide bg mario
            jump goodend

        "Kill him":
            show mario hurt
            e "Nani!"
            python:
                mario_rel -= 2

            hide bg mario
            jump badend




label finalend:
    me "End of story. Mario relationship  [mario_rel]"
    return


label badend:
    e "OH nos"
    jump finalend
label neutralend:
    e "How could you senpai"
    jump finalend
label goodend:
    e "You're the best senpai"
    jump finalend




    # This ends the game.

    return
