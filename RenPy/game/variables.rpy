#Characters
define e = Character("Mario", image="Mario")
define me = Character("Me", color="#f47a42")
define peach = Character("Peach", image="Peach")
define bowserjr = Character("Bowserjr", image = "bowser")

#Backgrounds
image bg marioland = "marioland.jpg"

init python:
    STAT_MAX = 100
    charisma = 5
    intel = 5
    strength = 5
    motivation = 5
    creativity = 5
    marioRel = 0
    peachVisited = 0

    anxrom = 0
    lorom = 0
    prom = 0
    morom = 0
    thomasfriend = 0

    fn = "Rien"
    ln = "Williams"


#Skipping purposes
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



define anx = Character (_('Anxiety'), color = "#8E8192")
define virg = Character (_('Virgil'), color = "#8E8192")
define lo = Character (_('Logan'), color = "#37578C")
define mo = Character (_('Patton'), color = "#489ECD")
define ro = Character (_('Roman'), color = "#A73636")
define ts = Character (_('Thomas'), color = "#B22222")
define yn = Character (_('[fn]'), color = "#ffffff")
define u = Character (_('???'), color = "#ffffff")

image player room morning = "Player_Room_Sunrise.png"
image player room midday = "Player_Room_Midday.png"
image player room sunset = "Player_Room_Sunset.png"
image player room night = "Player_Room_NightTime.png"
image black = "blank.png"
