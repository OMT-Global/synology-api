"""Unit tests for core_security — verifies all API namespaces are covered."""

import inspect
import unittest
from unittest.mock import MagicMock, patch

from synology_api.core_security import CoreSecurity


def _make_instance():
    """Create a CoreSecurity instance with mocked auth/session."""
    with patch('synology_api.core_security.base_api.BaseApi.__init__', return_value=None):
        instance = CoreSecurity.__new__(CoreSecurity)

    api_list = {
        'SYNO.Core.DisableAdmin': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.OTP': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.OTP.Admin': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.OTP.EnforcePolicy': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.OTP.Ex': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.OTP.Mail': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Security.AutoBlock.Rules': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Security.DSM': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Security.DSM.Embed': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Security.DSM.Proxy': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Security.DoS': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Security.Firewall': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Security.Firewall.Adapter': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Security.Firewall.Conf': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Security.Firewall.Geoip': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Security.Firewall.Profile.Apply': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Security.Firewall.Rules': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Security.Firewall.Rules.Serv': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.SmartBlock': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.SmartBlock.Device': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.SmartBlock.Trusted': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.SmartBlock.Untrusted': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.SmartBlock.User': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.TrustDevice': {'path': 'entry.cgi', 'maxVersion': 1},
    }
    instance.gen_list = api_list
    instance.request_data = MagicMock(return_value={'success': True, 'data': {}})
    return instance


class TestCoreSecurity(unittest.TestCase):
    """Tests for CoreSecurity methods."""

    def setUp(self):
        self.instance = _make_instance()

    def test_autoblock_rules_delete(self):
        self.instance.autoblock_rules_delete(rules={"test": True})
        self.instance.request_data.assert_called_once()

    def test_autoblock_rules_get(self):
        self.instance.autoblock_rules_get()
        self.instance.request_data.assert_called_once()

    def test_autoblock_rules_list(self):
        self.instance.autoblock_rules_list()
        self.instance.request_data.assert_called_once()

    def test_autoblock_rules_set(self):
        self.instance.autoblock_rules_set(rules={"test": True})
        self.instance.request_data.assert_called_once()

    def test_disable_admin_get(self):
        self.instance.disable_admin_get()
        self.instance.request_data.assert_called_once()

    def test_disable_admin_set(self):
        self.instance.disable_admin_set()
        self.instance.request_data.assert_called_once()

    def test_firewall_adapter_get(self):
        self.instance.firewall_adapter_get()
        self.instance.request_data.assert_called_once()

    def test_firewall_adapter_list(self):
        self.instance.firewall_adapter_list()
        self.instance.request_data.assert_called_once()

    def test_firewall_conf_get(self):
        self.instance.firewall_conf_get()
        self.instance.request_data.assert_called_once()

    def test_firewall_conf_set(self):
        self.instance.firewall_conf_set()
        self.instance.request_data.assert_called_once()

    def test_firewall_geoip_get(self):
        self.instance.firewall_geoip_get()
        self.instance.request_data.assert_called_once()

    def test_firewall_geoip_set(self):
        self.instance.firewall_geoip_set()
        self.instance.request_data.assert_called_once()

    def test_firewall_get(self):
        self.instance.firewall_get()
        self.instance.request_data.assert_called_once()

    def test_firewall_profile_apply(self):
        self.instance.firewall_profile_apply(profile_name='test')
        self.instance.request_data.assert_called_once()

    def test_firewall_profile_apply_status(self):
        self.instance.firewall_profile_apply_status()
        self.instance.request_data.assert_called_once()

    def test_firewall_rules_delete(self):
        self.instance.firewall_rules_delete(rules={"test": True})
        self.instance.request_data.assert_called_once()

    def test_firewall_rules_get(self):
        self.instance.firewall_rules_get()
        self.instance.request_data.assert_called_once()

    def test_firewall_rules_list(self):
        self.instance.firewall_rules_list()
        self.instance.request_data.assert_called_once()

    def test_firewall_rules_serv_get(self):
        self.instance.firewall_rules_serv_get()
        self.instance.request_data.assert_called_once()

    def test_firewall_rules_serv_list(self):
        self.instance.firewall_rules_serv_list()
        self.instance.request_data.assert_called_once()

    def test_firewall_rules_set(self):
        self.instance.firewall_rules_set(rules={"test": True})
        self.instance.request_data.assert_called_once()

    def test_firewall_set(self):
        self.instance.firewall_set()
        self.instance.request_data.assert_called_once()

    def test_otp_admin_get(self):
        self.instance.otp_admin_get()
        self.instance.request_data.assert_called_once()

    def test_otp_admin_set(self):
        self.instance.otp_admin_set()
        self.instance.request_data.assert_called_once()

    def test_otp_enforce_policy_get(self):
        self.instance.otp_enforce_policy_get()
        self.instance.request_data.assert_called_once()

    def test_otp_enforce_policy_set(self):
        self.instance.otp_enforce_policy_set()
        self.instance.request_data.assert_called_once()

    def test_otp_ex_get(self):
        self.instance.otp_ex_get()
        self.instance.request_data.assert_called_once()

    def test_otp_ex_set(self):
        self.instance.otp_ex_set()
        self.instance.request_data.assert_called_once()

    def test_otp_get(self):
        self.instance.otp_get()
        self.instance.request_data.assert_called_once()

    def test_otp_mail_get(self):
        self.instance.otp_mail_get()
        self.instance.request_data.assert_called_once()

    def test_otp_mail_set(self):
        self.instance.otp_mail_set()
        self.instance.request_data.assert_called_once()

    def test_otp_set(self):
        self.instance.otp_set()
        self.instance.request_data.assert_called_once()

    def test_security_dos_get(self):
        self.instance.security_dos_get()
        self.instance.request_data.assert_called_once()

    def test_security_dos_set(self):
        self.instance.security_dos_set()
        self.instance.request_data.assert_called_once()

    def test_security_dsm_embed_get(self):
        self.instance.security_dsm_embed_get()
        self.instance.request_data.assert_called_once()

    def test_security_dsm_embed_set(self):
        self.instance.security_dsm_embed_set()
        self.instance.request_data.assert_called_once()

    def test_security_dsm_get(self):
        self.instance.security_dsm_get()
        self.instance.request_data.assert_called_once()

    def test_security_dsm_proxy_get(self):
        self.instance.security_dsm_proxy_get()
        self.instance.request_data.assert_called_once()

    def test_security_dsm_proxy_set(self):
        self.instance.security_dsm_proxy_set()
        self.instance.request_data.assert_called_once()

    def test_security_dsm_set(self):
        self.instance.security_dsm_set()
        self.instance.request_data.assert_called_once()

    def test_smartblock_device_delete(self):
        self.instance.smartblock_device_delete(devices='test')
        self.instance.request_data.assert_called_once()

    def test_smartblock_device_get(self):
        self.instance.smartblock_device_get()
        self.instance.request_data.assert_called_once()

    def test_smartblock_device_list(self):
        self.instance.smartblock_device_list()
        self.instance.request_data.assert_called_once()

    def test_smartblock_get(self):
        self.instance.smartblock_get()
        self.instance.request_data.assert_called_once()

    def test_smartblock_set(self):
        self.instance.smartblock_set()
        self.instance.request_data.assert_called_once()

    def test_smartblock_trusted_delete(self):
        self.instance.smartblock_trusted_delete(entries='test')
        self.instance.request_data.assert_called_once()

    def test_smartblock_trusted_get(self):
        self.instance.smartblock_trusted_get()
        self.instance.request_data.assert_called_once()

    def test_smartblock_trusted_list(self):
        self.instance.smartblock_trusted_list()
        self.instance.request_data.assert_called_once()

    def test_smartblock_trusted_set(self):
        self.instance.smartblock_trusted_set(entries='test')
        self.instance.request_data.assert_called_once()

    def test_smartblock_untrusted_delete(self):
        self.instance.smartblock_untrusted_delete(entries='test')
        self.instance.request_data.assert_called_once()

    def test_smartblock_untrusted_get(self):
        self.instance.smartblock_untrusted_get()
        self.instance.request_data.assert_called_once()

    def test_smartblock_untrusted_list(self):
        self.instance.smartblock_untrusted_list()
        self.instance.request_data.assert_called_once()

    def test_smartblock_untrusted_set(self):
        self.instance.smartblock_untrusted_set(entries='test')
        self.instance.request_data.assert_called_once()

    def test_smartblock_user_delete(self):
        self.instance.smartblock_user_delete(users='test')
        self.instance.request_data.assert_called_once()

    def test_smartblock_user_get(self):
        self.instance.smartblock_user_get()
        self.instance.request_data.assert_called_once()

    def test_smartblock_user_list(self):
        self.instance.smartblock_user_list()
        self.instance.request_data.assert_called_once()

    def test_smartblock_user_set(self):
        self.instance.smartblock_user_set(users='test')
        self.instance.request_data.assert_called_once()

    def test_trust_device_delete(self):
        self.instance.trust_device_delete(devices='test')
        self.instance.request_data.assert_called_once()

    def test_trust_device_get(self):
        self.instance.trust_device_get()
        self.instance.request_data.assert_called_once()

    def test_trust_device_list(self):
        self.instance.trust_device_list()
        self.instance.request_data.assert_called_once()


class TestCoreSecurityCoverage(unittest.TestCase):
    """Meta-tests for API namespace coverage."""

    def test_all_namespaces_covered(self):
        """Every API namespace must be referenced in at least one method."""
        source = inspect.getsource(CoreSecurity)
        required = {
        'SYNO.Core.DisableAdmin',
        'SYNO.Core.OTP',
        'SYNO.Core.OTP.Admin',
        'SYNO.Core.OTP.EnforcePolicy',
        'SYNO.Core.OTP.Ex',
        'SYNO.Core.OTP.Mail',
        'SYNO.Core.Security.AutoBlock.Rules',
        'SYNO.Core.Security.DSM',
        'SYNO.Core.Security.DSM.Embed',
        'SYNO.Core.Security.DSM.Proxy',
        'SYNO.Core.Security.DoS',
        'SYNO.Core.Security.Firewall',
        'SYNO.Core.Security.Firewall.Adapter',
        'SYNO.Core.Security.Firewall.Conf',
        'SYNO.Core.Security.Firewall.Geoip',
        'SYNO.Core.Security.Firewall.Profile.Apply',
        'SYNO.Core.Security.Firewall.Rules',
        'SYNO.Core.Security.Firewall.Rules.Serv',
        'SYNO.Core.SmartBlock',
        'SYNO.Core.SmartBlock.Device',
        'SYNO.Core.SmartBlock.Trusted',
        'SYNO.Core.SmartBlock.Untrusted',
        'SYNO.Core.SmartBlock.User',
        'SYNO.Core.TrustDevice'
    }
        for ns in required:
            with self.subTest(namespace=ns):
                self.assertIn(f"'{ns}'", source)

    def test_method_count(self):
        """Verify expected number of public methods."""
        public = [m for m in dir(CoreSecurity)
                  if not m.startswith('_') and callable(getattr(CoreSecurity, m))
                  and m != 'logout']
        self.assertGreaterEqual(len(public), 60,
                                f"Expected 60+ methods, found {len(public)}")


if __name__ == '__main__':
    unittest.main()
