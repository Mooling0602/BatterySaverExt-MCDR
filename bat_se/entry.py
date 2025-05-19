import os
import bat_se.cfg as cfg
import bat_se.subscription as data

from mcdreforged.api.all import *
from mutils import tr, extract_file
from .listener import on_battery_event
from .commands import register_command


def on_load(server: PluginServerInterface, prev_module):
    config_path = os.path.join(server.get_data_folder(), 'config.yml')
    if not os.path.exists(config_path):
        extract_file(server, os.path.join('resources', 'config.default.yml'), config_path)
    cfg.config = server.load_config_simple(
        file_name='config.yml',
        default_config={
            'bat_se': {
                'enabled': True,
                'notify': {
                    'when_lower_than': 35,
                    'interval': 1
                }
            }
        },
        echo_in_console=False
    )
    server.register_event_listener('battery_saver:battery_info', on_battery_event)
    register_command(server)
    server.logger.info(tr(server, "on_load"))

def on_player_left(server: PluginServerInterface, player: str):
    if player in data.players:
        data.players.remove(player)