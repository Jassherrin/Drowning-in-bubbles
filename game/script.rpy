# The script of the game goes in this file.
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg river

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show blue neutral


    # These display lines of dialogue.
    "The heat was sweltering. It was something no fan or air-con could fix."
    "Even the 'coldest' nights were warm enough to sweat through."

    blue "This heat is too much."
    micah "Yeah. The river looks refreshing though."
    blue "Ugh…"
    micah "..."
    blue "Uggggghhhhh…."
    micah "So much for a sweet walk by the river. This would be nicer if you stopped groaning."
    blue "..."
    micah "..."
    blue "I want to jump in the river..."
    micah "*Sighs*"
    blue "It's too hotpot!"
    micah "You suggested this!"
    blue "Yea, we should have gone swimming instead."

    "Micah froze up immediately looking awkward."

    show blue upset

    "Blue looked concerned."

    blue "Do you… like have a phobia of water or something?"
    micah "Oh. No no it's nothing like that. It's just I have never tried swimming before."
    blue "Wait, what? I thought swimming lessons were, like, mandatory."
    micah "My school didn't have anything like that."

    # This ends the game.

    return
