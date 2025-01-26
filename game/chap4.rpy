label c4:
    #Back to Blue's perspective
    stop voice
    play music "Blue.wav" loop
    scene bg blue room with fade 
    show blue upset at left with fade

    "Blue is on a video call with work collegues."
    q "Blue can you handle this one?"
    aq "Give it to me instead. Blue will just make a mess like last time."
    blue "..."
    q "How about it Blue?"
    blue "I'm up for any task."

    "From the corner of the room, something shiny emerged."
    blue "A bubble?"
    aq "What?"
    q "Are you paying attention Blue?"
    blue "Of course!"

    show waterMon at right with zoomin
    call waterMonFight
    if (blue_hp < 1):
        jump game_over
    
    aq "This was why I said to just fire Blue..."
    show blue confused
    blue "?!"
    q "I need to talk alone with Blue."

    "The person left the call, leaving Blue with the supervisor."

    q "*sighs*"
    q "Listen Blue. You only get so many chances. If you mess up this time..."
    blue "You'll fire me."
    q "I'll have to deem you unqualified for this job."
    blue "*Nods*"
    q "Do you have anything to say?"
    blue "*Shakes head*"
    q "*sighs* I don't think you understand the position you're in."
    blue "..."
    q "We'll have no choice but to let you go if this keeps up."
    blue "I understand."
    q "Do you really?"
    blue "..."
    q "I can't stay in this meeting long. I'll discuss this thoroughly at a later date."
    blue "*nods*"
    "After the video call ended, Blue stretched."
    blue "Alright time to work!"
    "After work, Blue lies still in bed."
    "What should Blue do?"
    menu:
        "Call the supervisor":
            scene bg blue room with fade 
            show blue upset at left with fade
            "Blue called the supervisor."
            blue "You said you wanted to discuss further with me."
            q "I know I said we needed to have a discussion but it's after work hours."
            blue "..."
            q "I'm not in a good mood right now. I'll let you know on a later date when to -"
            show waterMon at right with zoomin
            call waterMonFight
            if (blue_hp < 1):
                jump game_over
            show blue confused
            q "Hey! Are you listening?"
            blue "Maybe I shoud just quit"
            q "..."
            "The supervisor hangs up the call."
            "Blue stares at the ceiling for a long time..."
            scene bad end with fade
            pause 5.0
            jump selfcredits

            return
            #bad end
        "Go for a walk":
            scene bg river with fade 
            show blue neutral at left with fade
            blue "..."
            blue "I wish this river could wash all the bad stuff away..."
            show waterMon at right with zoomin
            call waterMonFight
            if (blue_hp < 1):
                jump game_over
            show micah upset at right with moveinright
            micah "Why were you just throwing your arms out like that? Is that a new form of Tai Chi?"
            show blue confused
            blue "AHHHHH! AHHHH?! Uh... Micah?"
            show micah happy
            micah "Yeah, that's my name!"
            blue "You didn't see it?"
            show micah upset
            micah "See what?"
            blue "The water bubble monster! I was fighting it!"
            micah "..."
            blue "..."
            micah "Blue..."

            #new sprite blue crying
            blue "You don't believe me do you?"
            blue "It feels like I'm trapped in this bubble and no one cares."
            blue "I say everything's fine because it's suposed to be."
            blue "But no one even bothers to look inside the bubble."
            blue "And I'm just slowly dying inside it."
            blue "Do you know what that feels like?"

            micah "Blue... are you okay?"

            blue "No! Is that what you want me to say?"
            blue "No, I'm not okay and it's not like everything becomes okay just because I say I'm hurting out loud."
            blue "..."
            micah "..."
            blue "I want to go home."
            blue "But the water bubble monster is there too."
            blue "All those shiny perfect bubbles."
            blue "I wish the water will take me away."
            blue "To a place far, far, far away from here."

            micah "The monsters aren't real. You'll be okay Blue. We'll figure somethin-"

            blue "Are you real?"
            micah "What?"
            blue "Are you real?"
            micah "Obviously."
            blue "That's how real the monsters are to me."

            micah "Okay."
            blue "..."
            micah "Okay, I believe you. I'm just going to assume I couldn't see the monster because it camouflaged with the river or something."

            blue "I'm sorry."
            micah "About what?"
            blue "The drowning thing. I really didn't see or hear you."
            blue "I tend to do this thing where my mind wanders far, far away."
            blue "And I lose track of everything around me."
            blue "I'm about to lose my job because of it and well you already know my romantic life is burning to dust."
            blue "I thought being an adult meant I would have more control over my life."
            blue "Turns out, it just gets harder to control."
            blue "But I've been an awful friend. And it nearly cost your life."
            blue "It was my fault. All of it. I'm sorry"
            
            micah "I forgive you."

            "..."

            show blue neutral

            blue "You're too sweet for me sometimes."
            micah "So are you, cheesecake."


            jump c5
            #good end and go to chap 5



    return