"""
Synology Core External Device API wrapper.

Provides a Python interface for managing external devices on Synology NAS,
including Bluetooth, printers, and storage expansion units.
"""

from __future__ import annotations
from typing import Optional
from . import base_api


class CoreExternalDevice(base_api.BaseApi):
    """
    Core External Device API implementation for Synology NAS.

    Covers Bluetooth, printer (driver, network, USB, OAuth), and storage
    (expansion unit, settings) endpoints not handled by other modules.
    """

    # ------------------------------------------------------------------ #
    #  Bluetooth                                                          #
    # ------------------------------------------------------------------ #

    def bluetooth_get(self) -> dict[str, object] | str:
        """Get Bluetooth adapter status."""
        api_name = 'SYNO.Core.ExternalDevice.Bluetooth'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def bluetooth_set(self, enable: bool = True) -> dict[str, object] | str:
        """Enable or disable the Bluetooth adapter."""
        api_name = 'SYNO.Core.ExternalDevice.Bluetooth'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set',
                     'enable': str(enable).lower()}

        return self.request_data(api_name, api_path, req_param)

    def bluetooth_device_list(self) -> dict[str, object] | str:
        """List discovered Bluetooth devices."""
        api_name = 'SYNO.Core.ExternalDevice.Bluetooth.Device'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def bluetooth_device_get(self, device_id: str) -> dict[str, object] | str:
        """Get information for a specific Bluetooth device."""
        api_name = 'SYNO.Core.ExternalDevice.Bluetooth.Device'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get',
                     'id': device_id}

        return self.request_data(api_name, api_path, req_param)

    def bluetooth_device_connect(self, device_id: str) -> dict[str, object] | str:
        """Connect to a Bluetooth device."""
        api_name = 'SYNO.Core.ExternalDevice.Bluetooth.Device'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'connect',
                     'id': device_id}

        return self.request_data(api_name, api_path, req_param)

    def bluetooth_device_disconnect(self, device_id: str) -> dict[str, object] | str:
        """Disconnect a Bluetooth device."""
        api_name = 'SYNO.Core.ExternalDevice.Bluetooth.Device'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'disconnect',
                     'id': device_id}

        return self.request_data(api_name, api_path, req_param)

    def bluetooth_settings_get(self) -> dict[str, object] | str:
        """Get Bluetooth settings."""
        api_name = 'SYNO.Core.ExternalDevice.Bluetooth.Settings'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def bluetooth_settings_set(self, discoverable: Optional[bool] = None,
                               name: Optional[str] = None) -> dict[str, object] | str:
        """Set Bluetooth settings."""
        api_name = 'SYNO.Core.ExternalDevice.Bluetooth.Settings'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param: dict[str, object] = {
            'version': info['maxVersion'], 'method': 'set'}
        if discoverable is not None:
            req_param['discoverable'] = str(discoverable).lower()
        if name is not None:
            req_param['name'] = name

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  Default Permission                                                 #
    # ------------------------------------------------------------------ #

    def default_permission_get(self) -> dict[str, object] | str:
        """Get default permission settings for external devices."""
        api_name = 'SYNO.Core.ExternalDevice.DefaultPermission'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def default_permission_set(self, permission: str) -> dict[str, object] | str:
        """Set default permission for external devices."""
        api_name = 'SYNO.Core.ExternalDevice.DefaultPermission'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set',
                     'permission': permission}

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  Printer                                                            #
    # ------------------------------------------------------------------ #

    def printer_list(self) -> dict[str, object] | str:
        """List all printers."""
        api_name = 'SYNO.Core.ExternalDevice.Printer'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def printer_get(self, printer_id: str) -> dict[str, object] | str:
        """Get printer information."""
        api_name = 'SYNO.Core.ExternalDevice.Printer'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get',
                     'id': printer_id}

        return self.request_data(api_name, api_path, req_param)

    def printer_clean(self, printer_id: str) -> dict[str, object] | str:
        """Clean the print queue for a printer."""
        api_name = 'SYNO.Core.ExternalDevice.Printer'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'clean',
                     'id': printer_id}

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  Printer Driver                                                     #
    # ------------------------------------------------------------------ #

    def printer_driver_list(self) -> dict[str, object] | str:
        """List available printer drivers."""
        api_name = 'SYNO.Core.ExternalDevice.Printer.Driver'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def printer_driver_get(self, driver_id: str) -> dict[str, object] | str:
        """Get a specific printer driver."""
        api_name = 'SYNO.Core.ExternalDevice.Printer.Driver'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get',
                     'id': driver_id}

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  Printer Network                                                    #
    # ------------------------------------------------------------------ #

    def printer_network_list(self) -> dict[str, object] | str:
        """List network printers."""
        api_name = 'SYNO.Core.ExternalDevice.Printer.Network'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def printer_network_create(self, host: str, port: int = 9100,
                               driver_id: Optional[str] = None) -> dict[str, object] | str:
        """Add a network printer."""
        api_name = 'SYNO.Core.ExternalDevice.Printer.Network'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param: dict[str, object] = {
            'version': info['maxVersion'], 'method': 'create',
            'host': host, 'port': port}
        if driver_id is not None:
            req_param['driver_id'] = driver_id

        return self.request_data(api_name, api_path, req_param)

    def printer_network_delete(self, printer_id: str) -> dict[str, object] | str:
        """Remove a network printer."""
        api_name = 'SYNO.Core.ExternalDevice.Printer.Network'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'delete',
                     'id': printer_id}

        return self.request_data(api_name, api_path, req_param)

    def printer_network_host_list(self) -> dict[str, object] | str:
        """List network printer hosts discovered on the network."""
        api_name = 'SYNO.Core.ExternalDevice.Printer.Network.Host'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  Printer OAuth                                                      #
    # ------------------------------------------------------------------ #

    def printer_oauth_get(self) -> dict[str, object] | str:
        """Get OAuth settings for cloud printing."""
        api_name = 'SYNO.Core.ExternalDevice.Printer.OAuth'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def printer_oauth_set(self, token: str) -> dict[str, object] | str:
        """Set OAuth token for cloud printing."""
        api_name = 'SYNO.Core.ExternalDevice.Printer.OAuth'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set',
                     'token': token}

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  Printer USB                                                        #
    # ------------------------------------------------------------------ #

    def printer_usb_list(self) -> dict[str, object] | str:
        """List USB printers."""
        api_name = 'SYNO.Core.ExternalDevice.Printer.USB'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def printer_usb_get(self, printer_id: str) -> dict[str, object] | str:
        """Get USB printer information."""
        api_name = 'SYNO.Core.ExternalDevice.Printer.USB'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get',
                     'id': printer_id}

        return self.request_data(api_name, api_path, req_param)

    def printer_usb_release(self, printer_id: str) -> dict[str, object] | str:
        """Release a USB printer from the server."""
        api_name = 'SYNO.Core.ExternalDevice.Printer.USB'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'release',
                     'id': printer_id}

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  Storage — Expansion Unit                                           #
    # ------------------------------------------------------------------ #

    def storage_eunit_list(self) -> dict[str, object] | str:
        """List connected expansion units."""
        api_name = 'SYNO.Core.ExternalDevice.Storage.EUnit'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def storage_eunit_get(self, unit_id: str) -> dict[str, object] | str:
        """Get expansion unit details."""
        api_name = 'SYNO.Core.ExternalDevice.Storage.EUnit'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get',
                     'id': unit_id}

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  Storage — Setting                                                  #
    # ------------------------------------------------------------------ #

    def storage_setting_get(self) -> dict[str, object] | str:
        """Get external storage settings."""
        api_name = 'SYNO.Core.ExternalDevice.Storage.Setting'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def storage_setting_set(self,
                            auto_format: Optional[bool] = None,
                            auto_mount: Optional[bool] = None) -> dict[str, object] | str:
        """Set external storage settings."""
        api_name = 'SYNO.Core.ExternalDevice.Storage.Setting'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param: dict[str, object] = {
            'version': info['maxVersion'], 'method': 'set'}
        if auto_format is not None:
            req_param['auto_format'] = str(auto_format).lower()
        if auto_mount is not None:
            req_param['auto_mount'] = str(auto_mount).lower()

        return self.request_data(api_name, api_path, req_param)
