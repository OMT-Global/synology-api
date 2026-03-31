---
sidebar_position: 13
title: 🚧 CoreSecurity
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# CoreSecurity
:::warning
 
This API is partially documented or under construction.
 
:::
## Overview
Core Security API implementation for Synology NAS.  
  
Provides methods to manage security features including auto-block rules,
firewall settings, DoS protection, SmartBlock, OTP, and trusted devices.  
  
## Methods
### `autoblock_rules_get`
Get auto-block rules.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.AutoBlock.Rules`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Auto-block rules configuration.  
</div>
  



---


### `autoblock_rules_list`
List all auto-block rules.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.AutoBlock.Rules`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of auto-block rules.  
</div>
  



---


### `autoblock_rules_set`
Set auto-block rules.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.AutoBlock.Rules`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_rules_** `list[dict[str, object]]`  
List of rule objects to apply.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `autoblock_rules_delete`
Delete auto-block rules.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.AutoBlock.Rules`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_rules_** `list[dict[str, object]]`  
List of rule objects to delete.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the delete operation.  
</div>
  



---


### `security_dsm_get`
Get DSM security settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.DSM`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
DSM security settings.  
</div>
  



---


### `security_dsm_set`
Set DSM security settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.DSM`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Key-value pairs of DSM security settings to update.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `security_dsm_embed_get`
Get DSM embed security settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.DSM.Embed`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
DSM embed security settings.  
</div>
  



---


### `security_dsm_embed_set`
Set DSM embed security settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.DSM.Embed`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Key-value pairs of embed security settings to update.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `security_dsm_proxy_get`
Get DSM proxy security settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.DSM.Proxy`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
DSM proxy security settings.  
</div>
  



---


### `security_dsm_proxy_set`
Set DSM proxy security settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.DSM.Proxy`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Key-value pairs of proxy security settings to update.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `security_dos_get`
Get DoS protection settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.DoS`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
DoS protection settings.  
</div>
  



---


### `security_dos_set`
Set DoS protection settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.DoS`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Key-value pairs of DoS protection settings to update.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `firewall_get`
Get firewall status and settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.Firewall`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Firewall status and settings.  
</div>
  



---


### `firewall_set`
Set firewall settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.Firewall`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Key-value pairs of firewall settings to update.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `firewall_adapter_get`
Get firewall adapter configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.Firewall.Adapter`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Firewall adapter configuration.  
</div>
  



---


### `firewall_adapter_list`
List firewall adapters.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.Firewall.Adapter`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of firewall adapters.  
</div>
  



---


### `firewall_conf_get`
Get firewall configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.Firewall.Conf`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Firewall configuration.  
</div>
  



---


### `firewall_conf_set`
Set firewall configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.Firewall.Conf`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Key-value pairs of firewall configuration to update.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `firewall_geoip_get`
Get geo-IP blocking settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.Firewall.Geoip`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Geo-IP blocking settings.  
</div>
  



---


### `firewall_geoip_set`
Set geo-IP blocking settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.Firewall.Geoip`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Key-value pairs of geo-IP blocking settings to update.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `firewall_profile_apply`
Apply a firewall profile.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.Firewall.Profile.Apply`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_profile_name_** `str`  
Name of the firewall profile to apply. Defaults to empty string.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the apply operation.  
</div>
  



---


### `firewall_profile_apply_status`
Get the status of a firewall profile apply operation.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.Firewall.Profile.Apply`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Status of the apply operation.  
</div>
  



---


### `firewall_rules_get`
Get firewall rules.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.Firewall.Rules`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Firewall rules configuration.  
</div>
  



---


### `firewall_rules_list`
List all firewall rules.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.Firewall.Rules`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of firewall rules.  
</div>
  



---


### `firewall_rules_set`
Set firewall rules.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.Firewall.Rules`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_rules_** `list[dict[str, object]]`  
List of firewall rule objects to apply.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `firewall_rules_delete`
Delete firewall rules.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.Firewall.Rules`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_rules_** `list[dict[str, object]]`  
List of firewall rule objects to delete.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the delete operation.  
</div>
  



---


### `firewall_rules_serv_get`
Get service-based firewall rules.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.Firewall.Rules.Serv`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Service-based firewall rules.  
</div>
  



---


### `firewall_rules_serv_list`
List service-based firewall rules.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.Firewall.Rules.Serv`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of service-based firewall rules.  
</div>
  



---


### `smartblock_get`
Get SmartBlock settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SmartBlock`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
SmartBlock settings.  
</div>
  



---


### `smartblock_set`
Set SmartBlock settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SmartBlock`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Key-value pairs of SmartBlock settings to update.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `smartblock_device_get`
Get SmartBlock blocked devices.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SmartBlock.Device`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Blocked device information.  
</div>
  



---


### `smartblock_device_list`
List SmartBlock blocked devices.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SmartBlock.Device`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of blocked devices.  
</div>
  



---


### `smartblock_device_delete`
Remove devices from the SmartBlock blocked list.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SmartBlock.Device`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_devices_** `list[str]`  
List of device identifiers to remove.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the delete operation.  
</div>
  



---


### `smartblock_trusted_get`
Get SmartBlock trusted list.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SmartBlock.Trusted`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Trusted list entries.  
</div>
  



---


### `smartblock_trusted_list`
List SmartBlock trusted entries.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SmartBlock.Trusted`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of trusted entries.  
</div>
  



---


### `smartblock_trusted_set`
Set SmartBlock trusted list entries.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SmartBlock.Trusted`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_entries_** `list[dict[str, object]]`  
List of trusted entry objects to set.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `smartblock_trusted_delete`
Delete entries from the SmartBlock trusted list.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SmartBlock.Trusted`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_entries_** `list[str]`  
List of entry identifiers to remove.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the delete operation.  
</div>
  



---


### `smartblock_untrusted_get`
Get SmartBlock untrusted list.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SmartBlock.Untrusted`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Untrusted list entries.  
</div>
  



---


### `smartblock_untrusted_list`
List SmartBlock untrusted entries.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SmartBlock.Untrusted`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of untrusted entries.  
</div>
  



---


### `smartblock_untrusted_set`
Set SmartBlock untrusted list entries.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SmartBlock.Untrusted`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_entries_** `list[dict[str, object]]`  
List of untrusted entry objects to set.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `smartblock_untrusted_delete`
Delete entries from the SmartBlock untrusted list.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SmartBlock.Untrusted`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_entries_** `list[str]`  
List of entry identifiers to remove.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the delete operation.  
</div>
  



---


### `smartblock_user_get`
Get SmartBlock user-level block settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SmartBlock.User`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
User-level block settings.  
</div>
  



---


### `smartblock_user_list`
List SmartBlock user-level blocks.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SmartBlock.User`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of user-level blocks.  
</div>
  



---


### `smartblock_user_set`
Set SmartBlock user-level blocks.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SmartBlock.User`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_users_** `list[dict[str, object]]`  
List of user block objects to set.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `smartblock_user_delete`
Delete SmartBlock user-level blocks.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SmartBlock.User`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_users_** `list[str]`  
List of user identifiers to unblock.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the delete operation.  
</div>
  



---


### `otp_get`
Get OTP settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.OTP`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
OTP settings.  
</div>
  



---


### `otp_set`
Set OTP settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.OTP`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Key-value pairs of OTP settings to update.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `otp_admin_get`
Get OTP admin settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.OTP.Admin`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
OTP admin settings.  
</div>
  



---


### `otp_admin_set`
Set OTP admin settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.OTP.Admin`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Key-value pairs of OTP admin settings to update.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `otp_enforce_policy_get`
Get OTP enforcement policy.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.OTP.EnforcePolicy`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
OTP enforcement policy settings.  
</div>
  



---


### `otp_enforce_policy_set`
Set OTP enforcement policy.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.OTP.EnforcePolicy`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Key-value pairs of enforcement policy settings to update.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `otp_ex_get`
Get extended OTP settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.OTP.Ex`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Extended OTP settings.  
</div>
  



---


### `otp_ex_set`
Set extended OTP settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.OTP.Ex`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Key-value pairs of extended OTP settings to update.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `otp_mail_get`
Get OTP mail settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.OTP.Mail`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
OTP mail settings.  
</div>
  



---


### `otp_mail_set`
Set OTP mail settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.OTP.Mail`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Key-value pairs of OTP mail settings to update.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `trust_device_get`
Get trusted device settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.TrustDevice`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Trusted device settings.  
</div>
  



---


### `trust_device_list`
List trusted devices.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.TrustDevice`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of trusted devices.  
</div>
  



---


### `trust_device_delete`
Remove devices from the trusted list.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.TrustDevice`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_devices_** `list[str]`  
List of device identifiers to remove.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the delete operation.  
</div>
  



---


### `disable_admin_get`
Get disabled admin account settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.DisableAdmin`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Disabled admin account settings.  
</div>
  



---


### `disable_admin_set`
Set disabled admin account settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.DisableAdmin`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Key-value pairs of admin disable settings to update.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


