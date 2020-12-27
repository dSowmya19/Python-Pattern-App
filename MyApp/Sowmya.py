import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.core.clipboard import Clipboard


def show_popup():
    show = P()
    popupWindow = Popup(title = "Error",content = show,size_hint = (None,None),size =(400,400))
    popupWindow.open()



class P(FloatLayout):
    pass

class Code(Screen):
    def copy(self):
        mycode = self.ids.main_label
        Clipboard.copy(mycode.text)
        print("Done")

    def display(self, char):
        try:
            with open("{}.txt".format(char), "r") as f:
                contents = f.read()

            # don't create a new Label, use the one in this Screen
            self.ids.main_label.text = contents

            # switch to this Screen
            self.manager.current = 'code'
        except:
            show_popup()  # if it is an invalid letter like(@,*,&)

        

class SecondPage(Screen):
    # SecondPage asks the user to enter a letter
    letter = ObjectProperty(None)

    def Enter(self):
        # this method checks whether the user entered a valid letter or not
        if len(self.letter.text) == 1:
            char = self.letter.text
            char = char.lower()
            # c = Code()
            c = self.manager.get_screen('code')  # get Code Screen that was created by the `kv`
            c.display(char)  # passing this character display method

        else:
            show_popup()

            

class MainPage(Screen):
    #Main Page has two buttons asking the user whether
    #he want code for special character or a letter
    pass


class WindowManager(ScreenManager):
    pass




class Sowmya(App):
    def build(self):
        return WindowManager()
if __name__ == "__main__":
    Sowmya().run()
