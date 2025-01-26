# Declare characters used by this game. The color argument colorizes the
# name of the character.
define blue = Character("Blue", color="#00285f")
define micah = Character("Micah", color="#700000")
define q = Character("Supervisor", color="#000000")
define aq = Character("Collegue", color="#fb8200")

#Blue 
image blue neutral:
     "Blue neutral.png"
     pause 1.0
     "Blue neutral blink.png"
     pause 0.5
     "Blue neutral half blink.png"
     pause 0.5
     repeat
image blue upset:
     "Blue sad.png"
     pause 1.0
     "Blue sad blink.png"
     pause 0.5
     repeat
image blue happy:
     "Blue happy.png"
     pause 1.0
     "Blue happy blink.png"
     pause 0.5
     repeat
image blue confused:
     "Blue confused.png"
     pause 1.0
     "Blue confused blink.png"
     pause 0.5
     repeat
image blue swim h:
     "Blue swim happy.png"
     pause 1.0
     "Blue swim happy blink.png"
     pause 0.5
     repeat
image blue swim u = "Blue swim shock.png"

default blue_hp = 100



#Micah
image micah neutral:
     "Micah neutral.png"
     pause 1.0
     "Micah neutral blink.png"
     pause 0.5
     repeat
image micah upset:
     "Micah sad.png"
     pause 1.0
     "Micah sad blink.png"
     pause 0.5
     repeat
image micah happy:
     "Micah happy.png"
     pause 1.0
     "Micah happy blink.png"
     pause 0.5
     repeat
image micah enraged:
     "Micah enraged.png"
     pause 1.0
     "Micah enraged blink.png"
     pause 0.5
     repeat
image micah swim e:
     "Micah swim enraged.png"
     pause 1.0
     "Micah swim enraged blink.png"
     pause 0.5
     repeat

default bnm_hp = 200


#Water Monster
image waterMon = "Water monster.png"
image waterMon blocked = "Water monster blocked.png"
image waterMon crit = "Water monster crit.png"
image waterMon hit = "Water monster hit.png"
image waterMon damaged = "Water monster damage.png"
image waterMon tgth damaged = "Water monster tgth damage.png"
image waterMon red = "Water monster small dmg.png"
image waterMon light = "Water monster light dmg.png"
image waterMon tgth light = "Water monster tgth light dmg.png"
image waterMon dead:
     "Water monster d1.png"
     pause 0.5
     "Water monster d2.png"
     pause 0.5
     "Water monster d3.png"
     pause 0.5
default wmHp = 50
