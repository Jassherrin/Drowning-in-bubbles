# Declare characters used by this game. The color argument colorizes the
# name of the character.
define blue = Character("Blue", color="#75aeff")
define micah = Character("Micah", color="#ffa7ff")
define q = Character("???", color="#c9c9c9")
define aq = Character("???", color="#f2a654")

#Blue 
image blue neutral:
     "Blue neutral.png"
     pause 1.0
     "Blue neutral blink.png"
     pause 0.5
     "Blue neutral half blink.png"
     pause 0.5
     repeat
image blue upset ="Blue sad.png"
image blue happy = "Blue happy.png"
image blue confused = "Blue confused.png"
image blue swim h = "Blue swim happy.png"
image blue swim u = "Blue swim shock.png"

default blue_hp = 100



#Micah
image micah neutral = "Micah neutral.png"
image micah upset = "Micah sad.png"
image micah happy = "Micah happy.png"
image micah enraged = "Micah enraged.png"
image micah swim e = "Micah swim enraged.png"

#Water Monster
image waterMon = "Water monster.png"
image waterMon blocked = "Water monster blocked.png"
image waterMon crit = "Water monster crit.png"
image waterMon hit = "Water monster hit.png"
image waterMon damaged = "Water monster damage.png"
image waterMon red = "Water monster small dmg.png"
image waterMon light = "Water monster light dmg.png"
image waterMon dead:
     "Water monster d1.png"
     pause 0.5
     "Water monster d2.png"
     pause 0.5
     "Water monster d3.png"
     pause 0.5
default wmHp = 50
