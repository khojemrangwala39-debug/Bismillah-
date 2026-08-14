def game_over():
    print("\n💀 GAME OVER!!! 💀")
    print("Dobara khelne ke liye 'python devil.py' chalao.\n")
    sys.exit()

print("====================================================")
print("😈 WELCOME TO LEVEL DEVIL - ULTIMATE TROLL GAME 😈")
print("====================================================")

# ----------------- LEVEL 1 -----------------
print("\n--- LEVEL 1: THE TWO BUTTONS ---")
print("Saamne do buttons hain: ek Lal (Red) aur ek Neela (Blue).")
print("[1] Lal button dabao\n[2] Neela button dabao\n[3] Board par zor se laat maar do")

c1 = input("Apna faisla chuno: ")
if c1 == "1":
    print("\n❌ TROLL: Lal button dabate hi bomb phat gaya! GAME OVER!")
    game_over()
elif c1 == "2":
    print("\n❌ TROLL: Neela button dabaya toh screen neeli ho gayi aur phone hang ho gaya! GAME OVER!")
    game_over()
elif c1 == "3":
    print("\n🔥 VIP UNLOCKED: Board toot gaya aur peeche se naya rasta khul gaya! Level 2 mein swagat hai!")
else:
    print("\n❌ Faltu bakwas ki toh Devil ne kacha chaba liya!")
    game_over()

# ----------------- LEVEL 2 -----------------
print("\n--- LEVEL 2: THE BROKEN BRIDGE ---")
print("Saamne ek toota hua pul (bridge) hai. Neeche gehri khayi hai.")
print("[1] Tezi se bhaag kar paar karo\n[2] Aaram se reng kar (crawl) paar karo\n[3] Aankhein band karke pichwade ke bal kood jao")

c2 = input("Apna faisla chuno: ")
if c2 == "1":
    print("\n❌ TROLL: Tezi se bhaage par pul beech mein se hi toot gaya! GAME OVER!")
    game_over()
elif c2 == "2":
    print("\n❌ TROLL: Reng kar ja rahe the tabhi ek chidiya ne sir par potty kar di, tum slip hoke neeche gir gaye! GAME OVER!")
    game_over()
elif c2 == "3":
    print("\n🔥 VIP UNLOCKED: Koodte hi neeche ek invisible gadda (trampoline) tha! Tum uchhal kar doosri taraf pahunch gaye! Level 3!")
else:
    print("\n❌ Galat input!")
    game_over()

# ----------------- LEVEL 3 -----------------
print("\n--- LEVEL 3: THE GIANT WALL ---")
print("Saamne ek deewar hai aur peeche se ek aur deewar aage aa rahi hai!")
print("[1] Deewar par mukka maaro\n[2] Peeche bhago\n[3] Pray karo")
print("💡 Hint: Apna Secret VIP code yaad hai na?")

c3 = input("Apna jawab chuno: ")
if c3 == "1":
    print("\n❌ TROLL: Mukka maara par deewar patthar ki thi, haath toot gaya! GAME OVER!")
    game_over()
elif c3 == "2":
    print("\n❌ TROLL: Peeche bhage par wahan toh pehle se hi kaante the! GAME OVER!")
    game_over()
elif c3 == "3":
    print("\n❌ TROLL: Tumne pray kiya aur Devil ne upar se ek mota patthar gira diya! GAME OVER!")
    game_over()
elif c3 == "007":
    print("\n😎 SECRET CODE UNLOCKED! Tum deewar ke aar-paar nikal gaye jaise bhoot!")
    print("🎉 ASLI VIP VICTORY! Tumne Devil ka sabse bada troll hara diya!")
else:
    print("\n❌ Galat button dabaya aur Devil ne tumhe kacha chaba liya! 💀")
    game_over()

# ----------------- EYE BREAK REMINDER -----------------
print("\n" + "🚨 " * 10)
print("⚠️ WARNING: 3 LEVELS COMPLETED!")
print("APNI AANKHON KO AARAM DO AUR FIR KHELNA!")
print("🚨 " * 10)
print("\nGame 5 second ke liye pause ho gayi hai... Break lo...")
time.sleep(5)

# ----------------- LEVEL 4 -----------------
print("\n--- LEVEL 4: THE ROBOT'S QUIZ ---")
print("Saamne ek ajeeb sa jadooi Robot khada hai.")
print("Robot bolta hai: 'Aage jaana hai toh maths ka simple sawal hal karo!'")
print("Sawal: 2 + 2 * 2 kitna hota hai?")
print("[1] 8 \n[2] 6 \n[3] Mujhe nahi pata, chal hatt!")

c4 = input("Apna jawab chuno: ")
if c4 == "1":
    print("\n❌ TROLL! Bachpan mein BODMAS nahi padha kya? Galat jawab! Robot ne laser se uda diya! GAME OVER!")
    game_over()
elif c4 == "2":
    print("\n❌ TROLL OVERLOAD! Jawab toh 6 sahi hai, par Robot bola: 'Mujhe hoshiyar log bilkul pasand nahi!'\nRobot ne kachre ke dabbe mein phenk diya! GAME OVER!")
    game_over()
elif c4 == "3":
    print("\n🔥 VIP UNLOCKED! Robot muskuraaya aur bola: 'Wah! Mujhe badtameez log hi pasand hain!'\nRasta khul gaya! Welcome to Level 5!")
else:
    print("\n❌ Galat input!")
    game_over()

# ----------------- LEVEL 5 -----------------
print("\n--- LEVEL 5: THE MYSTERY BOX ---")
print("Saamne ek Sone ka dabba (Gold) aur ek Lakdi ka dabba (Wood) rakha hai.")
print("[1] Sone ka dabba kholo\n[2] Lakdi ka dabba kholo\n[3] Apne jeb se Kurkure nikaal kar khao")

c5 = input("Apna jawab chuno: ")
if c5 == "1":
    print("\n❌ TROLL: Sone ka dabba khali tha! Devil ne tumhe chori ke ilzaam mein jail bhej diya! GAME OVER!")
    game_over()
elif c5 == "2":
    print("\n❌ TROLL: Lakdi ka dabba kholte hi usme se ek jahreela saamp nikla aur kat liya! GAME OVER!")
    game_over()
elif c5 == "3":
    print("\n🔥 VIP UNLOCKED: Devil ko bhookh lagi thi! Usne tumse Kurkure chheen liye aur khushi-khushi rasta de diya! Level 6 (FINAL LEVEL)!")
else:
    print("\n❌ Galat input!")
    game_over()

# ----------------- LEVEL 6 (FINAL BOSS) -----------------
print("\n--- LEVEL 6: THE FINAL BOSS (DEVIL) ---")
print("Saamne asli Devil khada hai aur hass raha hai: 'Hahaha! Mujhe hara kar dikhao!'")
print("[1] Devil par talwar se hamla karo\n[2] Devil ke pair chhoo lo (Emotional Damage)\n[3] Devil ko bolo: 'Abey peeche dekh, teri mummy bula rahi hai!'")

c6 = input("Apna jawab chuno: ")
if c6 == "1":
    print("\n❌ TROLL: Devil ne talwar chheen li aur tumhari hi pant kaat di! Tum sharam ke maare bhaag gaye! GAME OVER!")
    game_over()
elif c6 == "2":
    print("\n❌ TROLL: Devil bola: 'No emotional drama in my game!' Aur laat maar ke uda diya! GAME OVER!")
    game_over()
elif c6 == "3":
    print("\n👑 GRAND VICTORY!!! Devil sach mein darr gaya aur peeche mud kar bhaag gaya!")
    print("Tumne LEVEL DEVIL GAME KO POORA JEET LIYA HAI! Tu asli coding champion hai bhai! 🏆🎉")
else:
    print("\n❌ Galat input!")
    game_over()
