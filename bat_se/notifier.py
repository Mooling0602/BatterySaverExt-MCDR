from mcdreforged.api.all import *
from .utils import SendTitle


psi = ServerInterface.psi()

def by_title(player: str):
    SendTitle(RText('test', RColor.blue), player).main()