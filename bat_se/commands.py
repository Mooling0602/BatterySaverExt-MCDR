import bat_se.notifier as notifier

from mcdreforged.api.all import *


builder = SimpleCommandBuilder()

@builder.command('!!bat_se:test <player>')
def on_notify_test(src: CommandSource, ctx: CommandContext):
    notifier.by_title(ctx['player'])

def register_command(server: PluginServerInterface):
    builder.arg('player', Text)
    builder.register(server)