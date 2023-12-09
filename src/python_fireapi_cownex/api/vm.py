import requests

from src.python_fireapi_cownex import exception, constants, utils
from src.python_fireapi_cownex.api.base import FireAPI


class VM(FireAPI):
    """Class for interacting with the VM Endpoints"""

    def list_all_vms(self):
        """List all VMs"""
        return self.request("vm/list", "GET")

    def list_all_host_systems(self):
        """List all available Hostsystems"""
        return self.request("vm/list/hosts", "GET")

    def list_all_os(self):
        """List all available Operating Systems"""
        return self.request("vm/list/os", "GET")

    def list_all_iso(self):
        """List all avaible ISO"""
        return self.request("vm/list/iso", "GET")

    def create_vm(self, cores:int, mem:int, disk:int, os, hostsystem, ips=None, backup_slots=None, network_speed=None):
        """
        Create a VM
        :param cores: Number of CPU cores
        :param mem: Memory in MB
        :param disk: Disk in GB
        :param os: OS (vm/list/os)
        :param hostsystem: Hostsystem (/vm/list/hosts)
        :param ips: Number of IPv4
        :param backup_slots: Number of Backup Slots (Default/Min: 2)
        :param network_speed: Networkspeed in Mbit/s (Default/Min: 1000)
        """
        data = {
            "cores": cores,
            "mem": mem,
            "disk": disk,
            "os": os,
            "hostsystem": hostsystem
        }
        utils.update_json(data, "ips", ips)
        utils.update_json(data, "backup_slots", backup_slots)
        utils.update_json(data, "network_speed", network_speed)
        return self.request("vm/create", "POST", data)



    def change_vm_config(self, vmid:int, cores=None, mem=None, disk=None, backup_slots=None, network_speed=None):
        """
        Change given VM Config
        :param vmid: ID of the VM
        :param cores: Number of CPU cores
        :param mem: Memory in MB
        :param disk: Disk in GB
        :param backup_slots: Number of Backup Slots (Default/Min: 2)
        :param network_speed: Networkspeed in Mbit/s (Default/Min: 1000)
        """
        if not vmid:
            raise exception.ParameterNotGivenException
        if not utils.is_not_all_none(cores, mem, disk, backup_slots, network_speed):
            raise exception.OneOptionalParameterRequiredException
        data = {}
        utils.update_json(data, "cores", cores)
        utils.update_json(data, "mem", mem)
        utils.update_json(data, "disk", disk)
        utils.update_json(data, "backup_slots", backup_slots)
        utils.update_json(data, "network_speed", network_speed)
        return self.request(f"vm/{vmid}/change", "POST", data)

    def reinstall_os(self, vmid, os=None):
        """
        Reinstall/Change the Operation-System of the VM.
        :param vmid: ID of the VM
        :param os: Operation-System (if None, just reinstall the current OS)
        """
        if not vmid:
            raise exception.ParameterNotGivenException
        data = {"vmid": vmid}
        if os:
            data['os'] = os
        return self.request(f"vm/{vmid}/reinstall", "POST", data)

    def get_config(self, vmid:int):
        """
        Get VM-Config
        :param vmid: ID of the VM
        :return:
        """
        if not vmid:
            raise exception.ParameterNotGivenException
        return self.request(f"vm/{vmid}/config", "GET")

    def change_rdns(self, vmid:int, domain, ip_address=None):
        """
        Change the RDNS Entry for the Given IPv4.
        :param vmid: ID of the VM
        :param domain: Domain for the RDNS
        :param ip_address: IP to change RDNS (if none rnds will be for all IPS)
        """
        if not vmid:
            raise exception.ParameterNotGivenException
        data = {"domain": domain}
        utils.update_json(data, "ip_address", ip_address)
        return self.request(f"vm/{vmid}/rdns", "POST", data)

    def get_novnc(self, vmid:int):
        """
        Get NoVNC Link
        :param vmid: ID of the VM
        """
        if not vmid:
            raise exception.ParameterNotGivenException
        return self.request(f"vm/{vmid}/novnc", "POST")

    def delete_vm(self, vmid:int):
        """
        Deletes the given VM
        :param vmid: ID of the VM
        """
        if not vmid:
            raise exception.ParameterNotGivenException
        return self.request(f"vm/{vmid}/delete", "DELETE")

    def get_vm_status(self, vmid:int):
        """
        Get Status of the VM
        :param vmid: ID of the VM
        """
        if not vmid:
            raise exception.ParameterNotGivenException
        return self.request(f"vm/{vmid}/status", "GET")

    def get_vm_installation_status(self, vmid:int):
        """
        Get VM Installation Status
        :param vmid: ID of the VM
        """
        if not vmid:
            raise exception.ParameterNotGivenException
        return self.request(f"vm/{vmid}/status/installation", "GET")

    def password_reset(self, vmid: int):
        """
        Reset Password of given VM
        :param vmid: ID of the VM
        """
        if not vmid:
            raise exception.ParameterNotGivenException
        return self.request(f"vm/{vmid}/password-reset", "POST")

    def power_action(self, vmid: int, action):
        """
        Reset Password of given VM
        :param vmid: ID of the VM
        :param action: possible actions: start, stop, restart
        """
        if not vmid or not action:
            raise exception.ParameterNotGivenException
        if not action in constants.POWER_STATES:
            raise exception.InvalidActionException
        return self.request(f"vm/{vmid}/power", "POST", {"action": action})

    def get_ddos_settings(self, vmid:int):
        """
        Get DDoS Settings
        :param vmid: ID of the VM
        """
        if not vmid:
            raise exception.ParameterNotGivenException
        return self.request(f"vm/{vmid}/ddos", "GET")

    def change_ddos_settings(self, vmid:int, ip_address, layer4=None, layer7=None):
        """
        Change the DDoS Settings of the given VM
        :param vmid: ID of the VM
        :param ip_address:
        :param layer4: possible options: permanent, dynamic
        :param layer7: possible options: on/off
        """
        if not utils.is_not_all_none(layer4, layer7):
            raise exception.OneOptionalParameterRequiredException
        data = {"ip_address": ip_address}
        utils.update_json(data, "layer4", layer4)
        utils.update_json(data, "layer7", layer7)
        return self.request(f"vm/{vmid}/ddos", "POST", data)

    def put_iso(self, vmid:int, iso):
        """
        Put ISO in given VM
        :param vmid: ID of the VM
        :param iso: ISO (/vm/list/iso)
        """
        if not vmid or iso:
            raise exception.ParameterNotGivenException
        data = {"iso": iso}
        return self.request(f"vm/{vmid}/iso", "PUT", data)

    def remove_iso(self, vmid:int):
        """
        Removes ISO from given VM
        :param vmid: transkribieren
        """
        return self.request(f"vm/{vmid}/iso", "DELETE")

    # todo bakckups

