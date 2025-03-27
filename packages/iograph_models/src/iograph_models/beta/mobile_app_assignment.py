from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field, SerializeAsAny


class MobileAppAssignment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	intent: Optional[InstallIntent | str] = Field(alias="intent", default=None,)
	settings: Optional[Union[AndroidManagedStoreAppAssignmentSettings, IosLobAppAssignmentSettings, IosStoreAppAssignmentSettings, IosVppAppAssignmentSettings, MacOsLobAppAssignmentSettings, MacOsVppAppAssignmentSettings, MicrosoftStoreForBusinessAppAssignmentSettings, Win32LobAppAssignmentSettings, Win32CatalogAppAssignmentSettings, WindowsAppXAppAssignmentSettings, WindowsUniversalAppXAppAssignmentSettings, WinGetAppAssignmentSettings]] = Field(alias="settings", default=None,discriminator="odata_type", )
	source: Optional[DeviceAndAppManagementAssignmentSource | str] = Field(alias="source", default=None,)
	sourceId: Optional[str] = Field(alias="sourceId", default=None,)
	target: Optional[Union[AllDevicesAssignmentTarget, AllLicensedUsersAssignmentTarget, AndroidFotaDeploymentAssignmentTarget, ConfigurationManagerCollectionAssignmentTarget, GroupAssignmentTarget, ExclusionGroupAssignmentTarget]] = Field(alias="target", default=None,discriminator="odata_type", )

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
from .device_and_app_management_assignment_source import DeviceAndAppManagementAssignmentSource
from .all_devices_assignment_target import AllDevicesAssignmentTarget
from .all_licensed_users_assignment_target import AllLicensedUsersAssignmentTarget
from .android_fota_deployment_assignment_target import AndroidFotaDeploymentAssignmentTarget
from .configuration_manager_collection_assignment_target import ConfigurationManagerCollectionAssignmentTarget
from .group_assignment_target import GroupAssignmentTarget
from .exclusion_group_assignment_target import ExclusionGroupAssignmentTarget

