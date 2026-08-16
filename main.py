from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock

class LevelDevilGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10
        self.current_level = 1

        self.title_label = Label(
            text="😈 LEVEL DEVIL - ULTIMATE TROLL GAME 😈",
            font_size='20sp',
            bold=True,
            size_hint_y=0.2
        )
        self.add_widget(self.title_label)

        self.story_label = Label(
            text="",
            font_size='16sp',
            halign='center',
            size_hint_y=0.4
        )
        self.add_widget(self.story_label)

        self.btn1 = Button(text="", size_hint_y=0.13)
        self.btn2 = Button(text="", size_hint_y=0.13)
        self.btn3 = Button(text="", size_hint_y=0.13)

        self.btn1.bind(on_release=lambda x: self.make_choice(1))
        self.btn2.bind(on_release=lambda x: self.make_choice(2))
        self.btn3.bind(on_release=lambda x: self.make_choice(3))

        self.add_widget(self.btn1)
        self.add_widget(self.btn2)
        self.add_widget(self.btn3)

        self.load_level_1()

    def game_over(self, msg):
        self.story_label.text = f"❌ TROLL / GAME OVER!\n{msg}"
        self.btn1.text = "Try Again"
        self.btn2.text = "Try Again"
        self.btn3.text = "Try Again"
        self.current_level = 0

    def make_choice(self, choice):
        if self.current_level == 0:
            self.current_level = 1
            self.load_level_1()
            return

        if self.current_level == 1:
            if choice == 3:
                self.load_level_2()
            elif choice == 1:
                self.game_over("Lal button dabate hi bomb phat gaya!")
            else:
                self.game_over("Neela button dabaya toh screen hang ho gayi!")

        elif self.current_level == 2:
            if choice == 3:
                self.load_level_3()
            elif choice == 1:
                self.game_over("Tezi se bhaage par pul toot gaya!")
            else:
                self.game_over("Chidiya ne potty kar di, tum slip ho gaye!")

        elif self.current_level == 3:
            if choice == 3:
                self.load_level_4()
            elif choice == 1:
                self.game_over("Deewar patthar ki thi, haath toot gaya!")
            else:
                self.game_over("Peeche kaante the, tum gir gaye!")

        elif self.current_level == 4:
            if choice == 3:
                self.load_level_5()
            elif choice == 1:
                self.game_over("Galat math! Robot ne laser se uda diya!")
            else:
                self.game_over("Robot ko hoshiyar log pasand nahi!")

        elif self.current_level == 5:
            if choice == 3:
                self.load_level_6()
            elif choice == 1:
                self.game_over("Sone ka dabba khali tha! Devil ne jail bhej diya!")
            else:
                self.game_over("Lakdi ke dabbe se saamp nikla!")

        elif self.current_level == 6:
            if choice == 3:
                self.story_label.text = "👑 GRAND VICTORY!!!\nDevil darr kar bhaag gaya! Tu champion hai! 🏆"
                self.btn1.text = "Play Again"
                self.btn2.text = "Play Again"
                self.btn3.text = "Play Again"
                self.current_level = 0
            elif choice == 1:
                self.game_over("Devil ne talwar chheen li!")
            else:
                self.game_over("Devil ne laat maar ke uda diya!")

    def load_level_1(self):
        self.current_level = 1
        self.story_label.text = "--- LEVEL 1: THE TWO BUTTONS ---\nSaamne do buttons hain: Lal aur Neela."
        self.btn1.text = "1. Lal button dabao"
        self.btn2.text = "2. Neela button dabao"
        self.btn3.text = "3. Board par laat maaro"

    def load_level_2(self):
        self.current_level = 2
        self.story_label.text = "🔥 VIP UNLOCKED!\n--- LEVEL 2: BROKEN BRIDGE ---\nSaamne toota pul hai."
        self.btn1.text = "1. Bhaag kar paar karo"
        self.btn2.text = "2. Reng kar paar karo"
        self.btn3.text = "3. Aankhein band karke koodo"

    def load_level_3(self):
        self.current_level = 3
        self.story_label.text = "🔥 LEVEL 3: THE GIANT WALL\nDeewar aage aa rahi hai!"
        self.btn1.text = "1. Deewar par mukka maaro"
        self.btn2.text = "2. Peeche bhago"
        self.btn3.text = "3. Secret Magic Move use karo"

    def load_level_4(self):
        self.current_level = 4
        self.story_label.text = "--- LEVEL 4: ROBOT QUIZ ---\nRobot: 2 + 2 * 2 kitna hota hai?"
        self.btn1.text = "1. Answer: 8"
        self.btn2.text = "2. Answer: 6"
        self.btn3.text = "3. Mujhe nahi pata, chal hatt!"

    def load_level_5(self):
        self.current_level = 5
        self.story_label.text = "--- LEVEL 5: MYSTERY BOX ---\nGold box ya Wood box?"
        self.btn1.text = "1. Sone ka dabba kholo"
        self.btn2.text = "2. Lakdi ka dabba kholo"
        self.btn3.text = "3. Kurkure nikaal kar khao"

    def load_level_6(self):
        self.current_level = 6
        self.story_label.text = "--- LEVEL 6: FINAL BOSS (DEVIL) ---\nDevil: Mujhe hara kar dikhao!"
        self.btn1.text = "1. Talwar se hamla karo"
        self.btn2.text = "2. Pair chhoo lo"
        self.btn3.text = "3. Bolo: 'Mummy bula rahi hai!'"

class MainApp(App):
    def build(self):
        return LevelDevilGame()

if __name__ == '__main__':
    MainApp().run()
        
