label c2:
    stop voice
    play music "Blue.wav" loop
    scene bg blue room with fade 
    show blue confused at left with fade
    "Blue thought that coming home would help."
    "However..."
    show waterMon at right with zoomin
    blue "Not again!"
    call waterMonFight
    if (blue_hp < 1):
        jump game_over
    blue "What is going on? I don't understand!"

    "What should Blue do?"

    menu:
        "Message Micah an apology and explain that you don't understand what's going on and about the strange Water Bubble Monsters":
            hide blue confused
            blue "Hey Micah, I know what I did earlier was terrible."
            blue "I still don't really get everything that happened."
            blue "I didn't realize so much time had passed and I genuinely did not hear you calling for me."
            blue "It must have been a really dangerous situation to be stuck in. I'm sorry for not realizing sooner."
            blue "I hope you'll forgive me and I hope you're okay."
            blue "These strange water bubble monsters attacked me after you left and I'm really scared."
            "Sent."
            "Blue knew it could have done without the last line but it did feel better to get it out."
            "Water bubble monsters. Something that now exists."
            "Ding!"
            micah "Honestly, these water bubble monsters you mention as well as ur lack of time awareness is concerning."
            micah "But I need time to process tdy."
            micah "Also, u literally left me to die. How am I supposed to forgive u for that?"
            blue "It was really an accident. If I knew you were in danger, I would have saved you. Promise!"
            micah "But you didn't! u know what? I'm too tired for this. Let's talk tmr."
            blue "kay. TTYL."
            show blue upset at left with fade
            blue "I hurt my best friend. I'm an awful person."
            blue "I'm so tired. I should head to bed."
            hide blue upset
            scene bg blue room with fade 
            show blue neutral at left with moveinright
            blue "Good Morning Sweet Day!"
            blue "Yesterday was-"
            show blue upset
            blue "Oh. Right."
            hide blue upset 

            jump c3
            #Good path


        "Beg Micah for forgiveness":
            hide blue confused
            blue "You're my best friend Micah! I'm really sorry for what happened earlier."
            blue "Please forgive me"
            blue "Please"
            blue "Please"
            blue "IK I was an awful friend kay?"
            blue "Just please forgive me?"
            blue "Hey?"
            blue "Hello?"
            blue "Please answer Micah"
            blue "Micah I'm crying. Please."
            blue "I can't lose u"
            blue "I promise I'll do anything to make it up to u"
            blue "Please. I'll give you anything you want."
            blue "You know what?"
            blue "This silent treatment is bs"
            blue "UR BS"
            blue "I'VE BEEN UR FRIEND FOR SO LONG"
            blue "BUT U CAN'T EVEN HEAR ME OUT ON ONE SIMPLE MISTAKE?"
            blue "UR THE AWFUL FRIEND"
            "..."
            show blue upset
            "All the messages were sent and the only thing remaining was immense regret."
            "Blue didn't mean to escalate things to these awful proportions."
            blue "It's fine."
            blue "I can do this on my own anyways."
            jump c2bad
            #Bad end


        "Try and figure out on your own":
            jump c2bad
            #Bad end
    return