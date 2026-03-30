"""Unit tests for core_service — verifies all API namespaces are covered."""

import inspect
import unittest
from unittest.mock import MagicMock, patch

from synology_api.core_service import CoreService


def _make_instance():
    """Create a CoreService instance with mocked auth/session."""
    with patch('synology_api.core_service.base_api.BaseApi.__init__', return_value=None):
        instance = CoreService.__new__(CoreService)

    api_list = {
        'SYNO.Core.ACL': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.ActionPriv': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.ActionPriv.Role': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.AppNotify': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.AppPortal': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.AppPortal.AccessControl': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.AppPortal.Config': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.AppPortal.ReverseProxy': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.AppPriv': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.AppPriv.App': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.AppPriv.Rule': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.BackgroundTask': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Backup.ED': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.BandwidthControl': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.CMS': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.CMS.Cache': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.CMS.Identity': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.CMS.Policy': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.CMS.ServerInfo': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.CMS.Task': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.CMS.Token': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Certificate.CSR': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Certificate.LetsEncrypt': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Certificate.LetsEncrypt.Account': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Certificate.Tencent': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.DDNS.Ethernet': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.DDNS.TWNIC': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.DSMNotify.MailContent': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.DSMNotify.Strings': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.DataCollect': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.DataCollect.Application': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.EW.Info': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Factory.Config': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Factory.Manutild': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.File': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.File.Thumbnail': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.FileServ.NFS.AdvancedSetting': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.FileServ.NFS.ConfBackup': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.FileServ.NFS.IDMap': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.FileServ.NFS.Kerberos': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.FileServ.NFS.SharePrivilege': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.FileServ.Rsync.Account': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.FileServ.SMB.ConfBackup': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.FileServ.SMB.Control': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.FileServ.SMB.MSDFS': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Findhost': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Group.ExtraAdmin': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Group.Member': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Group.ValidLocalAdmin': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Hardware.LCM': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Hardware.Led.Brightness': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Hardware.MemoryLayout': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Hardware.NeedReboot': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Hardware.OOBManagement': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Hardware.RemoteFanStatus': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Hardware.SpectreMeltdown': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Hardware.VideoTranscoding': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.ISCSI.FCTarget': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.ISCSI.Host': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.ISCSI.Lunbkp': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.ISCSI.Node': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.ISCSI.Replication': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.ISCSI.VMware': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.MediaIndexing': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.MediaIndexing.IndexFolder': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.MediaIndexing.MediaConverter': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.MediaIndexing.Scheduler': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.MediaIndexing.ThumbnailQuality': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.MyDSCenter': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.MyDSCenter.Account': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.MyDSCenter.Login': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.MyDSCenter.Logout': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.MyDSCenter.Purchase': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.NormalUser': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.NormalUser.LoginNotify': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.OAuth.Scope': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.OAuth.Server': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Package.AutoUpgrade.Progress': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Package.Control': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Package.FakeIFrame': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Package.Feed': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Package.Legal.PreRelease': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Package.Log': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Package.MyDS': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Package.MyDS.Purchase': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Package.Progress': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Package.Screenshot': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Package.Screenshot.Server': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Package.Setting.Update': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Package.Thumb': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Package.Thumb.Server': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.PersonalNotification.Device': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.PersonalNotification.Event': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.PersonalNotification.Filter': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.PersonalNotification.Mobile': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.PersonalNotification.Settings': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.PhotoViewer': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.PortForwarding': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.PortForwarding.Compatibility': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.PortForwarding.RouterInfo': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.PortForwarding.RouterList': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.PortForwarding.Rules.Serv': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Promotion.Info': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Promotion.PreInstall': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.QuickConnect.Hostname': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.QuickConnect.RegisterSite': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.QuickConnect.SNI': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.QuickConnect.Upnp': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.QuickStart.Info': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.QuickStart.Install': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Report': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Report.Analyzer': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Report.Analyzer.File': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Report.Analyzer.Share': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Report.Config': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Report.History': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Report.Redirect': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Report.Util': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.ResetAdmin': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.SecurityScan.Operation': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Service.Conf': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Service.PortInfo': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Share.Crypto': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Share.Crypto.Key': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Share.CryptoFile': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Share.KeyManager.AutoKey': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Share.KeyManager.Key': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Share.KeyManager.MachineKey': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Share.KeyManager.Store': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Share.Migration': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Share.Migration.Task': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Share.Permission': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Share.PermissionReport': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Share.ShellFile': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Sharing': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Sharing.Initdata': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Sharing.Login': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Sharing.Session': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.SupportForm.Form': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.SupportForm.Log': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.SupportForm.Service': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Synohdpack': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.SyslogClient.PersonalActivity': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Tuned': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.User.Group': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.User.PasswordExpiry': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.User.PasswordMeter': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.User.PasswordPolicy': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.User.UsernamePolicy': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Virtualization.Host.Capability': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.VolEncKeepKey': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Web.DSM.External': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Web.Security.HTTPCompression': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Web.Security.TLSProfile': {'path': 'entry.cgi', 'maxVersion': 1},
    }
    instance.gen_list = api_list
    instance.request_data = MagicMock(return_value={'success': True, 'data': {}})
    return instance


class TestCoreService(unittest.TestCase):
    """Tests for CoreService methods."""

    def setUp(self):
        self.instance = _make_instance()

    def test_acl_get(self):
        self.instance.acl_get(path='test')
        self.instance.request_data.assert_called_once()

    def test_acl_set(self):
        self.instance.acl_set(path='test', acl={"test": True})
        self.instance.request_data.assert_called_once()

    def test_action_priv_get(self):
        self.instance.action_priv_get()
        self.instance.request_data.assert_called_once()

    def test_action_priv_role_get(self):
        self.instance.action_priv_role_get()
        self.instance.request_data.assert_called_once()

    def test_action_priv_role_set(self):
        self.instance.action_priv_role_set(roles={"test": True})
        self.instance.request_data.assert_called_once()

    def test_app_notify_get(self):
        self.instance.app_notify_get()
        self.instance.request_data.assert_called_once()

    def test_app_portal_access_control_get(self):
        self.instance.app_portal_access_control_get()
        self.instance.request_data.assert_called_once()

    def test_app_portal_access_control_set(self):
        self.instance.app_portal_access_control_set()
        self.instance.request_data.assert_called_once()

    def test_app_portal_config_get(self):
        self.instance.app_portal_config_get()
        self.instance.request_data.assert_called_once()

    def test_app_portal_get(self):
        self.instance.app_portal_get()
        self.instance.request_data.assert_called_once()

    def test_app_portal_reverse_proxy_get(self):
        self.instance.app_portal_reverse_proxy_get()
        self.instance.request_data.assert_called_once()

    def test_app_portal_reverse_proxy_set(self):
        self.instance.app_portal_reverse_proxy_set()
        self.instance.request_data.assert_called_once()

    def test_app_portal_set(self):
        self.instance.app_portal_set()
        self.instance.request_data.assert_called_once()

    def test_app_priv_app_get(self):
        self.instance.app_priv_app_get()
        self.instance.request_data.assert_called_once()

    def test_app_priv_get(self):
        self.instance.app_priv_get()
        self.instance.request_data.assert_called_once()

    def test_app_priv_rule_get(self):
        self.instance.app_priv_rule_get()
        self.instance.request_data.assert_called_once()

    def test_app_priv_rule_set(self):
        self.instance.app_priv_rule_set(rules={"test": True})
        self.instance.request_data.assert_called_once()

    def test_background_task_get(self):
        self.instance.background_task_get(task_id='test')
        self.instance.request_data.assert_called_once()

    def test_background_task_list(self):
        self.instance.background_task_list()
        self.instance.request_data.assert_called_once()

    def test_backup_ed_get(self):
        self.instance.backup_ed_get()
        self.instance.request_data.assert_called_once()

    def test_bandwidth_control_get(self):
        self.instance.bandwidth_control_get()
        self.instance.request_data.assert_called_once()

    def test_bandwidth_control_set(self):
        self.instance.bandwidth_control_set()
        self.instance.request_data.assert_called_once()

    def test_certificate_csr_create(self):
        self.instance.certificate_csr_create()
        self.instance.request_data.assert_called_once()

    def test_certificate_csr_get(self):
        self.instance.certificate_csr_get()
        self.instance.request_data.assert_called_once()

    def test_certificate_letsencrypt_account_get(self):
        self.instance.certificate_letsencrypt_account_get()
        self.instance.request_data.assert_called_once()

    def test_certificate_letsencrypt_create(self):
        self.instance.certificate_letsencrypt_create()
        self.instance.request_data.assert_called_once()

    def test_certificate_letsencrypt_get(self):
        self.instance.certificate_letsencrypt_get()
        self.instance.request_data.assert_called_once()

    def test_certificate_tencent_get(self):
        self.instance.certificate_tencent_get()
        self.instance.request_data.assert_called_once()

    def test_cms_cache_get(self):
        self.instance.cms_cache_get()
        self.instance.request_data.assert_called_once()

    def test_cms_get(self):
        self.instance.cms_get()
        self.instance.request_data.assert_called_once()

    def test_cms_identity_get(self):
        self.instance.cms_identity_get()
        self.instance.request_data.assert_called_once()

    def test_cms_policy_get(self):
        self.instance.cms_policy_get()
        self.instance.request_data.assert_called_once()

    def test_cms_policy_set(self):
        self.instance.cms_policy_set()
        self.instance.request_data.assert_called_once()

    def test_cms_server_info_get(self):
        self.instance.cms_server_info_get()
        self.instance.request_data.assert_called_once()

    def test_cms_task_get(self):
        self.instance.cms_task_get()
        self.instance.request_data.assert_called_once()

    def test_cms_token_get(self):
        self.instance.cms_token_get()
        self.instance.request_data.assert_called_once()

    def test_data_collect_application_get(self):
        self.instance.data_collect_application_get()
        self.instance.request_data.assert_called_once()

    def test_data_collect_get(self):
        self.instance.data_collect_get()
        self.instance.request_data.assert_called_once()

    def test_data_collect_set(self):
        self.instance.data_collect_set(enabled=True)
        self.instance.request_data.assert_called_once()

    def test_ddns_ethernet_get(self):
        self.instance.ddns_ethernet_get()
        self.instance.request_data.assert_called_once()

    def test_ddns_twnic_get(self):
        self.instance.ddns_twnic_get()
        self.instance.request_data.assert_called_once()

    def test_dsm_notify_mail_content_get(self):
        self.instance.dsm_notify_mail_content_get()
        self.instance.request_data.assert_called_once()

    def test_dsm_notify_strings_get(self):
        self.instance.dsm_notify_strings_get()
        self.instance.request_data.assert_called_once()

    def test_ew_info_get(self):
        self.instance.ew_info_get()
        self.instance.request_data.assert_called_once()

    def test_factory_config_get(self):
        self.instance.factory_config_get()
        self.instance.request_data.assert_called_once()

    def test_factory_manutild_get(self):
        self.instance.factory_manutild_get()
        self.instance.request_data.assert_called_once()

    def test_file_get(self):
        self.instance.file_get(path='test')
        self.instance.request_data.assert_called_once()

    def test_file_thumbnail_get(self):
        self.instance.file_thumbnail_get(path='test', size='test')
        self.instance.request_data.assert_called_once()

    def test_fileserv_nfs_advanced_get(self):
        self.instance.fileserv_nfs_advanced_get()
        self.instance.request_data.assert_called_once()

    def test_fileserv_nfs_advanced_set(self):
        self.instance.fileserv_nfs_advanced_set()
        self.instance.request_data.assert_called_once()

    def test_fileserv_nfs_conf_backup_get(self):
        self.instance.fileserv_nfs_conf_backup_get()
        self.instance.request_data.assert_called_once()

    def test_fileserv_nfs_idmap_get(self):
        self.instance.fileserv_nfs_idmap_get()
        self.instance.request_data.assert_called_once()

    def test_fileserv_nfs_kerberos_get(self):
        self.instance.fileserv_nfs_kerberos_get()
        self.instance.request_data.assert_called_once()

    def test_fileserv_nfs_share_privilege_get(self):
        self.instance.fileserv_nfs_share_privilege_get()
        self.instance.request_data.assert_called_once()

    def test_fileserv_rsync_account_get(self):
        self.instance.fileserv_rsync_account_get()
        self.instance.request_data.assert_called_once()

    def test_fileserv_rsync_account_set(self):
        self.instance.fileserv_rsync_account_set()
        self.instance.request_data.assert_called_once()

    def test_fileserv_smb_conf_backup_get(self):
        self.instance.fileserv_smb_conf_backup_get()
        self.instance.request_data.assert_called_once()

    def test_fileserv_smb_control_get(self):
        self.instance.fileserv_smb_control_get()
        self.instance.request_data.assert_called_once()

    def test_fileserv_smb_msdfs_get(self):
        self.instance.fileserv_smb_msdfs_get()
        self.instance.request_data.assert_called_once()

    def test_findhost_get(self):
        self.instance.findhost_get()
        self.instance.request_data.assert_called_once()

    def test_group_extra_admin_get(self):
        self.instance.group_extra_admin_get()
        self.instance.request_data.assert_called_once()

    def test_group_member_list(self):
        self.instance.group_member_list(group='test')
        self.instance.request_data.assert_called_once()

    def test_group_valid_local_admin_get(self):
        self.instance.group_valid_local_admin_get()
        self.instance.request_data.assert_called_once()

    def test_hardware_lcm_get(self):
        self.instance.hardware_lcm_get()
        self.instance.request_data.assert_called_once()

    def test_hardware_led_brightness_get(self):
        self.instance.hardware_led_brightness_get()
        self.instance.request_data.assert_called_once()

    def test_hardware_led_brightness_set(self):
        self.instance.hardware_led_brightness_set(brightness=1)
        self.instance.request_data.assert_called_once()

    def test_hardware_memory_layout_get(self):
        self.instance.hardware_memory_layout_get()
        self.instance.request_data.assert_called_once()

    def test_hardware_need_reboot_get(self):
        self.instance.hardware_need_reboot_get()
        self.instance.request_data.assert_called_once()

    def test_hardware_oob_management_get(self):
        self.instance.hardware_oob_management_get()
        self.instance.request_data.assert_called_once()

    def test_hardware_remote_fan_status_get(self):
        self.instance.hardware_remote_fan_status_get()
        self.instance.request_data.assert_called_once()

    def test_hardware_spectre_meltdown_get(self):
        self.instance.hardware_spectre_meltdown_get()
        self.instance.request_data.assert_called_once()

    def test_hardware_video_transcoding_get(self):
        self.instance.hardware_video_transcoding_get()
        self.instance.request_data.assert_called_once()

    def test_iscsi_fc_target_get(self):
        self.instance.iscsi_fc_target_get()
        self.instance.request_data.assert_called_once()

    def test_iscsi_host_get(self):
        self.instance.iscsi_host_get()
        self.instance.request_data.assert_called_once()

    def test_iscsi_lunbkp_get(self):
        self.instance.iscsi_lunbkp_get()
        self.instance.request_data.assert_called_once()

    def test_iscsi_node_get(self):
        self.instance.iscsi_node_get()
        self.instance.request_data.assert_called_once()

    def test_iscsi_replication_get(self):
        self.instance.iscsi_replication_get()
        self.instance.request_data.assert_called_once()

    def test_iscsi_vmware_get(self):
        self.instance.iscsi_vmware_get()
        self.instance.request_data.assert_called_once()

    def test_media_indexing_get(self):
        self.instance.media_indexing_get()
        self.instance.request_data.assert_called_once()

    def test_media_indexing_index_folder_get(self):
        self.instance.media_indexing_index_folder_get()
        self.instance.request_data.assert_called_once()

    def test_media_indexing_media_converter_get(self):
        self.instance.media_indexing_media_converter_get()
        self.instance.request_data.assert_called_once()

    def test_media_indexing_scheduler_get(self):
        self.instance.media_indexing_scheduler_get()
        self.instance.request_data.assert_called_once()

    def test_media_indexing_set(self):
        self.instance.media_indexing_set()
        self.instance.request_data.assert_called_once()

    def test_media_indexing_thumbnail_quality_get(self):
        self.instance.media_indexing_thumbnail_quality_get()
        self.instance.request_data.assert_called_once()

    def test_mydscenter_account_get(self):
        self.instance.mydscenter_account_get()
        self.instance.request_data.assert_called_once()

    def test_mydscenter_get(self):
        self.instance.mydscenter_get()
        self.instance.request_data.assert_called_once()

    def test_mydscenter_login(self):
        self.instance.mydscenter_login(username='test', password='test')
        self.instance.request_data.assert_called_once()

    def test_mydscenter_logout(self):
        self.instance.mydscenter_logout()
        self.instance.request_data.assert_called_once()

    def test_mydscenter_purchase_get(self):
        self.instance.mydscenter_purchase_get()
        self.instance.request_data.assert_called_once()

    def test_normal_user_get(self):
        self.instance.normal_user_get()
        self.instance.request_data.assert_called_once()

    def test_normal_user_login_notify_get(self):
        self.instance.normal_user_login_notify_get()
        self.instance.request_data.assert_called_once()

    def test_oauth_scope_get(self):
        self.instance.oauth_scope_get()
        self.instance.request_data.assert_called_once()

    def test_oauth_server_get(self):
        self.instance.oauth_server_get()
        self.instance.request_data.assert_called_once()

    def test_oauth_server_set(self):
        self.instance.oauth_server_set()
        self.instance.request_data.assert_called_once()

    def test_package_auto_upgrade_progress_get(self):
        self.instance.package_auto_upgrade_progress_get()
        self.instance.request_data.assert_called_once()

    def test_package_control(self):
        self.instance.package_control(package_id='test', action='test')
        self.instance.request_data.assert_called_once()

    def test_package_fake_iframe_get(self):
        self.instance.package_fake_iframe_get()
        self.instance.request_data.assert_called_once()

    def test_package_feed_list(self):
        self.instance.package_feed_list()
        self.instance.request_data.assert_called_once()

    def test_package_feed_set(self):
        self.instance.package_feed_set()
        self.instance.request_data.assert_called_once()

    def test_package_legal_prerelease_get(self):
        self.instance.package_legal_prerelease_get()
        self.instance.request_data.assert_called_once()

    def test_package_log_get(self):
        self.instance.package_log_get(package_id='test')
        self.instance.request_data.assert_called_once()

    def test_package_myds_get(self):
        self.instance.package_myds_get()
        self.instance.request_data.assert_called_once()

    def test_package_myds_purchase_get(self):
        self.instance.package_myds_purchase_get()
        self.instance.request_data.assert_called_once()

    def test_package_progress_get(self):
        self.instance.package_progress_get(task_id='test')
        self.instance.request_data.assert_called_once()

    def test_package_screenshot_get(self):
        self.instance.package_screenshot_get(package_id='test')
        self.instance.request_data.assert_called_once()

    def test_package_screenshot_server_get(self):
        self.instance.package_screenshot_server_get(package_id='test')
        self.instance.request_data.assert_called_once()

    def test_package_setting_update_get(self):
        self.instance.package_setting_update_get()
        self.instance.request_data.assert_called_once()

    def test_package_thumb_get(self):
        self.instance.package_thumb_get(package_id='test')
        self.instance.request_data.assert_called_once()

    def test_package_thumb_server_get(self):
        self.instance.package_thumb_server_get(package_id='test')
        self.instance.request_data.assert_called_once()

    def test_personal_notification_device_get(self):
        self.instance.personal_notification_device_get()
        self.instance.request_data.assert_called_once()

    def test_personal_notification_event_get(self):
        self.instance.personal_notification_event_get()
        self.instance.request_data.assert_called_once()

    def test_personal_notification_filter_get(self):
        self.instance.personal_notification_filter_get()
        self.instance.request_data.assert_called_once()

    def test_personal_notification_filter_set(self):
        self.instance.personal_notification_filter_set()
        self.instance.request_data.assert_called_once()

    def test_personal_notification_mobile_get(self):
        self.instance.personal_notification_mobile_get()
        self.instance.request_data.assert_called_once()

    def test_personal_notification_settings_get(self):
        self.instance.personal_notification_settings_get()
        self.instance.request_data.assert_called_once()

    def test_personal_notification_settings_set(self):
        self.instance.personal_notification_settings_set()
        self.instance.request_data.assert_called_once()

    def test_photo_viewer_get(self):
        self.instance.photo_viewer_get()
        self.instance.request_data.assert_called_once()

    def test_port_forwarding_compatibility_get(self):
        self.instance.port_forwarding_compatibility_get()
        self.instance.request_data.assert_called_once()

    def test_port_forwarding_get(self):
        self.instance.port_forwarding_get()
        self.instance.request_data.assert_called_once()

    def test_port_forwarding_router_info_get(self):
        self.instance.port_forwarding_router_info_get()
        self.instance.request_data.assert_called_once()

    def test_port_forwarding_router_list(self):
        self.instance.port_forwarding_router_list()
        self.instance.request_data.assert_called_once()

    def test_port_forwarding_rules_serv_get(self):
        self.instance.port_forwarding_rules_serv_get()
        self.instance.request_data.assert_called_once()

    def test_promotion_info_get(self):
        self.instance.promotion_info_get()
        self.instance.request_data.assert_called_once()

    def test_promotion_preinstall_get(self):
        self.instance.promotion_preinstall_get()
        self.instance.request_data.assert_called_once()

    def test_quickconnect_hostname_get(self):
        self.instance.quickconnect_hostname_get()
        self.instance.request_data.assert_called_once()

    def test_quickconnect_register_site_get(self):
        self.instance.quickconnect_register_site_get()
        self.instance.request_data.assert_called_once()

    def test_quickconnect_sni_get(self):
        self.instance.quickconnect_sni_get()
        self.instance.request_data.assert_called_once()

    def test_quickconnect_upnp_get(self):
        self.instance.quickconnect_upnp_get()
        self.instance.request_data.assert_called_once()

    def test_quickstart_info_get(self):
        self.instance.quickstart_info_get()
        self.instance.request_data.assert_called_once()

    def test_quickstart_install(self):
        self.instance.quickstart_install()
        self.instance.request_data.assert_called_once()

    def test_report_analyzer_file_get(self):
        self.instance.report_analyzer_file_get()
        self.instance.request_data.assert_called_once()

    def test_report_analyzer_get(self):
        self.instance.report_analyzer_get()
        self.instance.request_data.assert_called_once()

    def test_report_analyzer_share_get(self):
        self.instance.report_analyzer_share_get()
        self.instance.request_data.assert_called_once()

    def test_report_config_get(self):
        self.instance.report_config_get()
        self.instance.request_data.assert_called_once()

    def test_report_config_set(self):
        self.instance.report_config_set()
        self.instance.request_data.assert_called_once()

    def test_report_get(self):
        self.instance.report_get()
        self.instance.request_data.assert_called_once()

    def test_report_history_get(self):
        self.instance.report_history_get()
        self.instance.request_data.assert_called_once()

    def test_report_redirect_get(self):
        self.instance.report_redirect_get()
        self.instance.request_data.assert_called_once()

    def test_report_util_get(self):
        self.instance.report_util_get()
        self.instance.request_data.assert_called_once()

    def test_reset_admin_get(self):
        self.instance.reset_admin_get()
        self.instance.request_data.assert_called_once()

    def test_security_scan_operation_get(self):
        self.instance.security_scan_operation_get()
        self.instance.request_data.assert_called_once()

    def test_security_scan_operation_start(self):
        self.instance.security_scan_operation_start()
        self.instance.request_data.assert_called_once()

    def test_service_conf_get(self):
        self.instance.service_conf_get()
        self.instance.request_data.assert_called_once()

    def test_service_conf_set(self):
        self.instance.service_conf_set()
        self.instance.request_data.assert_called_once()

    def test_service_port_info_get(self):
        self.instance.service_port_info_get()
        self.instance.request_data.assert_called_once()

    def test_share_crypto_file_get(self):
        self.instance.share_crypto_file_get()
        self.instance.request_data.assert_called_once()

    def test_share_crypto_get(self):
        self.instance.share_crypto_get()
        self.instance.request_data.assert_called_once()

    def test_share_crypto_key_get(self):
        self.instance.share_crypto_key_get()
        self.instance.request_data.assert_called_once()

    def test_share_key_manager_auto_key_get(self):
        self.instance.share_key_manager_auto_key_get()
        self.instance.request_data.assert_called_once()

    def test_share_key_manager_key_get(self):
        self.instance.share_key_manager_key_get()
        self.instance.request_data.assert_called_once()

    def test_share_key_manager_machine_key_get(self):
        self.instance.share_key_manager_machine_key_get()
        self.instance.request_data.assert_called_once()

    def test_share_key_manager_store_get(self):
        self.instance.share_key_manager_store_get()
        self.instance.request_data.assert_called_once()

    def test_share_migration_get(self):
        self.instance.share_migration_get()
        self.instance.request_data.assert_called_once()

    def test_share_migration_task_get(self):
        self.instance.share_migration_task_get()
        self.instance.request_data.assert_called_once()

    def test_share_permission_get(self):
        self.instance.share_permission_get(name='test')
        self.instance.request_data.assert_called_once()

    def test_share_permission_report_get(self):
        self.instance.share_permission_report_get()
        self.instance.request_data.assert_called_once()

    def test_share_permission_set(self):
        self.instance.share_permission_set(name='test', permissions={"test": True})
        self.instance.request_data.assert_called_once()

    def test_share_shell_file_get(self):
        self.instance.share_shell_file_get()
        self.instance.request_data.assert_called_once()

    def test_sharing_get(self):
        self.instance.sharing_get()
        self.instance.request_data.assert_called_once()

    def test_sharing_initdata_get(self):
        self.instance.sharing_initdata_get()
        self.instance.request_data.assert_called_once()

    def test_sharing_login(self):
        self.instance.sharing_login(sharing_id='test', password='test')
        self.instance.request_data.assert_called_once()

    def test_sharing_session_get(self):
        self.instance.sharing_session_get()
        self.instance.request_data.assert_called_once()

    def test_support_form_get(self):
        self.instance.support_form_get()
        self.instance.request_data.assert_called_once()

    def test_support_form_log_get(self):
        self.instance.support_form_log_get()
        self.instance.request_data.assert_called_once()

    def test_support_form_service_get(self):
        self.instance.support_form_service_get()
        self.instance.request_data.assert_called_once()

    def test_synohdpack_get(self):
        self.instance.synohdpack_get()
        self.instance.request_data.assert_called_once()

    def test_syslog_personal_activity_get(self):
        self.instance.syslog_personal_activity_get()
        self.instance.request_data.assert_called_once()

    def test_tuned_get(self):
        self.instance.tuned_get()
        self.instance.request_data.assert_called_once()

    def test_tuned_set(self):
        self.instance.tuned_set()
        self.instance.request_data.assert_called_once()

    def test_user_group_get(self):
        self.instance.user_group_get(user='test')
        self.instance.request_data.assert_called_once()

    def test_user_password_expiry_get(self):
        self.instance.user_password_expiry_get()
        self.instance.request_data.assert_called_once()

    def test_user_password_meter_get(self):
        self.instance.user_password_meter_get(password='test')
        self.instance.request_data.assert_called_once()

    def test_user_password_policy_get(self):
        self.instance.user_password_policy_get()
        self.instance.request_data.assert_called_once()

    def test_user_password_policy_set(self):
        self.instance.user_password_policy_set()
        self.instance.request_data.assert_called_once()

    def test_user_username_policy_get(self):
        self.instance.user_username_policy_get()
        self.instance.request_data.assert_called_once()

    def test_virtualization_host_capability_get(self):
        self.instance.virtualization_host_capability_get()
        self.instance.request_data.assert_called_once()

    def test_vol_enc_keep_key_get(self):
        self.instance.vol_enc_keep_key_get()
        self.instance.request_data.assert_called_once()

    def test_vol_enc_keep_key_set(self):
        self.instance.vol_enc_keep_key_set()
        self.instance.request_data.assert_called_once()

    def test_web_dsm_external_get(self):
        self.instance.web_dsm_external_get()
        self.instance.request_data.assert_called_once()

    def test_web_dsm_external_set(self):
        self.instance.web_dsm_external_set()
        self.instance.request_data.assert_called_once()

    def test_web_security_http_compression_get(self):
        self.instance.web_security_http_compression_get()
        self.instance.request_data.assert_called_once()

    def test_web_security_http_compression_set(self):
        self.instance.web_security_http_compression_set()
        self.instance.request_data.assert_called_once()

    def test_web_security_tls_profile_get(self):
        self.instance.web_security_tls_profile_get()
        self.instance.request_data.assert_called_once()

    def test_web_security_tls_profile_set(self):
        self.instance.web_security_tls_profile_set()
        self.instance.request_data.assert_called_once()


class TestCoreServiceCoverage(unittest.TestCase):
    """Meta-tests for API namespace coverage."""

    def test_all_namespaces_covered(self):
        """Every API namespace must be referenced in at least one method."""
        source = inspect.getsource(CoreService)
        required = {
        'SYNO.Core.ACL',
        'SYNO.Core.ActionPriv',
        'SYNO.Core.ActionPriv.Role',
        'SYNO.Core.AppNotify',
        'SYNO.Core.AppPortal',
        'SYNO.Core.AppPortal.AccessControl',
        'SYNO.Core.AppPortal.Config',
        'SYNO.Core.AppPortal.ReverseProxy',
        'SYNO.Core.AppPriv',
        'SYNO.Core.AppPriv.App',
        'SYNO.Core.AppPriv.Rule',
        'SYNO.Core.BackgroundTask',
        'SYNO.Core.Backup.ED',
        'SYNO.Core.BandwidthControl',
        'SYNO.Core.CMS',
        'SYNO.Core.CMS.Cache',
        'SYNO.Core.CMS.Identity',
        'SYNO.Core.CMS.Policy',
        'SYNO.Core.CMS.ServerInfo',
        'SYNO.Core.CMS.Task',
        'SYNO.Core.CMS.Token',
        'SYNO.Core.Certificate.CSR',
        'SYNO.Core.Certificate.LetsEncrypt',
        'SYNO.Core.Certificate.LetsEncrypt.Account',
        'SYNO.Core.Certificate.Tencent',
        'SYNO.Core.DDNS.Ethernet',
        'SYNO.Core.DDNS.TWNIC',
        'SYNO.Core.DSMNotify.MailContent',
        'SYNO.Core.DSMNotify.Strings',
        'SYNO.Core.DataCollect',
        'SYNO.Core.DataCollect.Application',
        'SYNO.Core.EW.Info',
        'SYNO.Core.Factory.Config',
        'SYNO.Core.Factory.Manutild',
        'SYNO.Core.File',
        'SYNO.Core.File.Thumbnail',
        'SYNO.Core.FileServ.NFS.AdvancedSetting',
        'SYNO.Core.FileServ.NFS.ConfBackup',
        'SYNO.Core.FileServ.NFS.IDMap',
        'SYNO.Core.FileServ.NFS.Kerberos',
        'SYNO.Core.FileServ.NFS.SharePrivilege',
        'SYNO.Core.FileServ.Rsync.Account',
        'SYNO.Core.FileServ.SMB.ConfBackup',
        'SYNO.Core.FileServ.SMB.Control',
        'SYNO.Core.FileServ.SMB.MSDFS',
        'SYNO.Core.Findhost',
        'SYNO.Core.Group.ExtraAdmin',
        'SYNO.Core.Group.Member',
        'SYNO.Core.Group.ValidLocalAdmin',
        'SYNO.Core.Hardware.LCM',
        'SYNO.Core.Hardware.Led.Brightness',
        'SYNO.Core.Hardware.MemoryLayout',
        'SYNO.Core.Hardware.NeedReboot',
        'SYNO.Core.Hardware.OOBManagement',
        'SYNO.Core.Hardware.RemoteFanStatus',
        'SYNO.Core.Hardware.SpectreMeltdown',
        'SYNO.Core.Hardware.VideoTranscoding',
        'SYNO.Core.ISCSI.FCTarget',
        'SYNO.Core.ISCSI.Host',
        'SYNO.Core.ISCSI.Lunbkp',
        'SYNO.Core.ISCSI.Node',
        'SYNO.Core.ISCSI.Replication',
        'SYNO.Core.ISCSI.VMware',
        'SYNO.Core.MediaIndexing',
        'SYNO.Core.MediaIndexing.IndexFolder',
        'SYNO.Core.MediaIndexing.MediaConverter',
        'SYNO.Core.MediaIndexing.Scheduler',
        'SYNO.Core.MediaIndexing.ThumbnailQuality',
        'SYNO.Core.MyDSCenter',
        'SYNO.Core.MyDSCenter.Account',
        'SYNO.Core.MyDSCenter.Login',
        'SYNO.Core.MyDSCenter.Logout',
        'SYNO.Core.MyDSCenter.Purchase',
        'SYNO.Core.NormalUser',
        'SYNO.Core.NormalUser.LoginNotify',
        'SYNO.Core.OAuth.Scope',
        'SYNO.Core.OAuth.Server',
        'SYNO.Core.Package.AutoUpgrade.Progress',
        'SYNO.Core.Package.Control',
        'SYNO.Core.Package.FakeIFrame',
        'SYNO.Core.Package.Feed',
        'SYNO.Core.Package.Legal.PreRelease',
        'SYNO.Core.Package.Log',
        'SYNO.Core.Package.MyDS',
        'SYNO.Core.Package.MyDS.Purchase',
        'SYNO.Core.Package.Progress',
        'SYNO.Core.Package.Screenshot',
        'SYNO.Core.Package.Screenshot.Server',
        'SYNO.Core.Package.Setting.Update',
        'SYNO.Core.Package.Thumb',
        'SYNO.Core.Package.Thumb.Server',
        'SYNO.Core.PersonalNotification.Device',
        'SYNO.Core.PersonalNotification.Event',
        'SYNO.Core.PersonalNotification.Filter',
        'SYNO.Core.PersonalNotification.Mobile',
        'SYNO.Core.PersonalNotification.Settings',
        'SYNO.Core.PhotoViewer',
        'SYNO.Core.PortForwarding',
        'SYNO.Core.PortForwarding.Compatibility',
        'SYNO.Core.PortForwarding.RouterInfo',
        'SYNO.Core.PortForwarding.RouterList',
        'SYNO.Core.PortForwarding.Rules.Serv',
        'SYNO.Core.Promotion.Info',
        'SYNO.Core.Promotion.PreInstall',
        'SYNO.Core.QuickConnect.Hostname',
        'SYNO.Core.QuickConnect.RegisterSite',
        'SYNO.Core.QuickConnect.SNI',
        'SYNO.Core.QuickConnect.Upnp',
        'SYNO.Core.QuickStart.Info',
        'SYNO.Core.QuickStart.Install',
        'SYNO.Core.Report',
        'SYNO.Core.Report.Analyzer',
        'SYNO.Core.Report.Analyzer.File',
        'SYNO.Core.Report.Analyzer.Share',
        'SYNO.Core.Report.Config',
        'SYNO.Core.Report.History',
        'SYNO.Core.Report.Redirect',
        'SYNO.Core.Report.Util',
        'SYNO.Core.ResetAdmin',
        'SYNO.Core.SecurityScan.Operation',
        'SYNO.Core.Service.Conf',
        'SYNO.Core.Service.PortInfo',
        'SYNO.Core.Share.Crypto',
        'SYNO.Core.Share.Crypto.Key',
        'SYNO.Core.Share.CryptoFile',
        'SYNO.Core.Share.KeyManager.AutoKey',
        'SYNO.Core.Share.KeyManager.Key',
        'SYNO.Core.Share.KeyManager.MachineKey',
        'SYNO.Core.Share.KeyManager.Store',
        'SYNO.Core.Share.Migration',
        'SYNO.Core.Share.Migration.Task',
        'SYNO.Core.Share.Permission',
        'SYNO.Core.Share.PermissionReport',
        'SYNO.Core.Share.ShellFile',
        'SYNO.Core.Sharing',
        'SYNO.Core.Sharing.Initdata',
        'SYNO.Core.Sharing.Login',
        'SYNO.Core.Sharing.Session',
        'SYNO.Core.SupportForm.Form',
        'SYNO.Core.SupportForm.Log',
        'SYNO.Core.SupportForm.Service',
        'SYNO.Core.Synohdpack',
        'SYNO.Core.SyslogClient.PersonalActivity',
        'SYNO.Core.Tuned',
        'SYNO.Core.User.Group',
        'SYNO.Core.User.PasswordExpiry',
        'SYNO.Core.User.PasswordMeter',
        'SYNO.Core.User.PasswordPolicy',
        'SYNO.Core.User.UsernamePolicy',
        'SYNO.Core.Virtualization.Host.Capability',
        'SYNO.Core.VolEncKeepKey',
        'SYNO.Core.Web.DSM.External',
        'SYNO.Core.Web.Security.HTTPCompression',
        'SYNO.Core.Web.Security.TLSProfile'
    }
        for ns in required:
            with self.subTest(namespace=ns):
                self.assertIn(f"'{ns}'", source)

    def test_method_count(self):
        """Verify expected number of public methods."""
        public = [m for m in dir(CoreService)
                  if not m.startswith('_') and callable(getattr(CoreService, m))
                  and m != 'logout']
        self.assertGreaterEqual(len(public), 184,
                                f"Expected 184+ methods, found {len(public)}")


if __name__ == '__main__':
    unittest.main()
