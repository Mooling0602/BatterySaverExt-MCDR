import bat_se.cfg as cfg
import bat_se.subscription as data

from mcdreforged.api.all import *
from mutils import execute_if, tr
from .utils import SendTitle


psi = ServerInterface.psi()

@execute_if(lambda: cfg.config is not None and cfg.config['bat_se'].get('enabled', None) is True)
def on_battery_event(server: PluginServerInterface, bi: dict):
    percent = bi.get('percent', None)
    lev_s = bi.get('level_shift', None)
    # is_c = bi.get('is_charging', None)
    tasks(bi)
    if percent is not None:
        percent = int(percent)
    if lev_s == "down" and percent < cfg.config['bat_se'].get('notify', None).get('when_lower_than', None):
        on_battery_low(server, percent)
    
def tasks(info: dict):
    status = None
    if info.get('is_charging', None) is True:
        status = tr(psi, "power_status.charging")
    if info.get('is_charging', None) is False:
        status = tr(psi, "power_status.battery")
    text = psi.rtr(f"{psi.get_self_metadata().id}.battery_info", percent=info.get('percent', None), status=status)
    rtext = RText(str(text), RColor.red)
    if int(info.get('percent', None)) > int(cfg.config['bat_se'].get('notify', None).get('when_lower_than', None)):
        rtext = RText(str(text), RColor.green)
    for i in data.players:
        message = SendTitle(rtext, i)
        message.actionbar()

@execute_if(lambda: psi.is_server_running() is True)        
def on_battery_low(server: PluginServerInterface, percent: int):
    text = server.rtr(f"{server.get_self_metadata().id}.low_battery_message", percent=percent)
    rtext = RText(text, RColor.red)
    message = SendTitle(rtext, "@a")
    message.actionbar()
    if not hasattr(on_battery_low, 'last_percent') or on_battery_low.last_percent != percent:
        message.main()
        on_battery_low.last_percent = percent