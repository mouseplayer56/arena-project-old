from itertools import count
from itertools import cycle
import random
hh=""
h="------"
game=0
pregame=0
enchance=0

while pregame==0:
    play=input("Enter Name: ")
    print(play)
    pregame=1
    while play!=None:
        playtwo=input("Are you sure? (Y/N) ")
        playtwo=playtwo.lower()
        
        if playtwo=="n":
            play=None
            pregame=0
        if playtwo=="y":
            game=1
            print("'",play,"' chosen.")
            menu=1
            gamestart=1
            play=None
        else:
            print("Please try again.")
            
def options():
    print("1.START GAME")
    print("2.ARMOURY")
    print("3.SKILLS")
    print("4.SETTINGS")
    print(hh)
    menuinput=int(input("Insert corresponding number: "))
    return menuinput

def enintro(name,health,stamina,mana,aggressiveness,damage):
    print("'",name,"'")
    print("Lethality [",damage,"]")
    print("Health:",health)
    print("Stamina:",stamina)
    print("Mana:",mana)
    print("Aggressiveness:",aggressiveness)

def cmds():
    print(" hit")
    print(" stand")
    print(" end")
    print(" cmds")
    print(" info")
    print(" [DEV]self")
    print(" [DEV]enemy")
    print(" [DEV]enemych")
    print(" [DEV]newenemych")
    print(" [DEV]kill")
    print(" exit")
    
def cmdsexpanded():
    print(" hit - damages the opponent.")
    print(" stand - regain health+stamina+mana at the cost of a 'turn point'.")
    print(" end - ends your turn completely.")
    print(" cmds - shows available commands.")
    print(" info - expands on available commands.")
    print(" [DEV]self - view your stats.")
    print(" [DEV]enemy - view your enemy's stats.")
    print(" [DEV]enemych - the number your enemy rolled (enemy chance).")
    print(" [DEV]newenemych - the number a new enemy rolls (new enemy chance).")
    print(" [DEV]kill - sets enemy health to -99. ¯\_(ツ)_/¯")
    print(" exit - leave on your current wave.")

def armcmds():
    print(" upgwpn: upgrades your weapon.")
    print(" upgwpn path: displays weapon upgrades available.")
    print(" d/upghl: improves your health.")
    print(" d/upgst: improves your stamina.")
    print(" d/upgm: improves your mana.")
    print(" d/upgstand: improves your stance when standing.")
    print(" exit: leave.")

fists=10
brassk=20
knife=30
bayonet=35
karambit=35
glock=45
glocksl=50
mkrov=50
mkrovsl=55
fn=60
fnsl=65
fntact=75
famas=35
famassl=40
famastact=50
famasmarks=150
marks=100
markssl=105
markstact=120
fiftybmg=200
fiftybmgsl=210
fiftybmgtact=225
namesbond=700

wpnwheel=["fists","brassk","knife","bayonet","karambit","glock","glocksl","mkrov","mkrovsl","fn","fnsl","fntact","famas","famassl","famastact","famasmarks","marks","markssl","markstact","fiftybmg","fiftybmgsl","fiftybmgtact"]
wpnvalwheel=["fists=10","brassk=20","knife=30","bayonet=35","karambit=35","glock=45","glocksl=50","mkrov=50","mkrovsl=55","fn=60","fnsl=65","fntact=75","famas=35","famassl=40","famastact=50","famasmarks=150","marks=100","markssl=105","markstact=120","fiftybmg=200","fiftybmgsl=210","fiftybmgtact=225"]

wpndefinitions={}
for item, definition in zip(wpnwheel, wpnvalwheel):
    key, value=definition.split("=")
    wpndefinitions[item]=int(value)

while game==1:
    if gamestart==1:
        print(hh)
        print(h)
        print("MENU ACTIVATED")
        print(h)

        maxhealth=100
        healhealth=10
        maxstamina=100
        healstamina=20
        maxmana=100
        healmana=5
        dodge=0
        startingwave=0
        maxturnpoints=2
        wpn=fists
        wpnshow="fists"

        deathcard=0
        
        gamestart=0


    while menu==1:
        menuoutput=0
        menuinput=options()

        while menuinput==2:
##            print(hh)
##            if wpn in wpnwheel:
##                wpnwheel.remove(wpn)
            print(wpnwheel)

            armcmds()
            print(hh)
            arminput=input("Enter an action. ")
            arminput=arminput.lower()
            if arminput=="upgwpn":
                if len(wpnwheel)==1:
                    print("hey, ho, no more to go.")
                    print(hh)
                    print("-", wpnshow)
                else:
                    wpnshow=wpnwheel[wpnwheel.index(wpnshow)+1]
                    wpnwheel.remove(wpnwheel[wpnwheel.index(wpnshow)-1])
                    wpn=wpnshow
                    print(wpnshow)
                    
            if arminput=="exit":
                menuinput==0
                if wpnshow in wpndefinitions:
                    wpn=wpndefinitions[wpnshow]
                print(wpn)
                break

            if arminput=="buyout":
                if len(wpnwheel)<=5:
                    print("hey ho, no more to go.")
                    print(hh)
                    print("-", wpnshow)
                elif len(wpnwheel)>5:
                    wpnshow=wpnwheel[wpnwheel.index(wpnshow)+5]
                    wpnwheel.remove(wpnwheel[wpnwheel.index(wpnshow)-1])
                    wpnwheel.remove(wpnwheel[wpnwheel.index(wpnshow)-1])
                    wpnwheel.remove(wpnwheel[wpnwheel.index(wpnshow)-1])
                    wpnwheel.remove(wpnwheel[wpnwheel.index(wpnshow)-1])
                    wpnwheel.remove(wpnwheel[wpnwheel.index(wpnshow)-1])
                    wpn=wpnshow
                    print(wpnshow)

        while menuinput==4:
            print(wpn, wpnshow)
            menuinput=0
            break
#--------------------------------------- THIS IS WHEN THE ACTUAL GAME STARTS
        
        while menuinput==1:
            playing=1
            loadout=1
            wave=startingwave
            thefirst=0
            thefirstnocommands=1
            while startingwave==0:
                en="Small Rat"
                enwpn=5
                enhealth=20
                enstamina=10
                enmana=0
                aggressiveness="30%"
                startingwave=1
                break
            while loadout==1:
                health=maxhealth
                stamina=maxstamina
                mana=maxmana
                turnpoints=maxturnpoints
                loadout==0
                break
            while playing==1:
                if health>maxhealth:
                    health=maxhealth
                if stamina>maxstamina:
                    stamina=maxstamina
                if mana>maxmana:
                    mana=maxmana
                if health<=0:
                    print("WARNING, HEALTH CRITICAL.")
                    print("(GAME WILL END UNLESS ENEMY DIES OR HEALTH IS REGAINED)")
                if stamina<0:
                    stamina=0
                if mana<0:
                    mana=0

                if thefirst==0:
                    print(hh)
                    print("Wave",wave)
                    enintro(en,enhealth,enstamina,enmana,aggressiveness,enwpn)
                    print(hh)
                    print(h)
                    print("Available Commands ['info' for details]:")
                    cmds()
                    print(h)
                    print(hh)
                    thefirst=1

                if thefirstnocommands==0:
                    print(hh)
                    print("Wave",wave)
                    enintro(en,enhealth,enstamina,enmana,aggressiveness,enwpn)
                    print(h)
                    print(hh)
                    thefirstnocommands=1

                print("health: ",health,"/",maxhealth,":",enhealth)
                print("stamina: ",stamina,"/",maxstamina,":",enstamina)
                print("mana: ",mana,"/",maxmana,":",enmana)
                print("turns:",turnpoints,"/",maxturnpoints)
                
                action=input("Enter Action: ")
                if action=="info":
                    cmdsexpanded()
                if action=="cmds":
                    cmds()
                if action=="self":
                    print(health)
                    print(stamina)
                    print(mana)
                    print(turnpoints)
                    print(deathcard)
                if action=="enemy":
                    print(enhealth)
                    print(enstamina)
                    print(enmana)
                if action=="enemych" or action=="enchance" or action=="enemychance":
                    print(enchance)
                if action=="newenemych":
                    print(newenemy)
                if action=="hit" or action=="h":
                    if wpn=="knife" or wpn=="bayonet" or wpn=="karambit" or wpn=="fists" or wpn=="brassk":
                        pass
                    if wpn=="fists":
                        stamina-=2
                    if wpn=="brassk":
                        stamina-=4
                    else:
                        stamina-=3
                        enhealth-=wpn
                        turnpoints-=1
                    if stamina<0:
                        stamina=0
                        turnpoints+=1
                        enhealth+=wpn
                    if wpn=="glock" or wpn=="glocksl" or wpn=="mkrov" or wpn=="mkrovsl" or wpn=="fn" or wpn=="fnsl" or wpn=="fntact":
                        turnpoints-=2
                        enhealth-=wpn
                        enstamina-=10
                if action=="stand":
                    health+=healhealth
                    mana+=healmana
                    stamina+=healstamina
                    turnpoints-=1
                if action=="end":
                    turnpoints=0
                if turnpoints<=0:
                    enchance=random.randint(0,100)


#--------------------------------------- ENEMY ATTACK POOL
                    enact=0 # COPY: and enact==0
#------------------------------- =SEWERS_1

                    if en=="Small Rat":
                        if enchance>70 and enact==0:
                            if enstamina>=3 and enact==0:
                                enact=1
                                print("Enemy Action: hit")
                                health-=enwpn
                                enstamina-=3
                            if enstamina<=3 and enact==0:
                                enchance=70
                                enact=1
                        if enchance<=70 and enact==0:
                            print("Enemy Action: stand")
                            enhealth+=3
                            enstamina+=5
                            enact=1

                    if en=="Rat":
                        if enchance>55 and enact==0:
                            if enstamina>=7 and enact==0:
                                print("Enemy Action: hit")
                                health-=enwpn
                                enstamina-=7
                                enact=1
                            if enstamina<=7 and enact==0:
                                enchance=55
                                enact=1
                        if enchance<=55 and enact==0:
                            print("Enemy Action: stand")
                            enhealth+=4
                            enstamina+=6
                            enact=1

                    if en=="Large Rat":
                        if enchance>40 and enact==0:
                            if enstamina>=15 and enact==0:
                                print("Enemy Action: hit")
                                health-=enwpn
                                enstamina-=15
                                enact=1
                            if enstamina<=15 and enact==0:
                                enchance=40
                                enact=1
                        if enchance<=40 and enact==0:
                            print("Enemy Action: stand")
                            enhealth+=9
                            enstamina+=15
                            enact=1

                    if en=="[Remmy]":
                        if enchance>40 and not enchance>=75 and enact==0:
                            if enstamina>12 and enact==0:
                                print("Enemy Action: hit")
                                health-=enwpn
                                enstamina-=12
                                enact=1
                            if enstamina<=12 and enact==0:
                                enchance=40
                                enact=1
                        if enchance>=75 and enact==0:
                            if enmana>=15 and enact==0:
                                print("Enemy Action: fireball")
                                health-=int(enwpn+(enwpn/2))
                                enmana-=15
                                enact=1
                            if enmana<=15 and enact==0:
                                enchance=40
                                enact=1
                        if enchance<=40 and enact==0:
                            print("Enemy Action: stand")
                            enhealth+=9
                            enstamina+=3
                            enmana+=4
                            enact=1

#------------------------------- =CATACOMBS_2

                    if en=="Ferret":
                        if enchance<=60 and enact==0:
                            if enstamina>10 and enact==0:
                                print("Enemy Action: hit")
                                health-=enwpn
                                enstamina-=10
                                enact=1
                            if enstamina<=10 and enact==0:
                                enchance=61
                                enact=1
                        if enchance>60 and enact==0:
                            print("Enemy Action: stand")
                            enhealth+=6
                            enstamina+=4
                            enact=1
                            
                    if en=="Skunk":
                        if enchance<34 and enact==0:
                            if enmana>=15 and enact==0:
                                print("Enemy Action: gas")
                                health-=int(enwpn*3)
                                enmana-=15
                                enact=1
                            if enmana<=15 and enact==0:
                                enchance=100
                                enact=1
                        if enchance<85 and enchance>33 and enact==0:
                            if enstamina>10 and enact==0:
                                print("Enemy Action: hit")
                                health-=enwpn
                                enstamina-=10
                                enact=1
                            if enstamina<=10 and enact==0:
                                enchance=40
                                enact=1
                        if enchance>84 and enact==0:
                            print("Enemy Action: stand")
                            enhealth+=5
                            enstamina+=3
                            enmana+=3
                            enact=1
                            
                    if en=="Fox":
                        if enchance>=31 and enact==0:
                            if enstamina>15 and not enstamina==0 and enact==0:
                                print("Enemy Action: hit")
                                health-=enwpn
                                enstamina-=15
                                enact=1
                            if enstamina<=15 and enact==0:
                                enchance=30
                                enact=1
                        if enchance<31 and enact==0:
                            print("Enemy Action: stand")
                            enhealth+=2
                            enstamina+=10
                            enact=1

                    if en=="[Stoat]":
                        if enchance>25 and not enchance>=70 and enact==0:
                            if enstamina>12 and enact==0:
                                print("Enemy Action: hit")
                                health-=enwpn
                                enstamina-=4
                                enact=1
                            if enstamina<=12 and enact==0:
                                enchance=20
                                enact=1
                        if enchance>=70 and enact==0:
                            if enmana>=10 and enact==0:
                                print("Enemy Action: double hit")
                                health-=enwpn*2
                                enmana-=10
                                enstamina-=8
                                enact=1
                            if enmana<=10 and enact==0:
                                enchance=20
                                enact=1
                        if enchance<=25 and enact==0:
                            print("Enemy Action: stand")
                            enhealth+=4
                            enstamina+=5
                            enmana+=5
                            enact=1
                            
#--------------------------------------- NEW ENEMY
                    if wave%5==0 and not startingwave>wave:
                        startingwave=wave+1
                    if health<=0 or deathcard>=1:
                        deathcard+=1
                    turnpoints=maxturnpoints
                if action=="exit" or (health<=0 and deathcard>=2):
                    menuinput=0
                    print(hh)
                    print(" Health:",health,"(x-x)")
                    print(hh)
                    print("--GAME END--")
                    print(hh)
                    break
                if enhealth<=0:
                    wave+=1
                    thefirstnocommands=0
                    turnpoints=maxturnpoints
                    if deathcard>0:
                        health=1
                    deathcard=0
                    if wave<5:
                        newenemy=random.randint(0,100)
                        if newenemy>20:
                            en="Rat"
                            enwpn=10
                            enhealth=35
                            enstamina=50
                            enmana=0
                            aggressiveness="30%"
                        if newenemy<=20:
                            en="Large Rat"
                            enwpn=20
                            enhealth=50
                            enstamina=85
                            enmana=15
                            aggressiveness="60%"
                    if wave==5:
                        en="[Remmy]"
                        enwpn=20
                        enhealth=65
                        enstamina=125
                        enmana=30
                        aggressiveness="35%(+25%)"
                        
                    if wave>5 and wave<15 and not wave==10:
                        newenemy=random.randint(0,100)
                        if newenemy<46:
                            en="Ferret"
                            enwpn=10
                            enhealth=55
                            enstamina=70
                            enmana=10
                            aggressiveness="60%"
                        if newenemy<71 and newenemy>45:
                            en="Skunk"
                            enwpn=10
                            enhealth=30
                            enstamina=45
                            enmana=50
                            aggressiveness="50%(+33%)"
                        if newenemy>70:
                            en="Fox"
                            enwpn=25
                            enhealth=60
                            enstamina=40
                            enmana=0
                            aggressiveness="70%"
                    if wave==10:
                        en="[Stoat]"
                        enwpn=17
                        enhealth=160
                        enstamina=99
                        enmana=50
                        aggressiveness="45%(+30%)"
                print(hh)
