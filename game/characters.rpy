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
image blue swim h = "Blue swim happy.png"
image blue swim u = "Blue swim shock.png"



#Micah
image micah neutral = "Micah neutral.png"
image micah upset = "Micah sad.png"
image micah happy = "Micah happy.png"
image micah enraged = "Micah enraged.png"
image micah swim e = "Micah enraged.png"
