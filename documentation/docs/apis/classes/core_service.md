---
sidebar_position: 14
title: 🚧 CoreService
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# CoreService
:::warning
 
This API is partially documented or under construction.
 
:::
## Overview
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
  
## Methods
### `acl_get`
Get ACL for a given path.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ACL`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_path_** `str`  
The path value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the acl get operation.  
</div>
  



---


### `acl_set`
Set ACL for a given path.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ACL`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_path_** `str`  
The path value.  
  
**_acl_** `dict`  
The acl value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the acl set operation.  
</div>
  



---


### `action_priv_get`
Get action privilege settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ActionPriv`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the action priv get operation.  
</div>
  



---


### `action_priv_role_get`
Get action privilege roles.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ActionPriv.Role`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the action priv role get operation.  
</div>
  



---


### `action_priv_role_set`
Set action privilege roles.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ActionPriv.Role`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_roles_** `dict`  
The roles value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the action priv role set operation.  
</div>
  



---


### `app_notify_get`
Get application notification settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.AppNotify`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the app notify get operation.  
</div>
  



---


### `app_portal_get`
Get application portal settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.AppPortal`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the app portal get operation.  
</div>
  



---


### `app_portal_set`
Set application portal settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.AppPortal`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `dict`  
Additional keyword arguments forwarded to the API.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the app portal set operation.  
</div>
  



---


### `app_portal_access_control_get`
Get application portal access control settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.AppPortal.AccessControl`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the app portal access control get operation.  
</div>
  



---


### `app_portal_access_control_set`
Set application portal access control settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.AppPortal.AccessControl`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `dict`  
Additional keyword arguments forwarded to the API.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the app portal access control set operation.  
</div>
  



---


### `app_portal_config_get`
Get application portal configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.AppPortal.Config`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the app portal config get operation.  
</div>
  



---


### `app_portal_reverse_proxy_get`
Get reverse proxy rules for app portal.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.AppPortal.ReverseProxy`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the app portal reverse proxy get operation.  
</div>
  



---


### `app_portal_reverse_proxy_set`
Set reverse proxy rules for app portal.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.AppPortal.ReverseProxy`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `dict`  
Additional keyword arguments forwarded to the API.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the app portal reverse proxy set operation.  
</div>
  



---


### `app_priv_get`
Get application privilege settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.AppPriv`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the app priv get operation.  
</div>
  



---


### `app_priv_app_get`
Get per-application privilege settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.AppPriv.App`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the app priv app get operation.  
</div>
  



---


### `app_priv_rule_get`
Get application privilege rules.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.AppPriv.Rule`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the app priv rule get operation.  
</div>
  



---


### `app_priv_rule_set`
Set application privilege rules.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.AppPriv.Rule`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_rules_** `dict`  
The rules value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the app priv rule set operation.  
</div>
  



---


### `background_task_list`
List all background tasks.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.BackgroundTask`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the background task list operation.  
</div>
  



---


### `background_task_get`
Get a specific background task status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.BackgroundTask`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_task_id_** `str`  
The task id value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the background task get operation.  
</div>
  



---


### `backup_ed_get`
Get encrypted data backup settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Backup.ED`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the backup ed get operation.  
</div>
  



---


### `bandwidth_control_get`
Get bandwidth control settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.BandwidthControl`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the bandwidth control get operation.  
</div>
  



---


### `bandwidth_control_set`
Set bandwidth control settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.BandwidthControl`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `dict`  
Additional keyword arguments forwarded to the API.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the bandwidth control set operation.  
</div>
  



---


### `cms_get`
Get CMS settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.CMS`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the cms get operation.  
</div>
  



---


### `cms_cache_get`
Get CMS cache information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.CMS.Cache`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the cms cache get operation.  
</div>
  



---


### `cms_identity_get`
Get CMS identity information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.CMS.Identity`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the cms identity get operation.  
</div>
  



---


### `cms_policy_get`
Get CMS policy settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.CMS.Policy`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the cms policy get operation.  
</div>
  



---


### `cms_policy_set`
Set CMS policy.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.CMS.Policy`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `dict`  
Additional keyword arguments forwarded to the API.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the cms policy set operation.  
</div>
  



---


### `cms_server_info_get`
Get CMS server information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.CMS.ServerInfo`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the cms server info get operation.  
</div>
  



---


### `cms_task_get`
Get CMS task status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.CMS.Task`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the cms task get operation.  
</div>
  



---


### `cms_token_get`
Get CMS authentication token.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.CMS.Token`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the cms token get operation.  
</div>
  



---


### `certificate_csr_get`
Get certificate signing request settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Certificate.CSR`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the certificate csr get operation.  
</div>
  



---


### `certificate_csr_create`
Create a certificate signing request.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Certificate.CSR`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `dict`  
Additional keyword arguments forwarded to the API.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the certificate csr create operation.  
</div>
  



---


### `certificate_letsencrypt_get`
Get Let's Encrypt certificate settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Certificate.LetsEncrypt`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the certificate letsencrypt get operation.  
</div>
  



---


### `certificate_letsencrypt_create`
Create/renew a Let's Encrypt certificate.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Certificate.LetsEncrypt`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `dict`  
Additional keyword arguments forwarded to the API.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the certificate letsencrypt create operation.  
</div>
  



---


### `certificate_letsencrypt_account_get`
Get Let's Encrypt account information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Certificate.LetsEncrypt.Account`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the certificate letsencrypt account get operation.  
</div>
  



---


### `certificate_tencent_get`
Get Tencent SSL certificate settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Certificate.Tencent`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the certificate tencent get operation.  
</div>
  



---


### `ddns_ethernet_get`
Get DDNS ethernet interface settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.DDNS.Ethernet`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the ddns ethernet get operation.  
</div>
  



---


### `ddns_twnic_get`
Get TWNIC DDNS settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.DDNS.TWNIC`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the ddns twnic get operation.  
</div>
  



---


### `dsm_notify_mail_content_get`
Get DSM notification mail content templates.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.DSMNotify.MailContent`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the dsm notify mail content get operation.  
</div>
  



---


### `dsm_notify_strings_get`
Get DSM notification strings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.DSMNotify.Strings`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the dsm notify strings get operation.  
</div>
  



---


### `data_collect_get`
Get data collection settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.DataCollect`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the data collect get operation.  
</div>
  



---


### `data_collect_set`
Set data collection settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.DataCollect`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_enabled_** `bool`  
The enabled value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the data collect set operation.  
</div>
  



---


### `data_collect_application_get`
Get per-application data collection settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.DataCollect.Application`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the data collect application get operation.  
</div>
  



---


### `ew_info_get`
Get extended warranty information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.EW.Info`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the ew info get operation.  
</div>
  



---


### `factory_config_get`
Get factory configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Factory.Config`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the factory config get operation.  
</div>
  



---


### `factory_manutild_get`
Get factory manufacturing settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Factory.Manutild`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the factory manutild get operation.  
</div>
  



---


### `file_get`
Get file information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.File`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_path_** `str`  
The path value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the file get operation.  
</div>
  



---


### `file_thumbnail_get`
Get file thumbnail.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.File.Thumbnail`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_path_** `str`  
The path value.  
  
**_size_** `str`  
The size value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the file thumbnail get operation.  
</div>
  



---


### `fileserv_nfs_advanced_get`
Get NFS advanced settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.FileServ.NFS.AdvancedSetting`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the fileserv nfs advanced get operation.  
</div>
  



---


### `fileserv_nfs_advanced_set`
Set NFS advanced settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.FileServ.NFS.AdvancedSetting`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `dict`  
Additional keyword arguments forwarded to the API.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the fileserv nfs advanced set operation.  
</div>
  



---


### `fileserv_nfs_conf_backup_get`
Get NFS configuration backup.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.FileServ.NFS.ConfBackup`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the fileserv nfs conf backup get operation.  
</div>
  



---


### `fileserv_nfs_idmap_get`
Get NFS ID mapping settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.FileServ.NFS.IDMap`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the fileserv nfs idmap get operation.  
</div>
  



---


### `fileserv_nfs_kerberos_get`
Get NFS Kerberos settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.FileServ.NFS.Kerberos`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the fileserv nfs kerberos get operation.  
</div>
  



---


### `fileserv_nfs_share_privilege_get`
Get NFS share privileges.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.FileServ.NFS.SharePrivilege`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the fileserv nfs share privilege get operation.  
</div>
  



---


### `fileserv_rsync_account_get`
Get rsync account settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.FileServ.Rsync.Account`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the fileserv rsync account get operation.  
</div>
  



---


### `fileserv_rsync_account_set`
Set rsync account settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.FileServ.Rsync.Account`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `dict`  
Additional keyword arguments forwarded to the API.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the fileserv rsync account set operation.  
</div>
  



---


### `fileserv_smb_conf_backup_get`
Get SMB configuration backup.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.FileServ.SMB.ConfBackup`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the fileserv smb conf backup get operation.  
</div>
  



---


### `fileserv_smb_control_get`
Get SMB control settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.FileServ.SMB.Control`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the fileserv smb control get operation.  
</div>
  



---


### `fileserv_smb_msdfs_get`
Get SMB MS-DFS settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.FileServ.SMB.MSDFS`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the fileserv smb msdfs get operation.  
</div>
  



---


### `findhost_get`
Get find-host settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Findhost`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the findhost get operation.  
</div>
  



---


### `group_extra_admin_get`
Get extra admin group settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Group.ExtraAdmin`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the group extra admin get operation.  
</div>
  



---


### `group_member_list`
List members of a group.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Group.Member`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_group_** `str`  
The group value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the group member list operation.  
</div>
  



---


### `group_valid_local_admin_get`
Get valid local admin information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Group.ValidLocalAdmin`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the group valid local admin get operation.  
</div>
  



---


### `hardware_lcm_get`
Get LCD monitor panel settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Hardware.LCM`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the hardware lcm get operation.  
</div>
  



---


### `hardware_led_brightness_get`
Get LED brightness settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Hardware.Led.Brightness`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the hardware led brightness get operation.  
</div>
  



---


### `hardware_led_brightness_set`
Set LED brightness level.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Hardware.Led.Brightness`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_brightness_** `int`  
The brightness value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the hardware led brightness set operation.  
</div>
  



---


### `hardware_memory_layout_get`
Get memory layout information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Hardware.MemoryLayout`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the hardware memory layout get operation.  
</div>
  



---


### `hardware_need_reboot_get`
Check if a reboot is required.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Hardware.NeedReboot`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the hardware need reboot get operation.  
</div>
  



---


### `hardware_oob_management_get`
Get out-of-band management (IPMI/BMC) settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Hardware.OOBManagement`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the hardware oob management get operation.  
</div>
  



---


### `hardware_remote_fan_status_get`
Get remote fan status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Hardware.RemoteFanStatus`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the hardware remote fan status get operation.  
</div>
  



---


### `hardware_spectre_meltdown_get`
Get Spectre/Meltdown mitigation status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Hardware.SpectreMeltdown`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the hardware spectre meltdown get operation.  
</div>
  



---


### `hardware_video_transcoding_get`
Get hardware video transcoding capability.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Hardware.VideoTranscoding`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the hardware video transcoding get operation.  
</div>
  



---


### `iscsi_fc_target_get`
Get Fibre Channel target settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ISCSI.FCTarget`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the iscsi fc target get operation.  
</div>
  



---


### `iscsi_host_get`
Get iSCSI host settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ISCSI.Host`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the iscsi host get operation.  
</div>
  



---


### `iscsi_lunbkp_get`
Get iSCSI LUN backup settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ISCSI.Lunbkp`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the iscsi lunbkp get operation.  
</div>
  



---


### `iscsi_node_get`
Get iSCSI node information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ISCSI.Node`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the iscsi node get operation.  
</div>
  



---


### `iscsi_replication_get`
Get iSCSI replication settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ISCSI.Replication`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the iscsi replication get operation.  
</div>
  



---


### `iscsi_vmware_get`
Get iSCSI VMware integration settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ISCSI.VMware`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the iscsi vmware get operation.  
</div>
  



---


### `media_indexing_get`
Get media indexing settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.MediaIndexing`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the media indexing get operation.  
</div>
  



---


### `media_indexing_set`
Set media indexing settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.MediaIndexing`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `dict`  
Additional keyword arguments forwarded to the API.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the media indexing set operation.  
</div>
  



---


### `media_indexing_index_folder_get`
Get indexed folder list.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.MediaIndexing.IndexFolder`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the media indexing index folder get operation.  
</div>
  



---


### `media_indexing_media_converter_get`
Get media converter settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.MediaIndexing.MediaConverter`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the media indexing media converter get operation.  
</div>
  



---


### `media_indexing_scheduler_get`
Get media indexing scheduler settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.MediaIndexing.Scheduler`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the media indexing scheduler get operation.  
</div>
  



---


### `media_indexing_thumbnail_quality_get`
Get thumbnail quality settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.MediaIndexing.ThumbnailQuality`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the media indexing thumbnail quality get operation.  
</div>
  



---


### `mydscenter_get`
Get MyDS Center settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.MyDSCenter`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the mydscenter get operation.  
</div>
  



---


### `mydscenter_account_get`
Get MyDS Center account information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.MyDSCenter.Account`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the mydscenter account get operation.  
</div>
  



---


### `mydscenter_login`
Login to MyDS Center.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.MyDSCenter.Login`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_username_** `str`  
The username value.  
  
**_password_** `str`  
The password value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the mydscenter login operation.  
</div>
  



---


### `mydscenter_logout`
Logout from MyDS Center.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.MyDSCenter.Logout`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the mydscenter logout operation.  
</div>
  



---


### `mydscenter_purchase_get`
Get MyDS Center purchase information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.MyDSCenter.Purchase`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the mydscenter purchase get operation.  
</div>
  



---


### `normal_user_get`
Get normal user settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.NormalUser`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the normal user get operation.  
</div>
  



---


### `normal_user_login_notify_get`
Get normal user login notification settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.NormalUser.LoginNotify`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the normal user login notify get operation.  
</div>
  



---


### `oauth_scope_get`
Get OAuth scope settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.OAuth.Scope`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the oauth scope get operation.  
</div>
  



---


### `oauth_server_get`
Get OAuth server settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.OAuth.Server`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the oauth server get operation.  
</div>
  



---


### `oauth_server_set`
Set OAuth server settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.OAuth.Server`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `dict`  
Additional keyword arguments forwarded to the API.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the oauth server set operation.  
</div>
  



---


### `package_auto_upgrade_progress_get`
Get package auto-upgrade progress.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Package.AutoUpgrade.Progress`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the package auto upgrade progress get operation.  
</div>
  



---


### `package_control`
Control a package (start/stop).  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Package.Control`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_package_id_** `str`  
The package id value.  
  
**_action_** `str`  
The action value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the package control operation.  
</div>
  



---


### `package_fake_iframe_get`
Get package fake iframe info.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Package.FakeIFrame`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the package fake iframe get operation.  
</div>
  



---


### `package_feed_list`
List package feeds.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Package.Feed`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the package feed list operation.  
</div>
  



---


### `package_feed_set`
Set package feed settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Package.Feed`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `dict`  
Additional keyword arguments forwarded to the API.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the package feed set operation.  
</div>
  



---


### `package_legal_prerelease_get`
Get package pre-release legal agreement status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Package.Legal.PreRelease`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the package legal prerelease get operation.  
</div>
  



---


### `package_log_get`
Get package log entries.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Package.Log`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_package_id_** `str`  
The package id value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the package log get operation.  
</div>
  



---


### `package_myds_get`
Get MyDS package info.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Package.MyDS`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the package myds get operation.  
</div>
  



---


### `package_myds_purchase_get`
Get MyDS package purchase info.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Package.MyDS.Purchase`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the package myds purchase get operation.  
</div>
  



---


### `package_progress_get`
Get package installation/upgrade progress.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Package.Progress`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_task_id_** `str`  
The task id value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the package progress get operation.  
</div>
  



---


### `package_screenshot_get`
Get package screenshots.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Package.Screenshot`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_package_id_** `str`  
The package id value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the package screenshot get operation.  
</div>
  



---


### `package_screenshot_server_get`
Get package screenshot from server.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Package.Screenshot.Server`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_package_id_** `str`  
The package id value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the package screenshot server get operation.  
</div>
  



---


### `package_setting_update_get`
Get package update settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Package.Setting.Update`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the package setting update get operation.  
</div>
  



---


### `package_thumb_get`
Get package thumbnail.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Package.Thumb`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_package_id_** `str`  
The package id value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the package thumb get operation.  
</div>
  



---


### `package_thumb_server_get`
Get package thumbnail from server.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Package.Thumb.Server`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_package_id_** `str`  
The package id value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the package thumb server get operation.  
</div>
  



---


### `personal_notification_device_get`
Get personal notification device settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.PersonalNotification.Device`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the personal notification device get operation.  
</div>
  



---


### `personal_notification_event_get`
Get personal notification events.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.PersonalNotification.Event`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the personal notification event get operation.  
</div>
  



---


### `personal_notification_filter_get`
Get personal notification filter settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.PersonalNotification.Filter`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the personal notification filter get operation.  
</div>
  



---


### `personal_notification_filter_set`
Set personal notification filter settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.PersonalNotification.Filter`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `dict`  
Additional keyword arguments forwarded to the API.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the personal notification filter set operation.  
</div>
  



---


### `personal_notification_mobile_get`
Get personal notification mobile settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.PersonalNotification.Mobile`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the personal notification mobile get operation.  
</div>
  



---


### `personal_notification_settings_get`
Get personal notification settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.PersonalNotification.Settings`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the personal notification settings get operation.  
</div>
  



---


### `personal_notification_settings_set`
Set personal notification settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.PersonalNotification.Settings`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `dict`  
Additional keyword arguments forwarded to the API.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the personal notification settings set operation.  
</div>
  



---


### `photo_viewer_get`
Get photo viewer settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.PhotoViewer`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the photo viewer get operation.  
</div>
  



---


### `port_forwarding_get`
Get port forwarding settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.PortForwarding`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the port forwarding get operation.  
</div>
  



---


### `port_forwarding_compatibility_get`
Get port forwarding compatibility status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.PortForwarding.Compatibility`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the port forwarding compatibility get operation.  
</div>
  



---


### `port_forwarding_router_info_get`
Get router information for port forwarding.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.PortForwarding.RouterInfo`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the port forwarding router info get operation.  
</div>
  



---


### `port_forwarding_router_list`
List detected routers.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.PortForwarding.RouterList`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the port forwarding router list operation.  
</div>
  



---


### `port_forwarding_rules_serv_get`
Get service-based port forwarding rules.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.PortForwarding.Rules.Serv`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the port forwarding rules serv get operation.  
</div>
  



---


### `promotion_info_get`
Get Synology promotion information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Promotion.Info`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the promotion info get operation.  
</div>
  



---


### `promotion_preinstall_get`
Get pre-install promotion information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Promotion.PreInstall`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the promotion preinstall get operation.  
</div>
  



---


### `quickconnect_hostname_get`
Get QuickConnect hostname settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.QuickConnect.Hostname`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the quickconnect hostname get operation.  
</div>
  



---


### `quickconnect_register_site_get`
Get QuickConnect registration site info.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.QuickConnect.RegisterSite`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the quickconnect register site get operation.  
</div>
  



---


### `quickconnect_sni_get`
Get QuickConnect SNI settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.QuickConnect.SNI`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the quickconnect sni get operation.  
</div>
  



---


### `quickconnect_upnp_get`
Get QuickConnect UPnP settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.QuickConnect.Upnp`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the quickconnect upnp get operation.  
</div>
  



---


### `quickstart_info_get`
Get quick start wizard information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.QuickStart.Info`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the quickstart info get operation.  
</div>
  



---


### `quickstart_install`
Run quick start installation.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.QuickStart.Install`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `dict`  
Additional keyword arguments forwarded to the API.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the quickstart install operation.  
</div>
  



---


### `report_get`
Get report settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Report`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the report get operation.  
</div>
  



---


### `report_analyzer_get`
Get report analyzer settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Report.Analyzer`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the report analyzer get operation.  
</div>
  



---


### `report_analyzer_file_get`
Get report analyzer file info.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Report.Analyzer.File`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the report analyzer file get operation.  
</div>
  



---


### `report_analyzer_share_get`
Get report analyzer share info.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Report.Analyzer.Share`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the report analyzer share get operation.  
</div>
  



---


### `report_config_get`
Get report configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Report.Config`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the report config get operation.  
</div>
  



---


### `report_config_set`
Set report configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Report.Config`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `dict`  
Additional keyword arguments forwarded to the API.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the report config set operation.  
</div>
  



---


### `report_history_get`
Get report history.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Report.History`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the report history get operation.  
</div>
  



---


### `report_redirect_get`
Get report redirect settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Report.Redirect`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the report redirect get operation.  
</div>
  



---


### `report_util_get`
Get report utility information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Report.Util`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the report util get operation.  
</div>
  



---


### `reset_admin_get`
Get admin reset status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ResetAdmin`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the reset admin get operation.  
</div>
  



---


### `security_scan_operation_start`
Start a security scan.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SecurityScan.Operation`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the security scan operation start operation.  
</div>
  



---


### `security_scan_operation_get`
Get security scan operation status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SecurityScan.Operation`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the security scan operation get operation.  
</div>
  



---


### `service_conf_get`
Get service configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Service.Conf`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the service conf get operation.  
</div>
  



---


### `service_conf_set`
Set service configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Service.Conf`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `dict`  
Additional keyword arguments forwarded to the API.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the service conf set operation.  
</div>
  



---


### `service_port_info_get`
Get service port information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Service.PortInfo`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the service port info get operation.  
</div>
  



---


### `share_crypto_get`
Get shared folder encryption settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Share.Crypto`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the share crypto get operation.  
</div>
  



---


### `share_crypto_key_get`
Get shared folder encryption key info.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Share.Crypto.Key`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the share crypto key get operation.  
</div>
  



---


### `share_crypto_file_get`
Get encrypted shared folder file settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Share.CryptoFile`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the share crypto file get operation.  
</div>
  



---


### `share_key_manager_auto_key_get`
Get key manager auto-key settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Share.KeyManager.AutoKey`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the share key manager auto key get operation.  
</div>
  



---


### `share_key_manager_key_get`
Get key manager key settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Share.KeyManager.Key`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the share key manager key get operation.  
</div>
  



---


### `share_key_manager_machine_key_get`
Get key manager machine key settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Share.KeyManager.MachineKey`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the share key manager machine key get operation.  
</div>
  



---


### `share_key_manager_store_get`
Get key manager store settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Share.KeyManager.Store`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the share key manager store get operation.  
</div>
  



---


### `share_migration_get`
Get shared folder migration status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Share.Migration`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the share migration get operation.  
</div>
  



---


### `share_migration_task_get`
Get shared folder migration task status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Share.Migration.Task`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the share migration task get operation.  
</div>
  



---


### `share_permission_get`
Get permissions for a shared folder.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Share.Permission`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_name_** `str`  
The name value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the share permission get operation.  
</div>
  



---


### `share_permission_set`
Set permissions for a shared folder.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Share.Permission`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_name_** `str`  
The name value.  
  
**_permissions_** `dict`  
The permissions value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the share permission set operation.  
</div>
  



---


### `share_permission_report_get`
Get shared folder permission report.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Share.PermissionReport`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the share permission report get operation.  
</div>
  



---


### `share_shell_file_get`
Get shared folder shell file settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Share.ShellFile`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the share shell file get operation.  
</div>
  



---


### `sharing_get`
Get file sharing settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Sharing`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the sharing get operation.  
</div>
  



---


### `sharing_initdata_get`
Get sharing initialization data.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Sharing.Initdata`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the sharing initdata get operation.  
</div>
  



---


### `sharing_login`
Login to a file sharing link.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Sharing.Login`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_sharing_id_** `str`  
The sharing id value.  
  
**_password_** `str`  
The password value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the sharing login operation.  
</div>
  



---


### `sharing_session_get`
Get sharing session information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Sharing.Session`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the sharing session get operation.  
</div>
  



---


### `support_form_get`
Get support form configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SupportForm.Form`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the support form get operation.  
</div>
  



---


### `support_form_log_get`
Get support form submission log.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SupportForm.Log`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the support form log get operation.  
</div>
  



---


### `support_form_service_get`
Get support form service status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SupportForm.Service`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the support form service get operation.  
</div>
  



---


### `synohdpack_get`
Get Synology HD pack information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Synohdpack`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the synohdpack get operation.  
</div>
  



---


### `syslog_personal_activity_get`
Get personal activity syslog settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SyslogClient.PersonalActivity`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the syslog personal activity get operation.  
</div>
  



---


### `tuned_get`
Get system tuning (tuned) settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Tuned`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the tuned get operation.  
</div>
  



---


### `tuned_set`
Set system tuning settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Tuned`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `dict`  
Additional keyword arguments forwarded to the API.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the tuned set operation.  
</div>
  



---


### `user_group_get`
Get groups a user belongs to.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.User.Group`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_user_** `str`  
The user value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the user group get operation.  
</div>
  



---


### `user_password_expiry_get`
Get password expiry settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.User.PasswordExpiry`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the user password expiry get operation.  
</div>
  



---


### `user_password_meter_get`
Check password strength.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.User.PasswordMeter`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_password_** `str`  
The password value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the user password meter get operation.  
</div>
  



---


### `user_password_policy_get`
Get password policy settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.User.PasswordPolicy`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the user password policy get operation.  
</div>
  



---


### `user_password_policy_set`
Set password policy settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.User.PasswordPolicy`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `dict`  
Additional keyword arguments forwarded to the API.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the user password policy set operation.  
</div>
  



---


### `user_username_policy_get`
Get username policy settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.User.UsernamePolicy`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the user username policy get operation.  
</div>
  



---


### `virtualization_host_capability_get`
Get virtualization host capability information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Virtualization.Host.Capability`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the virtualization host capability get operation.  
</div>
  



---


### `vol_enc_keep_key_get`
Get volume encryption keep-key settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.VolEncKeepKey`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the vol enc keep key get operation.  
</div>
  



---


### `vol_enc_keep_key_set`
Set volume encryption keep-key settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.VolEncKeepKey`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `dict`  
Additional keyword arguments forwarded to the API.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the vol enc keep key set operation.  
</div>
  



---


### `web_dsm_external_get`
Get DSM external web access settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Web.DSM.External`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the web dsm external get operation.  
</div>
  



---


### `web_dsm_external_set`
Set DSM external web access settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Web.DSM.External`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `dict`  
Additional keyword arguments forwarded to the API.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the web dsm external set operation.  
</div>
  



---


### `web_security_http_compression_get`
Get HTTP compression settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Web.Security.HTTPCompression`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the web security http compression get operation.  
</div>
  



---


### `web_security_http_compression_set`
Set HTTP compression settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Web.Security.HTTPCompression`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `dict`  
Additional keyword arguments forwarded to the API.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the web security http compression set operation.  
</div>
  



---


### `web_security_tls_profile_get`
Get TLS profile settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Web.Security.TLSProfile`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the web security tls profile get operation.  
</div>
  



---


### `web_security_tls_profile_set`
Set TLS profile settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Web.Security.TLSProfile`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `dict`  
Additional keyword arguments forwarded to the API.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the web security tls profile set operation.  
</div>
  



---


