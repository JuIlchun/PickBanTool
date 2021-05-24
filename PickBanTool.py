import ChampionClass
class pick :
    def _init_(self, top, jungle, mid, bot, support) :
        self.top = top
        self.jungle = jungle
        self.mid = mid
        self.bot = bot
        self.support = support

red_ban = pick(0,0,0,0,0)
red_pick = pick(0,0,0,0,0)
blue_ban = pick(0,0,0,0,0)
blue_pick = pick(0,0,0,0,0)

def banpick(mode, champ, team) : # team true = blue false = red
    champ_list.py.champ.ban = True
    num = champ_list.py.champ.index

    if mode == True : #벤 모드
        if team == True : #블루팀 벤
            for i in blue_ban :
                if i == 0 :
                    i = num
                    break
        elif team == False : # 레드팀 벤
            for i in red_ban :
                if i == 0 :
                    i = num
                    break

    elif mode == False : # 픽 모드
        if team == True : #블루팀 픽
            for i in blue_pick :
                if i == 0 :
                    i = num
                    break
        elif team == False : # 레드팀 픽
            for i in red_pick :
                if i == 0 :
                    i = num
                    break
    
    return red_ban, red_pick, blue_pick, blue_ban