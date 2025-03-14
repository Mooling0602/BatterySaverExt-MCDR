from mcdreforged.api.all import *


psi = ServerInterface.psi()

class SendTitle:
    def __init__(self, text: str|RText, target: str):
        self.text = text
        if isinstance(text, RText):
            self.text = text.to_json_str()
        self.target = target
    def main(self):
        psi.execute(f'title {self.target} title {self.text}')
    def sub(self):
        psi.execute(f'title {self.target} subtitle {self.text}')
    def actionbar(self):
        psi.execute(f'title {self.target} actionbar {self.text}')