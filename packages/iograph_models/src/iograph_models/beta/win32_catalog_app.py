from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Win32CatalogApp(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.win32CatalogApp"] = Field(alias="@odata.type", default="#microsoft.graph.win32CatalogApp")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	dependentAppCount: Optional[int] = Field(alias="dependentAppCount", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	developer: Optional[str] = Field(alias="developer", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	informationUrl: Optional[str] = Field(alias="informationUrl", default=None,)
	isAssigned: Optional[bool] = Field(alias="isAssigned", default=None,)
	isFeatured: Optional[bool] = Field(alias="isFeatured", default=None,)
	largeIcon: Optional[MimeContent] = Field(alias="largeIcon", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	notes: Optional[str] = Field(alias="notes", default=None,)
	owner: Optional[str] = Field(alias="owner", default=None,)
	privacyInformationUrl: Optional[str] = Field(alias="privacyInformationUrl", default=None,)
	publisher: Optional[str] = Field(alias="publisher", default=None,)
	publishingState: Optional[MobileAppPublishingState | str] = Field(alias="publishingState", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	supersededAppCount: Optional[int] = Field(alias="supersededAppCount", default=None,)
	supersedingAppCount: Optional[int] = Field(alias="supersedingAppCount", default=None,)
	uploadState: Optional[int] = Field(alias="uploadState", default=None,)
	assignments: Optional[list[MobileAppAssignment]] = Field(alias="assignments", default=None,)
	categories: Optional[list[MobileAppCategory]] = Field(alias="categories", default=None,)
	relationships: Optional[list[Annotated[Union[MobileAppDependency, MobileAppSupersedence]],Field(discriminator="odata_type")]]] = Field(alias="relationships", default=None,)
	committedContentVersion: Optional[str] = Field(alias="committedContentVersion", default=None,)
	fileName: Optional[str] = Field(alias="fileName", default=None,)
	size: Optional[int] = Field(alias="size", default=None,)
	contentVersions: Optional[list[MobileAppContent]] = Field(alias="contentVersions", default=None,)
	allowAvailableUninstall: Optional[bool] = Field(alias="allowAvailableUninstall", default=None,)
	applicableArchitectures: Optional[WindowsArchitecture | str] = Field(alias="applicableArchitectures", default=None,)
	detectionRules: Optional[list[Annotated[Union[Win32LobAppFileSystemDetection, Win32LobAppPowerShellScriptDetection, Win32LobAppProductCodeDetection, Win32LobAppRegistryDetection]],Field(discriminator="odata_type")]]] = Field(alias="detectionRules", default=None,)
	displayVersion: Optional[str] = Field(alias="displayVersion", default=None,)
	installCommandLine: Optional[str] = Field(alias="installCommandLine", default=None,)
	installExperience: Optional[Win32LobAppInstallExperience] = Field(alias="installExperience", default=None,)
	minimumCpuSpeedInMHz: Optional[int] = Field(alias="minimumCpuSpeedInMHz", default=None,)
	minimumFreeDiskSpaceInMB: Optional[int] = Field(alias="minimumFreeDiskSpaceInMB", default=None,)
	minimumMemoryInMB: Optional[int] = Field(alias="minimumMemoryInMB", default=None,)
	minimumNumberOfProcessors: Optional[int] = Field(alias="minimumNumberOfProcessors", default=None,)
	minimumSupportedOperatingSystem: Optional[WindowsMinimumOperatingSystem] = Field(alias="minimumSupportedOperatingSystem", default=None,)
	minimumSupportedWindowsRelease: Optional[str] = Field(alias="minimumSupportedWindowsRelease", default=None,)
	msiInformation: Optional[Win32LobAppMsiInformation] = Field(alias="msiInformation", default=None,)
	requirementRules: Optional[list[Annotated[Union[Win32LobAppFileSystemRequirement, Win32LobAppPowerShellScriptRequirement, Win32LobAppRegistryRequirement]],Field(discriminator="odata_type")]]] = Field(alias="requirementRules", default=None,)
	returnCodes: Optional[list[Win32LobAppReturnCode]] = Field(alias="returnCodes", default=None,)
	rules: Optional[list[Annotated[Union[Win32LobAppFileSystemRule, Win32LobAppPowerShellScriptRule, Win32LobAppProductCodeRule, Win32LobAppRegistryRule]],Field(discriminator="odata_type")]]] = Field(alias="rules", default=None,)
	setupFilePath: Optional[str] = Field(alias="setupFilePath", default=None,)
	uninstallCommandLine: Optional[str] = Field(alias="uninstallCommandLine", default=None,)
	mobileAppCatalogPackageId: Optional[str] = Field(alias="mobileAppCatalogPackageId", default=None,)
	latestUpgradeCatalogPackage: Optional[Union[Win32MobileAppCatalogPackage]] = Field(alias="latestUpgradeCatalogPackage", default=None,discriminator="odata_type", )
	referencedCatalogPackage: Optional[Union[Win32MobileAppCatalogPackage]] = Field(alias="referencedCatalogPackage", default=None,discriminator="odata_type", )

from .mime_content import MimeContent
from .mobile_app_publishing_state import MobileAppPublishingState
from .mobile_app_assignment import MobileAppAssignment
from .mobile_app_category import MobileAppCategory
from .mobile_app_dependency import MobileAppDependency
from .mobile_app_supersedence import MobileAppSupersedence
from .mobile_app_content import MobileAppContent
from .windows_architecture import WindowsArchitecture
from .win32_lob_app_file_system_detection import Win32LobAppFileSystemDetection
from .win32_lob_app_power_shell_script_detection import Win32LobAppPowerShellScriptDetection
from .win32_lob_app_product_code_detection import Win32LobAppProductCodeDetection
from .win32_lob_app_registry_detection import Win32LobAppRegistryDetection
from .win32_lob_app_install_experience import Win32LobAppInstallExperience
from .windows_minimum_operating_system import WindowsMinimumOperatingSystem
from .win32_lob_app_msi_information import Win32LobAppMsiInformation
from .win32_lob_app_file_system_requirement import Win32LobAppFileSystemRequirement
from .win32_lob_app_power_shell_script_requirement import Win32LobAppPowerShellScriptRequirement
from .win32_lob_app_registry_requirement import Win32LobAppRegistryRequirement
from .win32_lob_app_return_code import Win32LobAppReturnCode
from .win32_lob_app_file_system_rule import Win32LobAppFileSystemRule
from .win32_lob_app_power_shell_script_rule import Win32LobAppPowerShellScriptRule
from .win32_lob_app_product_code_rule import Win32LobAppProductCodeRule
from .win32_lob_app_registry_rule import Win32LobAppRegistryRule
from .win32_mobile_app_catalog_package import Win32MobileAppCatalogPackage
from .win32_mobile_app_catalog_package import Win32MobileAppCatalogPackage

