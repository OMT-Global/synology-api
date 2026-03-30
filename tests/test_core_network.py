"""Unit tests for core_network — verifies all API namespaces are covered."""

import inspect
import unittest
from unittest.mock import MagicMock, patch

from synology_api.core_network import CoreNetwork


def _make_instance():
    """Create a CoreNetwork instance with mocked auth/session."""
    with patch('synology_api.core_network.base_api.BaseApi.__init__', return_value=None):
        instance = CoreNetwork.__new__(CoreNetwork)

    api_list = {
        'SYNO.Core.Network.Authentication': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Network.Authentication.Cert': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Network.Ethernet.External': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Network.IPv6': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Network.IPv6.Router': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Network.IPv6.Router.Prefix': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Network.MACClone': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Network.OVS': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Network.PPPoE.Relay': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Network.Router.Static.Route': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Network.TrafficControl.RouterRules': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Network.TrafficControl.Rules': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Network.UPnPServer': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Network.VPN': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Network.VPN.OpenVPN.CA': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Network.VPN.OpenVPNWithConf': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Network.VPN.OpenVPNWithConf.Certs': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Network.WOL': {'path': 'entry.cgi', 'maxVersion': 1},
    }
    instance.core_list = api_list
    instance.request_data = MagicMock(return_value={'success': True, 'data': {}})
    return instance


class TestCoreNetwork(unittest.TestCase):
    """Tests for CoreNetwork methods."""

    def setUp(self):
        self.instance = _make_instance()

    def test_ethernet_external_get(self):
        self.instance.ethernet_external_get()
        self.instance.request_data.assert_called_once()

    def test_ethernet_external_set(self):
        self.instance.ethernet_external_set(ifname='test', enable='test')
        self.instance.request_data.assert_called_once()

    def test_ipv6_get(self):
        self.instance.ipv6_get()
        self.instance.request_data.assert_called_once()

    def test_ipv6_router_get(self):
        self.instance.ipv6_router_get()
        self.instance.request_data.assert_called_once()

    def test_ipv6_router_prefix_get(self):
        self.instance.ipv6_router_prefix_get()
        self.instance.request_data.assert_called_once()

    def test_ipv6_router_prefix_set(self):
        self.instance.ipv6_router_prefix_set(prefix='test', prefix_length='test', enable_auto='test')
        self.instance.request_data.assert_called_once()

    def test_ipv6_router_set(self):
        self.instance.ipv6_router_set(enable='test', mode='test')
        self.instance.request_data.assert_called_once()

    def test_ipv6_set(self):
        self.instance.ipv6_set(enable='test', type='test')
        self.instance.request_data.assert_called_once()

    def test_mac_clone_get(self):
        self.instance.mac_clone_get()
        self.instance.request_data.assert_called_once()

    def test_mac_clone_set(self):
        self.instance.mac_clone_set(ifname='test', mac='test', enable='test')
        self.instance.request_data.assert_called_once()

    def test_network_auth_cert_delete(self):
        self.instance.network_auth_cert_delete()
        self.instance.request_data.assert_called_once()

    def test_network_auth_cert_get(self):
        self.instance.network_auth_cert_get()
        self.instance.request_data.assert_called_once()

    def test_network_auth_cert_set(self):
        self.instance.network_auth_cert_set(cert_path='test', key_path='test', ca_path='test')
        self.instance.request_data.assert_called_once()

    def test_network_auth_get(self):
        self.instance.network_auth_get()
        self.instance.request_data.assert_called_once()

    def test_network_auth_set(self):
        self.instance.network_auth_set(enable='test', profile={"test": True})
        self.instance.request_data.assert_called_once()

    def test_ovs_get(self):
        self.instance.ovs_get()
        self.instance.request_data.assert_called_once()

    def test_ovs_set(self):
        self.instance.ovs_set(enable='test')
        self.instance.request_data.assert_called_once()

    def test_pppoe_relay_get(self):
        self.instance.pppoe_relay_get()
        self.instance.request_data.assert_called_once()

    def test_pppoe_relay_set(self):
        self.instance.pppoe_relay_set(enable='test', server_ifname='test', client_ifname='test')
        self.instance.request_data.assert_called_once()

    def test_static_route_create(self):
        self.instance.static_route_create(dest='test', gateway='test', ifname='test', mask='test', metric='test')
        self.instance.request_data.assert_called_once()

    def test_static_route_delete(self):
        self.instance.static_route_delete(route_id='test')
        self.instance.request_data.assert_called_once()

    def test_static_route_get(self):
        self.instance.static_route_get(route_id='test')
        self.instance.request_data.assert_called_once()

    def test_static_route_list(self):
        self.instance.static_route_list()
        self.instance.request_data.assert_called_once()

    def test_traffic_control_router_rules_get(self):
        self.instance.traffic_control_router_rules_get()
        self.instance.request_data.assert_called_once()

    def test_traffic_control_router_rules_list(self):
        self.instance.traffic_control_router_rules_list()
        self.instance.request_data.assert_called_once()

    def test_traffic_control_router_rules_set(self):
        self.instance.traffic_control_router_rules_set(rules={"test": True})
        self.instance.request_data.assert_called_once()

    def test_traffic_control_rules_create(self):
        self.instance.traffic_control_rules_create(protocol='test', port=1, upload_limit='test', download_limit='test', enabled=True)
        self.instance.request_data.assert_called_once()

    def test_traffic_control_rules_delete(self):
        self.instance.traffic_control_rules_delete(rule_id='test')
        self.instance.request_data.assert_called_once()

    def test_traffic_control_rules_get(self):
        self.instance.traffic_control_rules_get()
        self.instance.request_data.assert_called_once()

    def test_traffic_control_rules_list(self):
        self.instance.traffic_control_rules_list()
        self.instance.request_data.assert_called_once()

    def test_upnp_server_get(self):
        self.instance.upnp_server_get()
        self.instance.request_data.assert_called_once()

    def test_upnp_server_set(self):
        self.instance.upnp_server_set(enable='test')
        self.instance.request_data.assert_called_once()

    def test_vpn_get(self):
        self.instance.vpn_get()
        self.instance.request_data.assert_called_once()

    def test_vpn_openvpn_ca_get(self):
        self.instance.vpn_openvpn_ca_get()
        self.instance.request_data.assert_called_once()

    def test_vpn_openvpn_ca_set(self):
        self.instance.vpn_openvpn_ca_set(ca_path='test')
        self.instance.request_data.assert_called_once()

    def test_vpn_openvpn_with_conf_certs_get(self):
        self.instance.vpn_openvpn_with_conf_certs_get()
        self.instance.request_data.assert_called_once()

    def test_vpn_openvpn_with_conf_certs_set(self):
        self.instance.vpn_openvpn_with_conf_certs_set(cert_path='test', key_path='test', ca_path='test')
        self.instance.request_data.assert_called_once()

    def test_vpn_openvpn_with_conf_get(self):
        self.instance.vpn_openvpn_with_conf_get()
        self.instance.request_data.assert_called_once()

    def test_vpn_openvpn_with_conf_set(self):
        self.instance.vpn_openvpn_with_conf_set(conf_path='test', username='test', password='test')
        self.instance.request_data.assert_called_once()

    def test_vpn_set(self):
        self.instance.vpn_set(reconnect='test', interval='test')
        self.instance.request_data.assert_called_once()

    def test_wol_get(self):
        self.instance.wol_get()
        self.instance.request_data.assert_called_once()

    def test_wol_set(self):
        self.instance.wol_set(enable='test')
        self.instance.request_data.assert_called_once()

    def test_wol_wake(self):
        self.instance.wol_wake(mac='test', ifname='test')
        self.instance.request_data.assert_called_once()


class TestCoreNetworkCoverage(unittest.TestCase):
    """Meta-tests for API namespace coverage."""

    def test_all_namespaces_covered(self):
        """Every API namespace must be referenced in at least one method."""
        source = inspect.getsource(CoreNetwork)
        required = {
        'SYNO.Core.Network.Authentication',
        'SYNO.Core.Network.Authentication.Cert',
        'SYNO.Core.Network.Ethernet.External',
        'SYNO.Core.Network.IPv6',
        'SYNO.Core.Network.IPv6.Router',
        'SYNO.Core.Network.IPv6.Router.Prefix',
        'SYNO.Core.Network.MACClone',
        'SYNO.Core.Network.OVS',
        'SYNO.Core.Network.PPPoE.Relay',
        'SYNO.Core.Network.Router.Static.Route',
        'SYNO.Core.Network.TrafficControl.RouterRules',
        'SYNO.Core.Network.TrafficControl.Rules',
        'SYNO.Core.Network.UPnPServer',
        'SYNO.Core.Network.VPN',
        'SYNO.Core.Network.VPN.OpenVPN.CA',
        'SYNO.Core.Network.VPN.OpenVPNWithConf',
        'SYNO.Core.Network.VPN.OpenVPNWithConf.Certs',
        'SYNO.Core.Network.WOL'
    }
        for ns in required:
            with self.subTest(namespace=ns):
                self.assertIn(f"'{ns}'", source)

    def test_method_count(self):
        """Verify expected number of public methods."""
        public = [m for m in dir(CoreNetwork)
                  if not m.startswith('_') and callable(getattr(CoreNetwork, m))
                  and m != 'logout']
        self.assertGreaterEqual(len(public), 43,
                                f"Expected 43+ methods, found {len(public)}")


if __name__ == '__main__':
    unittest.main()
