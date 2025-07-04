from abc import ABC, abstractmethod


class Socket(ABC):
    @abstractmethod
    def plugin(self):
        pass

    @abstractmethod
    def unplug(self):
        pass

    def is_plugged(self):
        return self.is_connected


class Samsang(Socket):
    def __init__(self):
        self.is_connected = False

    def plugin(self):
        self._enable330V()

    def unplug(self):
        self._disable330V()

    def _enable330V(self):
        self.is_connected = True
        print("삼상 전기 연결")

    def _disable330V(self):
        self.is_connected = False
        print("삼상 전기 연결 해제")


class Dansang(Socket):
    def __init__(self):
        self.is_connected = False

    def plugin(self):
        self._enable220V()

    def unplug(self):
        self._disable220V()

    def _enable220V(self):
        self.is_connected = True
        print("단상 전기 연결")

    def _disable220V(self):
        self.is_connected = False
        print("단상 전기 연결 해제")


class SunPower(Socket):
    def __init__(self):
        self.is_connected = False

    def plugin(self):
        self._enableSun()

    def unplug(self):
        self._disableSun()

    def _enableSun(self):
        self.is_connected = True
        print("태양광 전기 연결")

    def _disableSun(self):
        self.is_connected = False
        print("태양광 전기 연결 해제")


class DryMachine:
    def __init__(self):
        self.socket: Socket = None

    def connect(self, socket: Socket):
        self.socket = socket
        self.socket.plugin()

    def disconnect(self):
        if self.socket:
            self.socket.unplug()
        else:
            print("연결된 소켓 없음")

    def run(self):
        if not (self.socket and self.socket.is_plugged()):
            raise RuntimeError("소켓이 연결 안됨")
            return
        print("사용중...")
        print("사용 완료")

if __name__ == "__main__":
    dry_machine = DryMachine()

    samsang_socket = Samsang()
    dansang_socket = Dansang()
    sunpower_socket = SunPower()

    dry_machine.connect(samsang_socket)
    dry_machine.run()
    dry_machine.disconnect()

    dry_machine.connect(dansang_socket)
    dry_machine.run()
    dry_machine.disconnect()

    dry_machine.connect(sunpower_socket)
    dry_machine.run()
    dry_machine.disconnect()