from pystemd.systemd1 import Unit


class ArkService:
    def __init__(self):
        self.unit = Unit(b"ark.service", _autoload=True)

    def status(self) -> str:
        return self.unit.Unit.ActiveState.decode("utf-8") 

    def start(self):
        self.unit.Unit.Start("replace")

    def stop(self):
        self.unit.Unit.Stop("replace")
