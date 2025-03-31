from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class WindowsManagedAppProtection(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsManagedAppProtection"] = Field(alias="@odata.type", default="#microsoft.graph.windowsManagedAppProtection")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)
	allowedInboundDataTransferSources: Optional[WindowsManagedAppDataTransferLevel | str] = Field(alias="allowedInboundDataTransferSources", default=None,)
	allowedOutboundClipboardSharingLevel: Optional[WindowsManagedAppClipboardSharingLevel | str] = Field(alias="allowedOutboundClipboardSharingLevel", default=None,)
	allowedOutboundDataTransferDestinations: Optional[WindowsManagedAppDataTransferLevel | str] = Field(alias="allowedOutboundDataTransferDestinations", default=None,)
	appActionIfUnableToAuthenticateUser: Optional[ManagedAppRemediationAction | str] = Field(alias="appActionIfUnableToAuthenticateUser", default=None,)
	deployedAppCount: Optional[int] = Field(alias="deployedAppCount", default=None,)
	isAssigned: Optional[bool] = Field(alias="isAssigned", default=None,)
	maximumAllowedDeviceThreatLevel: Optional[ManagedAppDeviceThreatLevel | str] = Field(alias="maximumAllowedDeviceThreatLevel", default=None,)
	maximumRequiredOsVersion: Optional[str] = Field(alias="maximumRequiredOsVersion", default=None,)
	maximumWarningOsVersion: Optional[str] = Field(alias="maximumWarningOsVersion", default=None,)
	maximumWipeOsVersion: Optional[str] = Field(alias="maximumWipeOsVersion", default=None,)
	minimumRequiredAppVersion: Optional[str] = Field(alias="minimumRequiredAppVersion", default=None,)
	minimumRequiredOsVersion: Optional[str] = Field(alias="minimumRequiredOsVersion", default=None,)
	minimumRequiredSdkVersion: Optional[str] = Field(alias="minimumRequiredSdkVersion", default=None,)
	minimumWarningAppVersion: Optional[str] = Field(alias="minimumWarningAppVersion", default=None,)
	minimumWarningOsVersion: Optional[str] = Field(alias="minimumWarningOsVersion", default=None,)
	minimumWipeAppVersion: Optional[str] = Field(alias="minimumWipeAppVersion", default=None,)
	minimumWipeOsVersion: Optional[str] = Field(alias="minimumWipeOsVersion", default=None,)
	minimumWipeSdkVersion: Optional[str] = Field(alias="minimumWipeSdkVersion", default=None,)
	mobileThreatDefenseRemediationAction: Optional[ManagedAppRemediationAction | str] = Field(alias="mobileThreatDefenseRemediationAction", default=None,)
	periodOfflineBeforeAccessCheck: Optional[str] = Field(alias="periodOfflineBeforeAccessCheck", default=None,)
	periodOfflineBeforeWipeIsEnforced: Optional[str] = Field(alias="periodOfflineBeforeWipeIsEnforced", default=None,)
	printBlocked: Optional[bool] = Field(alias="printBlocked", default=None,)
	apps: Optional[list[ManagedMobileApp]] = Field(alias="apps", default=None,)
	assignments: Optional[list[TargetedManagedAppPolicyAssignment]] = Field(alias="assignments", default=None,)
	deploymentSummary: Optional[ManagedAppPolicyDeploymentSummary] = Field(alias="deploymentSummary", default=None,)

from .windows_managed_app_data_transfer_level import WindowsManagedAppDataTransferLevel
from .windows_managed_app_clipboard_sharing_level import WindowsManagedAppClipboardSharingLevel
from .managed_app_remediation_action import ManagedAppRemediationAction
from .managed_app_device_threat_level import ManagedAppDeviceThreatLevel
from .managed_mobile_app import ManagedMobileApp
from .targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment
from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary
