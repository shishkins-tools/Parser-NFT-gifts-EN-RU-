#(RU) parser_by_shishkin-tools
#Я ВЕРЮ В ЧУДЕСА...

import tkinter as tk
from tkinter import messagebox
import random
NFT_COLLECTIONS = {
    "HeartLocket": 1949,      "PlushPepe": 2825,      "HeroicHelmet": 3414,
    "MightyArm": 3800,        "MagicPotion": 4871,    "MiniOscar": 4861,
    "IonGem": 4534,           "DurovsCap": 4709,      "PreciousPeach": 3000,
    "PerfumeBottle": 4403,    "NailBracelet": 4684,   "AstralShard": 5640,
    "GemSignet": 6149,        "ArtisanBrick": 6275,   "GenieLamp": 6508,
    "BondedRing": 7819,       "SharpTongue": 8099,    "ElectricSkull": 9211,
    "BlingBinky": 9321,       "RareBird": 11906,      "WestsideSign": 11490,
    "SignetRing": 16743,      "NekoHelmet": 15509,    "IonicDryer": 19870,
    "SwissWatch": 25701,      "DiamondRing": 32248,   "RecordPlayer": 33318,
    "LowRider": 23429,        "KhabibsPapakha": 28534, "EternalRose": 30908,
    "TopHat": 34338,          "SnowGlobe": 52493,     "ToyBear": 55821,
    "VintageCigar": 26335,    "SleighBell": 21924,    "FlyingBroom": 24714,
    "EternalCandle": 44965,   "HexPot": 55497,        "HangingStar": 44817,
    "SakuraFlower": 87632,    "BunnyMuffin": 51435,   "EvilEye": 73180,
    "SpyAgaric": 86704,       "WinterWreath": 72262,  "WitchHat": 82375,
    "SantaHat": 68659,        "SnowMittens": 38694,   "UFCStrike": 58406,
    "ValentineBox": 34426,    "CupidCharm": 29966,    "LovePotion": 29093,
    "LoveCandle": 23343,      "CookieHeart": 188019,  "TrappedHeart": 24883,
    "InstantRamen": 374132,   "SnoopDogg": 580200,    "IceCream": 324901,
    "HappyBrownie": 218297,   "WhipCupcake": 263907,  "LolPop": 432737,
    "DeskCalendar": 295664,   "XmasStocking": 210704, "CandyCane": 212201,
    "FreshSocks": 160000,     "CloverPin": 227607,    "SwagBag": 231259,
    "VictoryMedal": 94188,    "FaithAmulet": 136698,  "FancyPants": 142800,
    "SmartDoge": 95400,       "MousseCake": 163971,   "SnakeBox": 172698,
    "LunarSnake": 191154,     "B-DayCandle": 267956,  "PetSnake": 177074,
    "PrettyPosy": 119192,     "SpringBasket": 174105, "JesterHat": 135745,
    "StellarRocket": 135890,  "GingerCookie": 143311, "JollyChimp": 115876,
    "RestlessJar": 100186,    "MoneyPot": 70307,      "JingleBells": 73652,
    "LightSword": 124304,     "InputKey": 129245,     "PartySparkler": 178478,
    "MoonPendant": 101834,    "LushBouquet": 105680,  "JellyBunny": 102966,
    "TamaGadget": 103166,     "HolidayDrink": 83877,  "BigYear": 74660,
    "HomemadeCake": 178880,   "JoyfulBundle": 79232,  "Jack-in-the-Box": 96113,
    "SpicedWine": 102359,     "EasterEgg": 162412,    "HypnoLollipop": 80029,
    "StarNotepad": 69525,     "BowTie": 55087,        "BerryBox": 50711,
    "SnoopCigar": 117254
}
FILE_NAME = "links.txt"
def save_to_file(links):
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            f.write("\n".join(links))
        messagebox.showinfo("Успешно!", f"Ссылки успешно записаны в: {FILE_NAME}")
    except Exception as e:
        messagebox.showerror("Ошибка?!", f"Не удалось записать файл: {e}")
def generate_ten():
    all_keys = list(NFT_COLLECTIONS.keys())
    selected = random.sample(all_keys, 10)
    links = [f"https://t.me/nft/{k}-{random.randint(1, NFT_COLLECTIONS[k])}" for k in selected]
    save_to_file(links)
def generate_all():
    links = []
    for collection, max_id in NFT_COLLECTIONS.items():
        nft_id = random.randint(1, max_id)
        links.append(f"https://t.me/nft/{collection}-{nft_id}")
    save_to_file(links)
root = tk.Tk()
root.title("(RU) NFT Link Generator")
root.geometry("300x200")
label = tk.Label(root, text=f"В базе данных: {len(NFT_COLLECTIONS)} NFT коллекций.", pady=20)
label.pack()
btn_ten = tk.Button(root, text="10 рандомных NFT", command=generate_ten, width=25, height=2)
btn_ten.pack(pady=5)
btn_all = tk.Button(root, text="По одному из всех", command=generate_all, width=25, height=2)
btn_all.pack(pady=5)
root.mainloop()
