from youqu3.cmd import Cmd
from youqu3 import log

@log
class KernelMethod(Cmd):

    @classmethod
    def get_systemd_modules_load_service_status(cls):
        """sudo systemctl status systemd-modules-load.service"""
        stdout, exitcode = cls.sudo_run(
            "systemctl status systemd-modules-load.service",
            return_code=True
        )
        return exitcode

    @classmethod
    def get_journalctl_u(cls, service_name):
        """sudo journalctl -u {{service_name}}"""
        stdout = cls.sudo_run(f"journalctl -u {service_name}.service")
        return stdout

    @classmethod
    def get_journalctl_k(cls, egrep=None):
        """sudo journalctl -k"""
        if egrep is None:
            stdout = cls.sudo_run("journalctl -k")
        else:
            stdout = cls.sudo_run(f'journalctl -k | egrep -i "{egrep}"')
        return stdout

    @classmethod
    def get_journalctl_b(cls, index=0, egrep=None):
        """sudo journalctl -b"""
        if egrep is None:
            stdout = cls.sudo_run("journalctl -b")
        else:
            stdout = cls.sudo_run(f'journalctl -b {index} | egrep -i "{egrep}"')
        return stdout

    @classmethod
    def get_modinfo_parport_serial(cls, grep=None):
        """modinfo parport_seria"""
        if grep is None:
            stdout = cls.run("modinfo parport_serial")
        else:
            stdout = cls.run(f'modinfo parport_serial | grep {grep}')
        return stdout

    @classmethod
    def uname_r(cls):
        """uname -r"""
        return cls.run("uname -r")

    @classmethod
    def cat(cls, filepath):
        """cat {{filepath}}"""
        return cls.run(f"cat {filepath}")