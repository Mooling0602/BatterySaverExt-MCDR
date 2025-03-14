import bat_se.cfg as cfg

from mcdreforged.api.all import *
from mutils import execute_if


@execute_if(lambda: cfg.config is not None and cfg.config['bat_se'].get('enabled', None) is True)
def on_battery_event(server: PluginServerInterface, bi: dict):
    server.logger.info(f"Received battery percent: {bi.get('percent', None)}")