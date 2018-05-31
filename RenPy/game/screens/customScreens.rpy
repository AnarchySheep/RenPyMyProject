init python:
    def hideAll():
        renpy.hide_screen("screenMain")
    def Kill():
        stats = "Second"

label beginning:
    $hideAll()



screen death():
    text "death"
    $ hideAll()
    zorder 2

    vbox:

        hbox:
            box_wrap True
            vbox:
                style_prefix "radio"
                label _("Kill")

                textbutton _("Kill Mario") action [Hide("death"), Kill(), Jump("peach")]
                textbutton _("Kill Peach") action Preference("display", "fullscreen")
                textbutton _("Kill BowserJr") action Preference("display", "fullscreen")

            vbox:
                style_prefix "radio"
                label _("Wifey")
                textbutton _("Marry Mario") action Preference("display", "window")
                textbutton _("Marry Peach") action Preference("display", "fullscreen")
                textbutton _("Marry BowserJr") action Preference("display", "fullscreen")

            vbox:
                style_prefix "check"
                label _("Skip")
                textbutton _("Unseen Text") action Preference("skip", "toggle")
                textbutton _("After Choices") action Preference("after choices", "toggle")
                textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

            ## Additional vboxes of type "radio_pref" or "check_pref" can be
            ## added here, to add additional creator-defined preferences.

        null height (4 * gui.pref_spacing)

        hbox:
            style_prefix "slider"
            box_wrap True

            vbox:

                label _("Text Speed")

                bar value Preference("text speed")

                label _("Auto-Forward Time")

                bar value Preference("auto-forward time")

            vbox:

                if config.has_music:
                    label _("Music Volume")

                    hbox:
                        bar value Preference("music volume")

                if config.has_sound:

                    label _("Sound Volume")

                    hbox:
                        bar value Preference("sound volume")

                        if config.sample_sound:
                            textbutton _("Test") action Play("sound", config.sample_sound)


                if config.has_voice:
                    label _("Voice Volume")

                    hbox:
                        bar value Preference("voice volume")

                        if config.sample_voice:
                            textbutton _("Test") action Play("voice", config.sample_voice)

                if config.has_music or config.has_sound or config.has_voice:
                    null height gui.pref_spacing

                    textbutton _("Mute All"):
                        action Preference("all mute", "toggle")
                        style "mute_all_button"


screen example_imagemap:
    zorder 5
    imagemap:
        auto "worldmap_%s.jpg"

        hotspot (850, 400, 400, 400) clicked Return("center")
        hotspot (150, 500, 300, 300) clicked Return("bowserjr")
        hotspot (1700, 20, 200, 300) clicked Return("peach")
        hotspot (790, 20, 200, 200) clicked Return("boo")
