"""Unit tests for core_directory — verifies all API namespaces are covered."""

import inspect
import unittest
from unittest.mock import MagicMock, patch

from synology_api.core_directory import CoreDirectory


def _make_instance():
    """Create a CoreDirectory instance with mocked auth/session."""
    with patch('synology_api.core_directory.base_api.BaseApi.__init__', return_value=None):
        instance = CoreDirectory.__new__(CoreDirectory)

    api_list = {
        'SYNO.Core.Directory.Azure.SSO': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Directory.Domain.Conf': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Directory.Domain.Trust': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Directory.LDAP.BaseDN': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Directory.LDAP.Login.Notify': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Directory.LDAP.Profile': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Directory.LDAP.Refresh': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Directory.LDAP.User': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Directory.OIDC.SSO': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Directory.SSO.CAS': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Directory.SSO.Profile': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Directory.SSO.SAML': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Directory.SSO.SAML.Metadata': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Directory.SSO.SAML.Status': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Directory.SSO.Setting': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Directory.SSO.Status': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Directory.SSO.utils': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Directory.WebSphere.SSO': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.DirectoryServiceCheck.Common': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.DirectoryServiceCheck.Debug': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.DirectoryServiceCheck.Domain': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.DirectoryServiceCheck.DomainJoin': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.DirectoryServiceCheck.DomainService': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.DirectoryServiceCheck.DomainValidation': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.DirectoryServiceCheck.LDAP': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.DirectoryServiceCheck.Progress': {'path': 'entry.cgi', 'maxVersion': 1},
    }
    instance.gen_list = api_list
    instance.request_data = MagicMock(return_value={'success': True, 'data': {}})
    return instance


class TestCoreDirectory(unittest.TestCase):
    """Tests for CoreDirectory methods."""

    def setUp(self):
        self.instance = _make_instance()

    def test_directory_azure_sso_get(self):
        self.instance.directory_azure_sso_get()
        self.instance.request_data.assert_called_once()

    def test_directory_azure_sso_set(self):
        self.instance.directory_azure_sso_set(enable='test', tenant_id='test', client_id='test')
        self.instance.request_data.assert_called_once()

    def test_directory_domain_conf_get(self):
        self.instance.directory_domain_conf_get()
        self.instance.request_data.assert_called_once()

    def test_directory_domain_conf_set(self):
        self.instance.directory_domain_conf_set(conf='test')
        self.instance.request_data.assert_called_once()

    def test_directory_domain_trust_get(self):
        self.instance.directory_domain_trust_get()
        self.instance.request_data.assert_called_once()

    def test_directory_domain_trust_set(self):
        self.instance.directory_domain_trust_set(trust='test')
        self.instance.request_data.assert_called_once()

    def test_directory_ldap_base_dn_get(self):
        self.instance.directory_ldap_base_dn_get()
        self.instance.request_data.assert_called_once()

    def test_directory_ldap_base_dn_set(self):
        self.instance.directory_ldap_base_dn_set(base_dn='test')
        self.instance.request_data.assert_called_once()

    def test_directory_ldap_login_notify_get(self):
        self.instance.directory_ldap_login_notify_get()
        self.instance.request_data.assert_called_once()

    def test_directory_ldap_login_notify_set(self):
        self.instance.directory_ldap_login_notify_set(enable='test')
        self.instance.request_data.assert_called_once()

    def test_directory_ldap_profile_get(self):
        self.instance.directory_ldap_profile_get()
        self.instance.request_data.assert_called_once()

    def test_directory_ldap_profile_set(self):
        self.instance.directory_ldap_profile_set(profile={"test": True})
        self.instance.request_data.assert_called_once()

    def test_directory_ldap_refresh_get(self):
        self.instance.directory_ldap_refresh_get()
        self.instance.request_data.assert_called_once()

    def test_directory_ldap_refresh_set(self):
        self.instance.directory_ldap_refresh_set()
        self.instance.request_data.assert_called_once()

    def test_directory_ldap_user_get(self):
        self.instance.directory_ldap_user_get()
        self.instance.request_data.assert_called_once()

    def test_directory_ldap_user_set(self):
        self.instance.directory_ldap_user_set(user='test')
        self.instance.request_data.assert_called_once()

    def test_directory_oidc_sso_get(self):
        self.instance.directory_oidc_sso_get()
        self.instance.request_data.assert_called_once()

    def test_directory_oidc_sso_set(self):
        self.instance.directory_oidc_sso_set(enable='test', issuer='test', client_id='test')
        self.instance.request_data.assert_called_once()

    def test_directory_service_check_common_get(self):
        self.instance.directory_service_check_common_get()
        self.instance.request_data.assert_called_once()

    def test_directory_service_check_common_set(self):
        self.instance.directory_service_check_common_set(action='test')
        self.instance.request_data.assert_called_once()

    def test_directory_service_check_debug_get(self):
        self.instance.directory_service_check_debug_get()
        self.instance.request_data.assert_called_once()

    def test_directory_service_check_debug_set(self):
        self.instance.directory_service_check_debug_set(enable='test')
        self.instance.request_data.assert_called_once()

    def test_directory_service_check_domain_get(self):
        self.instance.directory_service_check_domain_get()
        self.instance.request_data.assert_called_once()

    def test_directory_service_check_domain_join_get(self):
        self.instance.directory_service_check_domain_join_get()
        self.instance.request_data.assert_called_once()

    def test_directory_service_check_domain_join_set(self):
        self.instance.directory_service_check_domain_join_set(action='test')
        self.instance.request_data.assert_called_once()

    def test_directory_service_check_domain_service_get(self):
        self.instance.directory_service_check_domain_service_get()
        self.instance.request_data.assert_called_once()

    def test_directory_service_check_domain_service_set(self):
        self.instance.directory_service_check_domain_service_set(action='test')
        self.instance.request_data.assert_called_once()

    def test_directory_service_check_domain_set(self):
        self.instance.directory_service_check_domain_set(action='test')
        self.instance.request_data.assert_called_once()

    def test_directory_service_check_domain_validation_get(self):
        self.instance.directory_service_check_domain_validation_get()
        self.instance.request_data.assert_called_once()

    def test_directory_service_check_domain_validation_set(self):
        self.instance.directory_service_check_domain_validation_set(action='test')
        self.instance.request_data.assert_called_once()

    def test_directory_service_check_ldap_get(self):
        self.instance.directory_service_check_ldap_get()
        self.instance.request_data.assert_called_once()

    def test_directory_service_check_ldap_set(self):
        self.instance.directory_service_check_ldap_set(action='test')
        self.instance.request_data.assert_called_once()

    def test_directory_service_check_progress_get(self):
        self.instance.directory_service_check_progress_get()
        self.instance.request_data.assert_called_once()

    def test_directory_service_check_progress_set(self):
        self.instance.directory_service_check_progress_set(action='test')
        self.instance.request_data.assert_called_once()

    def test_directory_sso_cas_get(self):
        self.instance.directory_sso_cas_get()
        self.instance.request_data.assert_called_once()

    def test_directory_sso_cas_set(self):
        self.instance.directory_sso_cas_set(settings='test')
        self.instance.request_data.assert_called_once()

    def test_directory_sso_profile_get(self):
        self.instance.directory_sso_profile_get()
        self.instance.request_data.assert_called_once()

    def test_directory_sso_profile_set(self):
        self.instance.directory_sso_profile_set(profile={"test": True})
        self.instance.request_data.assert_called_once()

    def test_directory_sso_saml_get(self):
        self.instance.directory_sso_saml_get()
        self.instance.request_data.assert_called_once()

    def test_directory_sso_saml_metadata_get(self):
        self.instance.directory_sso_saml_metadata_get()
        self.instance.request_data.assert_called_once()

    def test_directory_sso_saml_metadata_set(self):
        self.instance.directory_sso_saml_metadata_set(metadata='test')
        self.instance.request_data.assert_called_once()

    def test_directory_sso_saml_set(self):
        self.instance.directory_sso_saml_set(settings='test')
        self.instance.request_data.assert_called_once()

    def test_directory_sso_saml_status_get(self):
        self.instance.directory_sso_saml_status_get()
        self.instance.request_data.assert_called_once()

    def test_directory_sso_saml_status_set(self):
        self.instance.directory_sso_saml_status_set(enable='test')
        self.instance.request_data.assert_called_once()

    def test_directory_sso_setting_get(self):
        self.instance.directory_sso_setting_get()
        self.instance.request_data.assert_called_once()

    def test_directory_sso_setting_set(self):
        self.instance.directory_sso_setting_set(settings='test')
        self.instance.request_data.assert_called_once()

    def test_directory_sso_status_get(self):
        self.instance.directory_sso_status_get()
        self.instance.request_data.assert_called_once()

    def test_directory_sso_status_set(self):
        self.instance.directory_sso_status_set(enable='test')
        self.instance.request_data.assert_called_once()

    def test_directory_sso_utils_get(self):
        self.instance.directory_sso_utils_get()
        self.instance.request_data.assert_called_once()

    def test_directory_sso_utils_set(self):
        self.instance.directory_sso_utils_set(data='test')
        self.instance.request_data.assert_called_once()

    def test_directory_websphere_sso_get(self):
        self.instance.directory_websphere_sso_get()
        self.instance.request_data.assert_called_once()

    def test_directory_websphere_sso_set(self):
        self.instance.directory_websphere_sso_set(enable='test', settings='test')
        self.instance.request_data.assert_called_once()


class TestCoreDirectoryCoverage(unittest.TestCase):
    """Meta-tests for API namespace coverage."""

    def test_all_namespaces_covered(self):
        """Every API namespace must be referenced in at least one method."""
        source = inspect.getsource(CoreDirectory)
        required = {
        'SYNO.Core.Directory.Azure.SSO',
        'SYNO.Core.Directory.Domain.Conf',
        'SYNO.Core.Directory.Domain.Trust',
        'SYNO.Core.Directory.LDAP.BaseDN',
        'SYNO.Core.Directory.LDAP.Login.Notify',
        'SYNO.Core.Directory.LDAP.Profile',
        'SYNO.Core.Directory.LDAP.Refresh',
        'SYNO.Core.Directory.LDAP.User',
        'SYNO.Core.Directory.OIDC.SSO',
        'SYNO.Core.Directory.SSO.CAS',
        'SYNO.Core.Directory.SSO.Profile',
        'SYNO.Core.Directory.SSO.SAML',
        'SYNO.Core.Directory.SSO.SAML.Metadata',
        'SYNO.Core.Directory.SSO.SAML.Status',
        'SYNO.Core.Directory.SSO.Setting',
        'SYNO.Core.Directory.SSO.Status',
        'SYNO.Core.Directory.SSO.utils',
        'SYNO.Core.Directory.WebSphere.SSO',
        'SYNO.Core.DirectoryServiceCheck.Common',
        'SYNO.Core.DirectoryServiceCheck.Debug',
        'SYNO.Core.DirectoryServiceCheck.Domain',
        'SYNO.Core.DirectoryServiceCheck.DomainJoin',
        'SYNO.Core.DirectoryServiceCheck.DomainService',
        'SYNO.Core.DirectoryServiceCheck.DomainValidation',
        'SYNO.Core.DirectoryServiceCheck.LDAP',
        'SYNO.Core.DirectoryServiceCheck.Progress'
    }
        for ns in required:
            with self.subTest(namespace=ns):
                self.assertIn(f"'{ns}'", source)

    def test_method_count(self):
        """Verify expected number of public methods."""
        public = [m for m in dir(CoreDirectory)
                  if not m.startswith('_') and callable(getattr(CoreDirectory, m))
                  and m != 'logout']
        self.assertGreaterEqual(len(public), 52,
                                f"Expected 52+ methods, found {len(public)}")


if __name__ == '__main__':
    unittest.main()
