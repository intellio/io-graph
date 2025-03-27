from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class MobileAppPolicySetItem(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.mobileAppPolicySetItem"] = Field(alias="@odata.type", default="#microsoft.graph.mobileAppPolicySetItem")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	errorCode: Optional[ErrorCode | str] = Field(alias="errorCode", default=None,)
	guidedDeploymentTags: Optional[list[str]] = Field(alias="guidedDeploymentTags", default=None,)
	itemType: Optional[str] = Field(alias="itemType", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	payloadId: Optional[str] = Field(alias="payloadId", default=None,)
	status: Optional[PolicySetStatus | str] = Field(alias="status", default=None,)
	intent: Optional[InstallIntent | str] = Field(alias="intent", default=None,)
	settings: Optional[Union[AndroidManagedStoreAppAssignmentSettings, IosLobAppAssignmentSettings, IosStoreAppAssignmentSettings, IosVppAppAssignmentSettings, MacOsLobAppAssignmentSettings, MacOsVppAppAssignmentSettings, MicrosoftStoreForBusinessAppAssignmentSettings, Win32LobAppAssignmentSettings, Win32CatalogAppAssignmentSettings, WindowsAppXAppAssignmentSettings, WindowsUniversalAppXAppAssignmentSettings, WinGetAppAssignmentSettings]] = Field(alias="settings", default=None,discriminator="odata_type", )

from .error_code import ErrorCode
from .policy_set_status import PolicySetStatus
from .install_intent import InstallIntent
from .android_managed_store_app_assignment_settings import AndroidManagedStoreAppAssignmentSettings
from .ios_lob_app_assignment_settings import IosLobAppAssignmentSettings
from .ios_store_app_assignment_settings import IosStoreAppAssignmentSettings
from .ios_vpp_app_assignment_settings import IosVppAppAssignmentSettings
from .mac_os_lob_app_assignment_settings import MacOsLobAppAssignmentSettings
from .mac_os_vpp_app_assignment_settings import MacOsVppAppAssignmentSettings
from .microsoft_store_for_business_app_assignment_settings import MicrosoftStoreForBusinessAppAssignmentSettings
from .win32_lob_app_assignment_settings import Win32LobAppAssignmentSettings
from .win32_catalog_app_assignment_settings import Win32CatalogAppAssignmentSettings
from .windows_app_x_app_assignment_settings import WindowsAppXAppAssignmentSettings
from .windows_universal_app_x_app_assignment_settings import WindowsUniversalAppXAppAssignmentSettings
from .win_get_app_assignment_settings import WinGetAppAssignmentSettings

