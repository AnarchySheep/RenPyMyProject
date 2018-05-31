style statscreenstyle:
    xpadding 0
    xmargin 0
    xspacing 0
    yspacing 1
    xalign 0.05
    xfill False
    justify False
    spacing 0
    fit_first "width"


screen display_stats(name=True, bar=True, value=True, max=True):
    #   Tag menu removes everything with same tag
    #   Parsed as a name, not an expression. This specifies a tag associated with this screen. Showing a screen replaces other screens with the same tag. This can be used to ensure that only one screen of a menu is shown at a time, in the same context.
    zorder 101
    frame:
        yalign 0.000001
        xalign 0.99999
        xmargin 0
        ymargin 0


        vbox:
            style "statscreenstyle"



            $ number_of_stats = 5
            grid 3 number_of_stats :
                style "statscreenstyle"

                label "Charisma"  style "statscreenstyle"
                bar value charisma range STAT_MAX xmaximum 200 xalign 0.1
                label ("%d/%d" % (charisma, STAT_MAX)) xalign 0.5

                label "Creativity" style "statscreenstyle"
                bar value intel range STAT_MAX xmaximum 200 xalign 0.1
                label ("%d/%d" % (creativity, STAT_MAX)) xalign 0.5

                label "Intelligence" style "statscreenstyle"
                bar value intel range STAT_MAX xmaximum 200 xalign 0.1
                label ("%d/%d" % (intel, STAT_MAX)) xalign 0.5

                label "Motivation" style "statscreenstyle"
                bar value motivation range STAT_MAX xmaximum 200 xalign 0.1
                label ("%d/%d" % (motivation, STAT_MAX)) xalign 0.5

                label "Strength" style "statscreenstyle"
                bar value strength range STAT_MAX xmaximum 200 xalign 0.1
                label ("%d/%d" % (strength, STAT_MAX)) xalign 0.5
