import bat_se.subscription as data

from mcdreforged.api.all import *
from mutils import tr


builder = SimpleCommandBuilder()
psi = ServerInterface.psi()

@builder.command('!!batse show')
def on_subscribe_notification(src: CommandSource, ctx: CommandContext):
    if src.is_player:
        data.players.append(src.player)
    else:
        src.reply(tr(psi, "command.not_player"))

@builder.command('!!batse hide')
def on_cancel_subscription(src: CommandSource, ctx: CommandContext):
    if src.is_player:
        data.players.remove(src.player)
    else:
        src.reply(tr(psi, "command.not_player"))

def register_command(server: PluginServerInterface):
    builder.arg('player', Text)
    builder.register(server)