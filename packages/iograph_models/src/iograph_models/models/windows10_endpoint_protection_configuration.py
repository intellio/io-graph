from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Windows10EndpointProtectionConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	version: Optional[int] = Field(alias="version",default=None,)
	assignments: Optional[list[DeviceConfigurationAssignment]] = Field(alias="assignments",default=None,)
	deviceSettingStateSummaries: Optional[list[SettingStateDeviceSummary]] = Field(alias="deviceSettingStateSummaries",default=None,)
	deviceStatuses: Optional[list[DeviceConfigurationDeviceStatus]] = Field(alias="deviceStatuses",default=None,)
	deviceStatusOverview: Optional[DeviceConfigurationDeviceOverview] = Field(alias="deviceStatusOverview",default=None,)
	userStatuses: Optional[list[DeviceConfigurationUserStatus]] = Field(alias="userStatuses",default=None,)
	userStatusOverview: Optional[DeviceConfigurationUserOverview] = Field(alias="userStatusOverview",default=None,)
	applicationGuardAllowPersistence: Optional[bool] = Field(alias="applicationGuardAllowPersistence",default=None,)
	applicationGuardAllowPrintToLocalPrinters: Optional[bool] = Field(alias="applicationGuardAllowPrintToLocalPrinters",default=None,)
	applicationGuardAllowPrintToNetworkPrinters: Optional[bool] = Field(alias="applicationGuardAllowPrintToNetworkPrinters",default=None,)
	applicationGuardAllowPrintToPDF: Optional[bool] = Field(alias="applicationGuardAllowPrintToPDF",default=None,)
	applicationGuardAllowPrintToXPS: Optional[bool] = Field(alias="applicationGuardAllowPrintToXPS",default=None,)
	applicationGuardBlockClipboardSharing: Optional[str | ApplicationGuardBlockClipboardSharingType] = Field(alias="applicationGuardBlockClipboardSharing",default=None,)
	applicationGuardBlockFileTransfer: Optional[str | ApplicationGuardBlockFileTransferType] = Field(alias="applicationGuardBlockFileTransfer",default=None,)
	applicationGuardBlockNonEnterpriseContent: Optional[bool] = Field(alias="applicationGuardBlockNonEnterpriseContent",default=None,)
	applicationGuardEnabled: Optional[bool] = Field(alias="applicationGuardEnabled",default=None,)
	applicationGuardForceAuditing: Optional[bool] = Field(alias="applicationGuardForceAuditing",default=None,)
	appLockerApplicationControl: Optional[str | AppLockerApplicationControlType] = Field(alias="appLockerApplicationControl",default=None,)
	bitLockerDisableWarningForOtherDiskEncryption: Optional[bool] = Field(alias="bitLockerDisableWarningForOtherDiskEncryption",default=None,)
	bitLockerEnableStorageCardEncryptionOnMobile: Optional[bool] = Field(alias="bitLockerEnableStorageCardEncryptionOnMobile",default=None,)
	bitLockerEncryptDevice: Optional[bool] = Field(alias="bitLockerEncryptDevice",default=None,)
	bitLockerRemovableDrivePolicy: Optional[BitLockerRemovableDrivePolicy] = Field(alias="bitLockerRemovableDrivePolicy",default=None,)
	defenderAdditionalGuardedFolders: Optional[list[str]] = Field(alias="defenderAdditionalGuardedFolders",default=None,)
	defenderAttackSurfaceReductionExcludedPaths: Optional[list[str]] = Field(alias="defenderAttackSurfaceReductionExcludedPaths",default=None,)
	defenderExploitProtectionXml: Optional[str] = Field(alias="defenderExploitProtectionXml",default=None,)
	defenderExploitProtectionXmlFileName: Optional[str] = Field(alias="defenderExploitProtectionXmlFileName",default=None,)
	defenderGuardedFoldersAllowedAppPaths: Optional[list[str]] = Field(alias="defenderGuardedFoldersAllowedAppPaths",default=None,)
	defenderSecurityCenterBlockExploitProtectionOverride: Optional[bool] = Field(alias="defenderSecurityCenterBlockExploitProtectionOverride",default=None,)
	firewallBlockStatefulFTP: Optional[bool] = Field(alias="firewallBlockStatefulFTP",default=None,)
	firewallCertificateRevocationListCheckMethod: Optional[str | FirewallCertificateRevocationListCheckMethodType] = Field(alias="firewallCertificateRevocationListCheckMethod",default=None,)
	firewallIdleTimeoutForSecurityAssociationInSeconds: Optional[int] = Field(alias="firewallIdleTimeoutForSecurityAssociationInSeconds",default=None,)
	firewallIPSecExemptionsAllowDHCP: Optional[bool] = Field(alias="firewallIPSecExemptionsAllowDHCP",default=None,)
	firewallIPSecExemptionsAllowICMP: Optional[bool] = Field(alias="firewallIPSecExemptionsAllowICMP",default=None,)
	firewallIPSecExemptionsAllowNeighborDiscovery: Optional[bool] = Field(alias="firewallIPSecExemptionsAllowNeighborDiscovery",default=None,)
	firewallIPSecExemptionsAllowRouterDiscovery: Optional[bool] = Field(alias="firewallIPSecExemptionsAllowRouterDiscovery",default=None,)
	firewallMergeKeyingModuleSettings: Optional[bool] = Field(alias="firewallMergeKeyingModuleSettings",default=None,)
	firewallPacketQueueingMethod: Optional[str | FirewallPacketQueueingMethodType] = Field(alias="firewallPacketQueueingMethod",default=None,)
	firewallPreSharedKeyEncodingMethod: Optional[str | FirewallPreSharedKeyEncodingMethodType] = Field(alias="firewallPreSharedKeyEncodingMethod",default=None,)
	firewallProfileDomain: Optional[WindowsFirewallNetworkProfile] = Field(alias="firewallProfileDomain",default=None,)
	firewallProfilePrivate: Optional[WindowsFirewallNetworkProfile] = Field(alias="firewallProfilePrivate",default=None,)
	firewallProfilePublic: Optional[WindowsFirewallNetworkProfile] = Field(alias="firewallProfilePublic",default=None,)
	smartScreenBlockOverrideForFiles: Optional[bool] = Field(alias="smartScreenBlockOverrideForFiles",default=None,)
	smartScreenEnableInShell: Optional[bool] = Field(alias="smartScreenEnableInShell",default=None,)

from .device_configuration_assignment import DeviceConfigurationAssignment
from .setting_state_device_summary import SettingStateDeviceSummary
from .device_configuration_device_status import DeviceConfigurationDeviceStatus
from .device_configuration_device_overview import DeviceConfigurationDeviceOverview
from .device_configuration_user_status import DeviceConfigurationUserStatus
from .device_configuration_user_overview import DeviceConfigurationUserOverview
from .application_guard_block_clipboard_sharing_type import ApplicationGuardBlockClipboardSharingType
from .application_guard_block_file_transfer_type import ApplicationGuardBlockFileTransferType
from .app_locker_application_control_type import AppLockerApplicationControlType
from .bit_locker_removable_drive_policy import BitLockerRemovableDrivePolicy
from .firewall_certificate_revocation_list_check_method_type import FirewallCertificateRevocationListCheckMethodType
from .firewall_packet_queueing_method_type import FirewallPacketQueueingMethodType
from .firewall_pre_shared_key_encoding_method_type import FirewallPreSharedKeyEncodingMethodType
from .windows_firewall_network_profile import WindowsFirewallNetworkProfile
from .windows_firewall_network_profile import WindowsFirewallNetworkProfile
from .windows_firewall_network_profile import WindowsFirewallNetworkProfile

