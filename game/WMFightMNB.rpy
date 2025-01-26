label wmFightMnB:
    "Water Bubble Monster is attacking! Prepare to fight!\nWater Monster's HP: [wmHp] \nBlue and Micah's HP: [bnm_hp]"
    while wmHp > 0:
        if (bnm_hp > 0):
            menu:
                "Attack together":
                    $ bnm_hp = bnm_hp - 10
                    show waterMon hit
                    "Blue and Micah were attacked!"
                    $ wmHp = wmHp - 20
                    "Blue and Micah struck back!"
                    show waterMon damaged 
                    "Water Monster's HP: [wmHp] \nBlue and Micah's HP: [bnm_hp]"
                    show waterMon
                "Block and half attack":
                    $ bnm_hp = bnm_hp - 5
                    show waterMon red 
                    $ wmHp = wmHp - 10
                    show waterMon blocked
                    "Blue and Micah were attacked but only took light damages."
                    "Blue and Micah swung back immediately!"
                    "Water Monster's HP: [wmHp] \nBlue and Micah's HP: [bnm_hp] \nBlue and Micah won't move ahead without fighting back!"
                    show waterMon 
                "Take a deep breath":
                    $ bnm_hp = bnm_hp + 20
                    show waterMon light 
                    $ wmHp = wmHp - 10
                    "Water Monster's HP: [wmHp] \nBlue and Micah's HP: [bnm_hp] \n..."
                    "..."
                    show waterMon
        elif (bnm_hp <= 0):
            return
    
    show waterMon dead
    "...\nCongratulations!"
    hide waterMon
    
    $ bnm_hp = 200  # Reset HP
    $ wmHp = 50
    "Blue and Micah won!"
    return