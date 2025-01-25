label waterMonFight:
    "Water Bubble Monster is attacking! Prepare to fight!"
    while wmHp > 0:
        if (blue_hp > 0):
            menu:
                "Swing arms widely":
                    $ blue_hp = blue_hp - 10
                    show waterMon hit
                    "Blue was attacked!"
                    $ wmHp = wmHp - 10
                    "Blue struck back!"
                    show waterMon damaged 
                    "Water Monster's HP: [wmHp] \nBlue's HP: [blue_hp]"
                    show waterMon
                "Cry":
                    $ blue_hp = blue_hp - 20
                    show waterMon crit
                    "Blue was attacked harshly!"
                    "Water Monster's HP: [wmHp] \nBlue's HP: [blue_hp] \nCrying is useless..."
                    show waterMon
                "Block and half swing":
                    $ blue_hp = blue_hp -5
                    show waterMon red 
                    $ wmHp = wmHp - 5
                    show waterMon blocked
                    "Blue was attacked but only took light damages."
                    "Blue swung back immediately!"
                    "Water Monster's HP: [wmHp] \nBlue's HP: [blue_hp] \nBlue won't move ahead without fighting back!"
                    show waterMon 
                "Take a deep breath":
                    $ blue_hp = blue_hp + 10
                    show waterMon light 
                    $ wmHp = wmHp - 5
                    "Water Monster's HP: [wmHp] \nBlue's HP: [blue_hp] \n..."
                    "..."
                    show waterMon
        else:
            "Blue died!"
            return
    show waterMon dead
    "...\nCongratulations!"
    hide waterMon
    
    $ blue_hp = 100
    $ wmHp = 50
    "Blue won!"
    "HP fully restored!"