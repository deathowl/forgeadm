import dbus


class ForgeService:
    def __init__(self):
        self.sysbus = dbus.SystemBus()
        self.systemd1 = self.sysbus.get_object('org.freedesktop.systemd1', '/org/freedesktop/systemd1')
        self.manager = dbus.Interface(self.systemd1, 'org.freedesktop.systemd1.Manager')
        self.service = self.sysbus.get_object('org.freedesktop.systemd1', object_path=self.manager.GetUnit('minecraft.service'))
        self.interface = dbus.Interface(self.service, dbus_interface='org.freedesktop.DBus.Properties')

    def status(self) -> str:
        return self.interface.Get('org.freedesktop.systemd1.Unit', 'ActiveState')

    def start(self):
        self.manager.StartUnit('minecraft.service', 'fail')

    def stop(self):
        self.manager.StopUnit('minecraft.service', 'fail')
