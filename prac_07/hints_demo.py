from kivy.app import App
from kivy.lang import Builder


class HintsDemo(App):
    def build(self):
        self.title = "  Reading Track 2.0"
        self.root = Builder.load_file('hints_demo.kv')
        return self.root 

    def build_config(self, config):
        self. title = 'Develop'
        return self.root


# create and start the App running
HintsDemo().run()
