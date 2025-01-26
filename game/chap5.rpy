label c5:
    stop voice
    play music "chill_day.mp3" loop
    scene bg micah room with fade 
    show micah happy at left with fade
    show blue neutral at right with moveinright

    micah "You sure they'll show?"
    blue "They attack me quite often."
    hide blue neutral
    show waterMon at right with moveinright
    show blue neutral
    micah "AHHH! IT! IT'S!"
    blue "It's here. Told you it was real."
    show micah happy
    micah "Unbelievable."
    call wmFightMnB from _call_wmFightMnB
    if (bnm_hp < 1):
        jump game_over
    

    scene bg micah room with fade 
    show micah happy at left with fade
    show blue neutral
    blue "It's easier to fight them with you."
    micah "Maybe because they were never meant to be fought alone."
    blue "You're going to become the real cheesecake."
    micah "Ugh..."
    blue "Heh."



    scene bg blue room with fade 
    show micah happy at left with fade
    show blue neutral
    micah "Feels like forever since I stepped into your room."
    blue "You're not wrong. I haven't invited you a lot."
    micah "Why not though?"
    blue "Just wanted to keep you seperate enough from this place since it's also my 'office'"
    blue "I don't want to think about work when I'm with you."
    micah "Makes sense"


    scene bg river with fade 
    show micah happy at left with fade
    show blue neutral
    show waterMon at right with zoomin
    micah "Heh!"
    blue "We've fought many of these haha!"
    call wmFightMnB from _call_wmFightMnB_1
    if (bnm_hp < 1):
        jump game_over
    micah "The river is still pretty here."
    blue "Yeah."
    micah "How's work?"
    blue "Better."
    micah "I'm happy for you."
    blue "Thanks."
    micah "The bubble monsters are weird huh?"
    blue "What do you mean?"
    micah "Like why do we have to fight them?"
    blue "No idea."
    micah "Scary."
    blue "I'm just glad I have you now to fight against them."
    micah "Yeah, they aren't much of a threat when we're together."
    blue "Which just means we have more of a reason to keep to our contract."
    micah "Oh! You remember the contract?"
    blue "Of course! We are binded for eternity!"
    micah "..."
    micah "Why am I surprised the cheesecake remembered the cheesy promise?"
    blue "OI!"
    micah "I'm glad too. That we're friends for 'eternity'."
    show blue happy
    pause 1.0


    scene bg starry night with fade 
    show micah happy at left with fade
    show blue neutral at right with moveinright
    blue "Happy birthday Micah!"
    blue "Thank you for always being my best friend."
    blue "Thank you for caring enough to enter my 'bubble'"
    blue "You mean a lot to me and you will be my most precious and dearest friend."
    micah "This is like the best place for my birthday. Thank you Blue."
    blue "Honestly, I just wanted to come here with you again too."
    blue "This place is to die for."
    micah "This place is to live for."
    show blue happy
    blue "!"
    blue "Yeah, this place is to live for."
    scene good end with fade
    pause 5.0
    #Good ending screen and then credits
    jump selfcredits



    return