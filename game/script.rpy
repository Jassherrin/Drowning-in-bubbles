label start:
    "The heat was sweltering. It was something no fan or air-con could fix."
    "Even the 'coldest' nights were warm enough to sweat through."

    scene bg river with dissolve 
    "2.36pm. Two friends walking by a river."

    show blue neutral at left 
    # with dissolve
    blue "This heat is too much."
    show micah neutral at right with moveinright
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

    show micah upset

    "Micah froze up immediately looking awkward."

    show blue upset

    "Blue looked concerned."

    blue "Do you… like have a phobia of water or something?"
    micah "Oh. No no it's nothing like that. It's just I have never tried swimming before."
    blue "Wait, what? I thought swimming lessons were, like, mandatory."
    micah "My school didn't have anything like that."

    #FOXY
    show blue happy
    blue "It's not too late to learn!"
    show micah happy
    micah "Why not? It beats standing here listening to you grumble."
    blue "OI!"

    #Scene change to swimming pool
    scene bg swimming pool
    "A few days later, the duo go to the swimming pool."
    "Blue is swimming on his own while Micah is swimming with floaties."

    "Blue is drifting away any thoughts and heat with swimming."
    show blue swim h at left with moveinleft

    blue "This is the best!"
    "Time passes by peacefully."

    "..."
    "..."
    micah "...Blue..."
    micah "...hey..."
    micah "...are you listening...?"
    show micah swim e at right with zoomin
    micah "BLUE!"
    blue "Huh? what?"
    "Micah looks at Blue enraged."
    show blue swim u at left 
    blue "Why? What happened?"
    micah "I nearly drowned!"
    menu:
        "Are you joking?":
            jump c1bad
        "What? I didn't see that. I'm so sorry. When did it happen?":
            micah "What do you mean you didn't see? I was right here! I was screaming for you!"
            blue "Micah, I really didn't notice-"
            micah "I could have died! If a passerby hadn't seen the bubbles while I was under, I could have died!"
            "Blue looked around confused. When they came in, it was packed. Now there were only a handful of swimmers."
            blue "What... time is it?"
            micah "I've been telling you all day that we should head home!"
            blue "Wait? What? We've been here that long?"
            micah "I've had enough. I'm going home!"
            blue "Oh! Um..."
            hide micah swim e
            "Left behind, Blue wonders how so many things happened yet seemed like it didn't."
            blue "I don't understand..."
            jump c2


    return
