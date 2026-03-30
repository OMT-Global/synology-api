"""
Synology Core miscellaneous services API wrapper.

Covers the remaining SYNO.Core.* sub-namespaces not handled by the
dedicated core_security, core_network, core_notification, core_directory,
core_storage, core_upgrade, core_system, or core_external_device modules.
"""

from __future__ import annotations
import json
from typing import Optional
from . import base_api


class CoreService(base_api.BaseApi):
    """
    Catch-all Core API for miscellaneous SYNO.Core.* endpoints.

    Groups: ACL, ActionPriv, AppPortal, AppPriv, AppNotify, BackgroundTask,
    Backup.ED, BandwidthControl, CMS, Certificate extras, DDNS extras,
    DSMNotify extras, DataCollect, EW, Factory, File, FileServ extras,
    Findhost, Group extras, Hardware extras, ISCSI extras, MediaIndexing,
    MyDSCenter, NormalUser, OAuth, Package extras, PersonalNotification,
    PhotoViewer, PortForwarding, Promotion, QuickConnect extras,
    QuickStart, Report, ResetAdmin, SecurityScan, Service, Share extras,
    Sharing, SupportForm, Synohdpack, SyslogClient extras, Tuned,
    User extras, Virtualization, VolEncKeepKey, Web extras.
    """

    # ------------------------------------------------------------------
    # SYNO.Core.ACL
    # ------------------------------------------------------------------

    def acl_get(self, path: str) -> dict[str, object] | str:
        """Get ACL for a given path."""
        api_name = 'SYNO.Core.ACL'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get', 'path': path})

    def acl_set(self, path: str, acl: dict) -> dict[str, object] | str:
        """Set ACL for a given path."""
        api_name = 'SYNO.Core.ACL'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'set',
             'path': path, 'acl': json.dumps(acl)})

    # ------------------------------------------------------------------
    # SYNO.Core.ActionPriv / SYNO.Core.ActionPriv.Role
    # ------------------------------------------------------------------

    def action_priv_get(self) -> dict[str, object] | str:
        """Get action privilege settings."""
        api_name = 'SYNO.Core.ActionPriv'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def action_priv_role_get(self) -> dict[str, object] | str:
        """Get action privilege roles."""
        api_name = 'SYNO.Core.ActionPriv.Role'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def action_priv_role_set(self, roles: dict) -> dict[str, object] | str:
        """Set action privilege roles."""
        api_name = 'SYNO.Core.ActionPriv.Role'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'set',
             'roles': json.dumps(roles)})

    # ------------------------------------------------------------------
    # SYNO.Core.AppNotify
    # ------------------------------------------------------------------

    def app_notify_get(self) -> dict[str, object] | str:
        """Get application notification settings."""
        api_name = 'SYNO.Core.AppNotify'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.AppPortal / AccessControl / Config / ReverseProxy
    # ------------------------------------------------------------------

    def app_portal_get(self) -> dict[str, object] | str:
        """Get application portal settings."""
        api_name = 'SYNO.Core.AppPortal'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def app_portal_set(self, **kwargs) -> dict[str, object] | str:
        """Set application portal settings."""
        api_name = 'SYNO.Core.AppPortal'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    def app_portal_access_control_get(self) -> dict[str, object] | str:
        """Get application portal access control settings."""
        api_name = 'SYNO.Core.AppPortal.AccessControl'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def app_portal_access_control_set(self, **kwargs) -> dict[str, object] | str:
        """Set application portal access control settings."""
        api_name = 'SYNO.Core.AppPortal.AccessControl'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    def app_portal_config_get(self) -> dict[str, object] | str:
        """Get application portal configuration."""
        api_name = 'SYNO.Core.AppPortal.Config'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def app_portal_reverse_proxy_get(self) -> dict[str, object] | str:
        """Get reverse proxy rules for app portal."""
        api_name = 'SYNO.Core.AppPortal.ReverseProxy'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def app_portal_reverse_proxy_set(self, **kwargs) -> dict[str, object] | str:
        """Set reverse proxy rules for app portal."""
        api_name = 'SYNO.Core.AppPortal.ReverseProxy'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.AppPriv / App / Rule
    # ------------------------------------------------------------------

    def app_priv_get(self) -> dict[str, object] | str:
        """Get application privilege settings."""
        api_name = 'SYNO.Core.AppPriv'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def app_priv_app_get(self) -> dict[str, object] | str:
        """Get per-application privilege settings."""
        api_name = 'SYNO.Core.AppPriv.App'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def app_priv_rule_get(self) -> dict[str, object] | str:
        """Get application privilege rules."""
        api_name = 'SYNO.Core.AppPriv.Rule'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def app_priv_rule_set(self, rules: dict) -> dict[str, object] | str:
        """Set application privilege rules."""
        api_name = 'SYNO.Core.AppPriv.Rule'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'set',
             'rules': json.dumps(rules)})

    # ------------------------------------------------------------------
    # SYNO.Core.BackgroundTask
    # ------------------------------------------------------------------

    def background_task_list(self) -> dict[str, object] | str:
        """List all background tasks."""
        api_name = 'SYNO.Core.BackgroundTask'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'list'})

    def background_task_get(self, task_id: str) -> dict[str, object] | str:
        """Get a specific background task status."""
        api_name = 'SYNO.Core.BackgroundTask'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get', 'taskid': task_id})

    # ------------------------------------------------------------------
    # SYNO.Core.Backup.ED
    # ------------------------------------------------------------------

    def backup_ed_get(self) -> dict[str, object] | str:
        """Get encrypted data backup settings."""
        api_name = 'SYNO.Core.Backup.ED'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.BandwidthControl
    # ------------------------------------------------------------------

    def bandwidth_control_get(self) -> dict[str, object] | str:
        """Get bandwidth control settings."""
        api_name = 'SYNO.Core.BandwidthControl'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def bandwidth_control_set(self, **kwargs) -> dict[str, object] | str:
        """Set bandwidth control settings."""
        api_name = 'SYNO.Core.BandwidthControl'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.CMS (Central Management System)
    # ------------------------------------------------------------------

    def cms_get(self) -> dict[str, object] | str:
        """Get CMS settings."""
        api_name = 'SYNO.Core.CMS'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def cms_cache_get(self) -> dict[str, object] | str:
        """Get CMS cache information."""
        api_name = 'SYNO.Core.CMS.Cache'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def cms_identity_get(self) -> dict[str, object] | str:
        """Get CMS identity information."""
        api_name = 'SYNO.Core.CMS.Identity'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def cms_policy_get(self) -> dict[str, object] | str:
        """Get CMS policy settings."""
        api_name = 'SYNO.Core.CMS.Policy'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def cms_policy_set(self, **kwargs) -> dict[str, object] | str:
        """Set CMS policy."""
        api_name = 'SYNO.Core.CMS.Policy'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    def cms_server_info_get(self) -> dict[str, object] | str:
        """Get CMS server information."""
        api_name = 'SYNO.Core.CMS.ServerInfo'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def cms_task_get(self) -> dict[str, object] | str:
        """Get CMS task status."""
        api_name = 'SYNO.Core.CMS.Task'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def cms_token_get(self) -> dict[str, object] | str:
        """Get CMS authentication token."""
        api_name = 'SYNO.Core.CMS.Token'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.Certificate extras (CSR, LetsEncrypt, Tencent)
    # ------------------------------------------------------------------

    def certificate_csr_get(self) -> dict[str, object] | str:
        """Get certificate signing request settings."""
        api_name = 'SYNO.Core.Certificate.CSR'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def certificate_csr_create(self, **kwargs) -> dict[str, object] | str:
        """Create a certificate signing request."""
        api_name = 'SYNO.Core.Certificate.CSR'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'create'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    def certificate_letsencrypt_get(self) -> dict[str, object] | str:
        """Get Let's Encrypt certificate settings."""
        api_name = 'SYNO.Core.Certificate.LetsEncrypt'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def certificate_letsencrypt_create(self, **kwargs) -> dict[str, object] | str:
        """Create/renew a Let's Encrypt certificate."""
        api_name = 'SYNO.Core.Certificate.LetsEncrypt'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'create'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    def certificate_letsencrypt_account_get(self) -> dict[str, object] | str:
        """Get Let's Encrypt account information."""
        api_name = 'SYNO.Core.Certificate.LetsEncrypt.Account'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def certificate_tencent_get(self) -> dict[str, object] | str:
        """Get Tencent SSL certificate settings."""
        api_name = 'SYNO.Core.Certificate.Tencent'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.DDNS extras (Ethernet, TWNIC)
    # ------------------------------------------------------------------

    def ddns_ethernet_get(self) -> dict[str, object] | str:
        """Get DDNS ethernet interface settings."""
        api_name = 'SYNO.Core.DDNS.Ethernet'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def ddns_twnic_get(self) -> dict[str, object] | str:
        """Get TWNIC DDNS settings."""
        api_name = 'SYNO.Core.DDNS.TWNIC'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.DSMNotify extras
    # ------------------------------------------------------------------

    def dsm_notify_mail_content_get(self) -> dict[str, object] | str:
        """Get DSM notification mail content templates."""
        api_name = 'SYNO.Core.DSMNotify.MailContent'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def dsm_notify_strings_get(self) -> dict[str, object] | str:
        """Get DSM notification strings."""
        api_name = 'SYNO.Core.DSMNotify.Strings'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.DataCollect / Application
    # ------------------------------------------------------------------

    def data_collect_get(self) -> dict[str, object] | str:
        """Get data collection settings."""
        api_name = 'SYNO.Core.DataCollect'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def data_collect_set(self, enabled: bool = True) -> dict[str, object] | str:
        """Set data collection settings."""
        api_name = 'SYNO.Core.DataCollect'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'set',
             'enabled': json.dumps(enabled)})

    def data_collect_application_get(self) -> dict[str, object] | str:
        """Get per-application data collection settings."""
        api_name = 'SYNO.Core.DataCollect.Application'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.EW.Info
    # ------------------------------------------------------------------

    def ew_info_get(self) -> dict[str, object] | str:
        """Get extended warranty information."""
        api_name = 'SYNO.Core.EW.Info'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.Factory
    # ------------------------------------------------------------------

    def factory_config_get(self) -> dict[str, object] | str:
        """Get factory configuration."""
        api_name = 'SYNO.Core.Factory.Config'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def factory_manutild_get(self) -> dict[str, object] | str:
        """Get factory manufacturing settings."""
        api_name = 'SYNO.Core.Factory.Manutild'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.File / Thumbnail
    # ------------------------------------------------------------------

    def file_get(self, path: str) -> dict[str, object] | str:
        """Get file information."""
        api_name = 'SYNO.Core.File'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get', 'path': path})

    def file_thumbnail_get(self, path: str, size: str = 'small') -> dict[str, object] | str:
        """Get file thumbnail."""
        api_name = 'SYNO.Core.File.Thumbnail'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get',
             'path': path, 'size': size})

    # ------------------------------------------------------------------
    # SYNO.Core.FileServ NFS/Rsync/SMB extras
    # ------------------------------------------------------------------

    def fileserv_nfs_advanced_get(self) -> dict[str, object] | str:
        """Get NFS advanced settings."""
        api_name = 'SYNO.Core.FileServ.NFS.AdvancedSetting'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def fileserv_nfs_advanced_set(self, **kwargs) -> dict[str, object] | str:
        """Set NFS advanced settings."""
        api_name = 'SYNO.Core.FileServ.NFS.AdvancedSetting'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    def fileserv_nfs_conf_backup_get(self) -> dict[str, object] | str:
        """Get NFS configuration backup."""
        api_name = 'SYNO.Core.FileServ.NFS.ConfBackup'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def fileserv_nfs_idmap_get(self) -> dict[str, object] | str:
        """Get NFS ID mapping settings."""
        api_name = 'SYNO.Core.FileServ.NFS.IDMap'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def fileserv_nfs_kerberos_get(self) -> dict[str, object] | str:
        """Get NFS Kerberos settings."""
        api_name = 'SYNO.Core.FileServ.NFS.Kerberos'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def fileserv_nfs_share_privilege_get(self) -> dict[str, object] | str:
        """Get NFS share privileges."""
        api_name = 'SYNO.Core.FileServ.NFS.SharePrivilege'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def fileserv_rsync_account_get(self) -> dict[str, object] | str:
        """Get rsync account settings."""
        api_name = 'SYNO.Core.FileServ.Rsync.Account'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def fileserv_rsync_account_set(self, **kwargs) -> dict[str, object] | str:
        """Set rsync account settings."""
        api_name = 'SYNO.Core.FileServ.Rsync.Account'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    def fileserv_smb_conf_backup_get(self) -> dict[str, object] | str:
        """Get SMB configuration backup."""
        api_name = 'SYNO.Core.FileServ.SMB.ConfBackup'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def fileserv_smb_control_get(self) -> dict[str, object] | str:
        """Get SMB control settings."""
        api_name = 'SYNO.Core.FileServ.SMB.Control'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def fileserv_smb_msdfs_get(self) -> dict[str, object] | str:
        """Get SMB MS-DFS settings."""
        api_name = 'SYNO.Core.FileServ.SMB.MSDFS'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.Findhost
    # ------------------------------------------------------------------

    def findhost_get(self) -> dict[str, object] | str:
        """Get find-host settings."""
        api_name = 'SYNO.Core.Findhost'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.Group extras
    # ------------------------------------------------------------------

    def group_extra_admin_get(self) -> dict[str, object] | str:
        """Get extra admin group settings."""
        api_name = 'SYNO.Core.Group.ExtraAdmin'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def group_member_list(self, group: str) -> dict[str, object] | str:
        """List members of a group."""
        api_name = 'SYNO.Core.Group.Member'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'list', 'group': group})

    def group_valid_local_admin_get(self) -> dict[str, object] | str:
        """Get valid local admin information."""
        api_name = 'SYNO.Core.Group.ValidLocalAdmin'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.Hardware extras
    # ------------------------------------------------------------------

    def hardware_lcm_get(self) -> dict[str, object] | str:
        """Get LCD monitor panel settings."""
        api_name = 'SYNO.Core.Hardware.LCM'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def hardware_led_brightness_get(self) -> dict[str, object] | str:
        """Get LED brightness settings."""
        api_name = 'SYNO.Core.Hardware.Led.Brightness'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def hardware_led_brightness_set(self, brightness: int) -> dict[str, object] | str:
        """Set LED brightness level."""
        api_name = 'SYNO.Core.Hardware.Led.Brightness'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'set',
             'brightness': brightness})

    def hardware_memory_layout_get(self) -> dict[str, object] | str:
        """Get memory layout information."""
        api_name = 'SYNO.Core.Hardware.MemoryLayout'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def hardware_need_reboot_get(self) -> dict[str, object] | str:
        """Check if a reboot is required."""
        api_name = 'SYNO.Core.Hardware.NeedReboot'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def hardware_oob_management_get(self) -> dict[str, object] | str:
        """Get out-of-band management (IPMI/BMC) settings."""
        api_name = 'SYNO.Core.Hardware.OOBManagement'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def hardware_remote_fan_status_get(self) -> dict[str, object] | str:
        """Get remote fan status."""
        api_name = 'SYNO.Core.Hardware.RemoteFanStatus'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def hardware_spectre_meltdown_get(self) -> dict[str, object] | str:
        """Get Spectre/Meltdown mitigation status."""
        api_name = 'SYNO.Core.Hardware.SpectreMeltdown'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def hardware_video_transcoding_get(self) -> dict[str, object] | str:
        """Get hardware video transcoding capability."""
        api_name = 'SYNO.Core.Hardware.VideoTranscoding'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.ISCSI extras
    # ------------------------------------------------------------------

    def iscsi_fc_target_get(self) -> dict[str, object] | str:
        """Get Fibre Channel target settings."""
        api_name = 'SYNO.Core.ISCSI.FCTarget'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def iscsi_host_get(self) -> dict[str, object] | str:
        """Get iSCSI host settings."""
        api_name = 'SYNO.Core.ISCSI.Host'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def iscsi_lunbkp_get(self) -> dict[str, object] | str:
        """Get iSCSI LUN backup settings."""
        api_name = 'SYNO.Core.ISCSI.Lunbkp'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def iscsi_node_get(self) -> dict[str, object] | str:
        """Get iSCSI node information."""
        api_name = 'SYNO.Core.ISCSI.Node'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def iscsi_replication_get(self) -> dict[str, object] | str:
        """Get iSCSI replication settings."""
        api_name = 'SYNO.Core.ISCSI.Replication'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def iscsi_vmware_get(self) -> dict[str, object] | str:
        """Get iSCSI VMware integration settings."""
        api_name = 'SYNO.Core.ISCSI.VMware'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.MediaIndexing
    # ------------------------------------------------------------------

    def media_indexing_get(self) -> dict[str, object] | str:
        """Get media indexing settings."""
        api_name = 'SYNO.Core.MediaIndexing'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def media_indexing_set(self, **kwargs) -> dict[str, object] | str:
        """Set media indexing settings."""
        api_name = 'SYNO.Core.MediaIndexing'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    def media_indexing_index_folder_get(self) -> dict[str, object] | str:
        """Get indexed folder list."""
        api_name = 'SYNO.Core.MediaIndexing.IndexFolder'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def media_indexing_media_converter_get(self) -> dict[str, object] | str:
        """Get media converter settings."""
        api_name = 'SYNO.Core.MediaIndexing.MediaConverter'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def media_indexing_scheduler_get(self) -> dict[str, object] | str:
        """Get media indexing scheduler settings."""
        api_name = 'SYNO.Core.MediaIndexing.Scheduler'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def media_indexing_thumbnail_quality_get(self) -> dict[str, object] | str:
        """Get thumbnail quality settings."""
        api_name = 'SYNO.Core.MediaIndexing.ThumbnailQuality'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.MyDSCenter
    # ------------------------------------------------------------------

    def mydscenter_get(self) -> dict[str, object] | str:
        """Get MyDS Center settings."""
        api_name = 'SYNO.Core.MyDSCenter'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def mydscenter_account_get(self) -> dict[str, object] | str:
        """Get MyDS Center account information."""
        api_name = 'SYNO.Core.MyDSCenter.Account'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def mydscenter_login(self, username: str, password: str) -> dict[str, object] | str:
        """Login to MyDS Center."""
        api_name = 'SYNO.Core.MyDSCenter.Login'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'login',
             'username': username, 'password': password}, method='post')

    def mydscenter_logout(self) -> dict[str, object] | str:
        """Logout from MyDS Center."""
        api_name = 'SYNO.Core.MyDSCenter.Logout'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'logout'})

    def mydscenter_purchase_get(self) -> dict[str, object] | str:
        """Get MyDS Center purchase information."""
        api_name = 'SYNO.Core.MyDSCenter.Purchase'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.NormalUser
    # ------------------------------------------------------------------

    def normal_user_get(self) -> dict[str, object] | str:
        """Get normal user settings."""
        api_name = 'SYNO.Core.NormalUser'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def normal_user_login_notify_get(self) -> dict[str, object] | str:
        """Get normal user login notification settings."""
        api_name = 'SYNO.Core.NormalUser.LoginNotify'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.OAuth
    # ------------------------------------------------------------------

    def oauth_scope_get(self) -> dict[str, object] | str:
        """Get OAuth scope settings."""
        api_name = 'SYNO.Core.OAuth.Scope'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def oauth_server_get(self) -> dict[str, object] | str:
        """Get OAuth server settings."""
        api_name = 'SYNO.Core.OAuth.Server'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def oauth_server_set(self, **kwargs) -> dict[str, object] | str:
        """Set OAuth server settings."""
        api_name = 'SYNO.Core.OAuth.Server'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.Package extras
    # ------------------------------------------------------------------

    def package_auto_upgrade_progress_get(self) -> dict[str, object] | str:
        """Get package auto-upgrade progress."""
        api_name = 'SYNO.Core.Package.AutoUpgrade.Progress'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def package_control(self, package_id: str, action: str) -> dict[str, object] | str:
        """Control a package (start/stop)."""
        api_name = 'SYNO.Core.Package.Control'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': action, 'id': package_id})

    def package_fake_iframe_get(self) -> dict[str, object] | str:
        """Get package fake iframe info."""
        api_name = 'SYNO.Core.Package.FakeIFrame'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def package_feed_list(self) -> dict[str, object] | str:
        """List package feeds."""
        api_name = 'SYNO.Core.Package.Feed'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'list'})

    def package_feed_set(self, **kwargs) -> dict[str, object] | str:
        """Set package feed settings."""
        api_name = 'SYNO.Core.Package.Feed'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    def package_legal_prerelease_get(self) -> dict[str, object] | str:
        """Get package pre-release legal agreement status."""
        api_name = 'SYNO.Core.Package.Legal.PreRelease'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def package_log_get(self, package_id: Optional[str] = None) -> dict[str, object] | str:
        """Get package log entries."""
        api_name = 'SYNO.Core.Package.Log'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'get'}
        if package_id:
            req_param['id'] = package_id
        return self.request_data(api_name, info['path'], req_param)

    def package_myds_get(self) -> dict[str, object] | str:
        """Get MyDS package info."""
        api_name = 'SYNO.Core.Package.MyDS'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def package_myds_purchase_get(self) -> dict[str, object] | str:
        """Get MyDS package purchase info."""
        api_name = 'SYNO.Core.Package.MyDS.Purchase'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def package_progress_get(self, task_id: Optional[str] = None) -> dict[str, object] | str:
        """Get package installation/upgrade progress."""
        api_name = 'SYNO.Core.Package.Progress'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'get'}
        if task_id:
            req_param['taskid'] = task_id
        return self.request_data(api_name, info['path'], req_param)

    def package_screenshot_get(self, package_id: str) -> dict[str, object] | str:
        """Get package screenshots."""
        api_name = 'SYNO.Core.Package.Screenshot'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get', 'id': package_id})

    def package_screenshot_server_get(self, package_id: str) -> dict[str, object] | str:
        """Get package screenshot from server."""
        api_name = 'SYNO.Core.Package.Screenshot.Server'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get', 'id': package_id})

    def package_setting_update_get(self) -> dict[str, object] | str:
        """Get package update settings."""
        api_name = 'SYNO.Core.Package.Setting.Update'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def package_thumb_get(self, package_id: str) -> dict[str, object] | str:
        """Get package thumbnail."""
        api_name = 'SYNO.Core.Package.Thumb'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get', 'id': package_id})

    def package_thumb_server_get(self, package_id: str) -> dict[str, object] | str:
        """Get package thumbnail from server."""
        api_name = 'SYNO.Core.Package.Thumb.Server'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get', 'id': package_id})

    # ------------------------------------------------------------------
    # SYNO.Core.PersonalNotification
    # ------------------------------------------------------------------

    def personal_notification_device_get(self) -> dict[str, object] | str:
        """Get personal notification device settings."""
        api_name = 'SYNO.Core.PersonalNotification.Device'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def personal_notification_event_get(self) -> dict[str, object] | str:
        """Get personal notification events."""
        api_name = 'SYNO.Core.PersonalNotification.Event'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def personal_notification_filter_get(self) -> dict[str, object] | str:
        """Get personal notification filter settings."""
        api_name = 'SYNO.Core.PersonalNotification.Filter'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def personal_notification_filter_set(self, **kwargs) -> dict[str, object] | str:
        """Set personal notification filter settings."""
        api_name = 'SYNO.Core.PersonalNotification.Filter'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    def personal_notification_mobile_get(self) -> dict[str, object] | str:
        """Get personal notification mobile settings."""
        api_name = 'SYNO.Core.PersonalNotification.Mobile'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def personal_notification_settings_get(self) -> dict[str, object] | str:
        """Get personal notification settings."""
        api_name = 'SYNO.Core.PersonalNotification.Settings'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def personal_notification_settings_set(self, **kwargs) -> dict[str, object] | str:
        """Set personal notification settings."""
        api_name = 'SYNO.Core.PersonalNotification.Settings'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.PhotoViewer
    # ------------------------------------------------------------------

    def photo_viewer_get(self) -> dict[str, object] | str:
        """Get photo viewer settings."""
        api_name = 'SYNO.Core.PhotoViewer'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.PortForwarding extras
    # ------------------------------------------------------------------

    def port_forwarding_get(self) -> dict[str, object] | str:
        """Get port forwarding settings."""
        api_name = 'SYNO.Core.PortForwarding'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def port_forwarding_compatibility_get(self) -> dict[str, object] | str:
        """Get port forwarding compatibility status."""
        api_name = 'SYNO.Core.PortForwarding.Compatibility'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def port_forwarding_router_info_get(self) -> dict[str, object] | str:
        """Get router information for port forwarding."""
        api_name = 'SYNO.Core.PortForwarding.RouterInfo'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def port_forwarding_router_list(self) -> dict[str, object] | str:
        """List detected routers."""
        api_name = 'SYNO.Core.PortForwarding.RouterList'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def port_forwarding_rules_serv_get(self) -> dict[str, object] | str:
        """Get service-based port forwarding rules."""
        api_name = 'SYNO.Core.PortForwarding.Rules.Serv'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.Promotion
    # ------------------------------------------------------------------

    def promotion_info_get(self) -> dict[str, object] | str:
        """Get Synology promotion information."""
        api_name = 'SYNO.Core.Promotion.Info'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def promotion_preinstall_get(self) -> dict[str, object] | str:
        """Get pre-install promotion information."""
        api_name = 'SYNO.Core.Promotion.PreInstall'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.QuickConnect extras
    # ------------------------------------------------------------------

    def quickconnect_hostname_get(self) -> dict[str, object] | str:
        """Get QuickConnect hostname settings."""
        api_name = 'SYNO.Core.QuickConnect.Hostname'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def quickconnect_register_site_get(self) -> dict[str, object] | str:
        """Get QuickConnect registration site info."""
        api_name = 'SYNO.Core.QuickConnect.RegisterSite'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def quickconnect_sni_get(self) -> dict[str, object] | str:
        """Get QuickConnect SNI settings."""
        api_name = 'SYNO.Core.QuickConnect.SNI'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def quickconnect_upnp_get(self) -> dict[str, object] | str:
        """Get QuickConnect UPnP settings."""
        api_name = 'SYNO.Core.QuickConnect.Upnp'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.QuickStart
    # ------------------------------------------------------------------

    def quickstart_info_get(self) -> dict[str, object] | str:
        """Get quick start wizard information."""
        api_name = 'SYNO.Core.QuickStart.Info'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def quickstart_install(self, **kwargs) -> dict[str, object] | str:
        """Run quick start installation."""
        api_name = 'SYNO.Core.QuickStart.Install'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'start'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.Report
    # ------------------------------------------------------------------

    def report_get(self) -> dict[str, object] | str:
        """Get report settings."""
        api_name = 'SYNO.Core.Report'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def report_analyzer_get(self) -> dict[str, object] | str:
        """Get report analyzer settings."""
        api_name = 'SYNO.Core.Report.Analyzer'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def report_analyzer_file_get(self) -> dict[str, object] | str:
        """Get report analyzer file info."""
        api_name = 'SYNO.Core.Report.Analyzer.File'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def report_analyzer_share_get(self) -> dict[str, object] | str:
        """Get report analyzer share info."""
        api_name = 'SYNO.Core.Report.Analyzer.Share'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def report_config_get(self) -> dict[str, object] | str:
        """Get report configuration."""
        api_name = 'SYNO.Core.Report.Config'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def report_config_set(self, **kwargs) -> dict[str, object] | str:
        """Set report configuration."""
        api_name = 'SYNO.Core.Report.Config'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    def report_history_get(self) -> dict[str, object] | str:
        """Get report history."""
        api_name = 'SYNO.Core.Report.History'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def report_redirect_get(self) -> dict[str, object] | str:
        """Get report redirect settings."""
        api_name = 'SYNO.Core.Report.Redirect'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def report_util_get(self) -> dict[str, object] | str:
        """Get report utility information."""
        api_name = 'SYNO.Core.Report.Util'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.ResetAdmin
    # ------------------------------------------------------------------

    def reset_admin_get(self) -> dict[str, object] | str:
        """Get admin reset status."""
        api_name = 'SYNO.Core.ResetAdmin'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.SecurityScan.Operation
    # ------------------------------------------------------------------

    def security_scan_operation_start(self) -> dict[str, object] | str:
        """Start a security scan."""
        api_name = 'SYNO.Core.SecurityScan.Operation'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'start'})

    def security_scan_operation_get(self) -> dict[str, object] | str:
        """Get security scan operation status."""
        api_name = 'SYNO.Core.SecurityScan.Operation'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.Service extras
    # ------------------------------------------------------------------

    def service_conf_get(self) -> dict[str, object] | str:
        """Get service configuration."""
        api_name = 'SYNO.Core.Service.Conf'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def service_conf_set(self, **kwargs) -> dict[str, object] | str:
        """Set service configuration."""
        api_name = 'SYNO.Core.Service.Conf'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    def service_port_info_get(self) -> dict[str, object] | str:
        """Get service port information."""
        api_name = 'SYNO.Core.Service.PortInfo'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.Share extras (Crypto, KeyManager, Migration, Permission)
    # ------------------------------------------------------------------

    def share_crypto_get(self) -> dict[str, object] | str:
        """Get shared folder encryption settings."""
        api_name = 'SYNO.Core.Share.Crypto'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def share_crypto_key_get(self) -> dict[str, object] | str:
        """Get shared folder encryption key info."""
        api_name = 'SYNO.Core.Share.Crypto.Key'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def share_crypto_file_get(self) -> dict[str, object] | str:
        """Get encrypted shared folder file settings."""
        api_name = 'SYNO.Core.Share.CryptoFile'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def share_key_manager_auto_key_get(self) -> dict[str, object] | str:
        """Get key manager auto-key settings."""
        api_name = 'SYNO.Core.Share.KeyManager.AutoKey'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def share_key_manager_key_get(self) -> dict[str, object] | str:
        """Get key manager key settings."""
        api_name = 'SYNO.Core.Share.KeyManager.Key'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def share_key_manager_machine_key_get(self) -> dict[str, object] | str:
        """Get key manager machine key settings."""
        api_name = 'SYNO.Core.Share.KeyManager.MachineKey'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def share_key_manager_store_get(self) -> dict[str, object] | str:
        """Get key manager store settings."""
        api_name = 'SYNO.Core.Share.KeyManager.Store'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def share_migration_get(self) -> dict[str, object] | str:
        """Get shared folder migration status."""
        api_name = 'SYNO.Core.Share.Migration'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def share_migration_task_get(self) -> dict[str, object] | str:
        """Get shared folder migration task status."""
        api_name = 'SYNO.Core.Share.Migration.Task'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def share_permission_get(self, name: str) -> dict[str, object] | str:
        """Get permissions for a shared folder."""
        api_name = 'SYNO.Core.Share.Permission'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get', 'name': name})

    def share_permission_set(self, name: str, permissions: dict) -> dict[str, object] | str:
        """Set permissions for a shared folder."""
        api_name = 'SYNO.Core.Share.Permission'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'set',
             'name': name, 'user_group_type_list': json.dumps(permissions)})

    def share_permission_report_get(self) -> dict[str, object] | str:
        """Get shared folder permission report."""
        api_name = 'SYNO.Core.Share.PermissionReport'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def share_shell_file_get(self) -> dict[str, object] | str:
        """Get shared folder shell file settings."""
        api_name = 'SYNO.Core.Share.ShellFile'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.Sharing
    # ------------------------------------------------------------------

    def sharing_get(self) -> dict[str, object] | str:
        """Get file sharing settings."""
        api_name = 'SYNO.Core.Sharing'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def sharing_initdata_get(self) -> dict[str, object] | str:
        """Get sharing initialization data."""
        api_name = 'SYNO.Core.Sharing.Initdata'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def sharing_login(self, sharing_id: str, password: Optional[str] = None) -> dict[str, object] | str:
        """Login to a file sharing link."""
        api_name = 'SYNO.Core.Sharing.Login'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'login',
                     'sharing_id': sharing_id}
        if password:
            req_param['password'] = password
        return self.request_data(api_name, info['path'], req_param)

    def sharing_session_get(self) -> dict[str, object] | str:
        """Get sharing session information."""
        api_name = 'SYNO.Core.Sharing.Session'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.SupportForm
    # ------------------------------------------------------------------

    def support_form_get(self) -> dict[str, object] | str:
        """Get support form configuration."""
        api_name = 'SYNO.Core.SupportForm.Form'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def support_form_log_get(self) -> dict[str, object] | str:
        """Get support form submission log."""
        api_name = 'SYNO.Core.SupportForm.Log'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def support_form_service_get(self) -> dict[str, object] | str:
        """Get support form service status."""
        api_name = 'SYNO.Core.SupportForm.Service'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.Synohdpack
    # ------------------------------------------------------------------

    def synohdpack_get(self) -> dict[str, object] | str:
        """Get Synology HD pack information."""
        api_name = 'SYNO.Core.Synohdpack'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.SyslogClient.PersonalActivity
    # ------------------------------------------------------------------

    def syslog_personal_activity_get(self) -> dict[str, object] | str:
        """Get personal activity syslog settings."""
        api_name = 'SYNO.Core.SyslogClient.PersonalActivity'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.Tuned
    # ------------------------------------------------------------------

    def tuned_get(self) -> dict[str, object] | str:
        """Get system tuning (tuned) settings."""
        api_name = 'SYNO.Core.Tuned'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def tuned_set(self, **kwargs) -> dict[str, object] | str:
        """Set system tuning settings."""
        api_name = 'SYNO.Core.Tuned'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.User extras
    # ------------------------------------------------------------------

    def user_group_get(self, user: str) -> dict[str, object] | str:
        """Get groups a user belongs to."""
        api_name = 'SYNO.Core.User.Group'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get', 'name': user})

    def user_password_expiry_get(self) -> dict[str, object] | str:
        """Get password expiry settings."""
        api_name = 'SYNO.Core.User.PasswordExpiry'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def user_password_meter_get(self, password: str) -> dict[str, object] | str:
        """Check password strength."""
        api_name = 'SYNO.Core.User.PasswordMeter'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get',
             'password': password}, method='post')

    def user_password_policy_get(self) -> dict[str, object] | str:
        """Get password policy settings."""
        api_name = 'SYNO.Core.User.PasswordPolicy'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def user_password_policy_set(self, **kwargs) -> dict[str, object] | str:
        """Set password policy settings."""
        api_name = 'SYNO.Core.User.PasswordPolicy'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    def user_username_policy_get(self) -> dict[str, object] | str:
        """Get username policy settings."""
        api_name = 'SYNO.Core.User.UsernamePolicy'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.Virtualization.Host.Capability
    # ------------------------------------------------------------------

    def virtualization_host_capability_get(self) -> dict[str, object] | str:
        """Get virtualization host capability information."""
        api_name = 'SYNO.Core.Virtualization.Host.Capability'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.VolEncKeepKey
    # ------------------------------------------------------------------

    def vol_enc_keep_key_get(self) -> dict[str, object] | str:
        """Get volume encryption keep-key settings."""
        api_name = 'SYNO.Core.VolEncKeepKey'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def vol_enc_keep_key_set(self, **kwargs) -> dict[str, object] | str:
        """Set volume encryption keep-key settings."""
        api_name = 'SYNO.Core.VolEncKeepKey'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.Web extras
    # ------------------------------------------------------------------

    def web_dsm_external_get(self) -> dict[str, object] | str:
        """Get DSM external web access settings."""
        api_name = 'SYNO.Core.Web.DSM.External'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def web_dsm_external_set(self, **kwargs) -> dict[str, object] | str:
        """Set DSM external web access settings."""
        api_name = 'SYNO.Core.Web.DSM.External'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    def web_security_http_compression_get(self) -> dict[str, object] | str:
        """Get HTTP compression settings."""
        api_name = 'SYNO.Core.Web.Security.HTTPCompression'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def web_security_http_compression_set(self, **kwargs) -> dict[str, object] | str:
        """Set HTTP compression settings."""
        api_name = 'SYNO.Core.Web.Security.HTTPCompression'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    def web_security_tls_profile_get(self) -> dict[str, object] | str:
        """Get TLS profile settings."""
        api_name = 'SYNO.Core.Web.Security.TLSProfile'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
            {'version': info['maxVersion'], 'method': 'get'})

    def web_security_tls_profile_set(self, **kwargs) -> dict[str, object] | str:
        """Set TLS profile settings."""
        api_name = 'SYNO.Core.Web.Security.TLSProfile'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)
