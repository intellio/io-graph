from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Win32LobApp(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	dependentAppCount: Optional[int] = Field(alias="dependentAppCount",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	developer: Optional[str] = Field(alias="developer",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	informationUrl: Optional[str] = Field(alias="informationUrl",default=None,)
	isAssigned: Optional[bool] = Field(alias="isAssigned",default=None,)
	isFeatured: Optional[bool] = Field(alias="isFeatured",default=None,)
	largeIcon: Optional[MimeContent] = Field(alias="largeIcon",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	notes: Optional[str] = Field(alias="notes",default=None,)
	owner: Optional[str] = Field(alias="owner",default=None,)
	privacyInformationUrl: Optional[str] = Field(alias="privacyInformationUrl",default=None,)
	publisher: Optional[str] = Field(alias="publisher",default=None,)
	publishingState: Optional[MobileAppPublishingState | str] = Field(alias="publishingState",default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds",default=None,)
	supersededAppCount: Optional[int] = Field(alias="supersededAppCount",default=None,)
	supersedingAppCount: Optional[int] = Field(alias="supersedingAppCount",default=None,)
	uploadState: Optional[int] = Field(alias="uploadState",default=None,)
	assignments: Optional[list[MobileAppAssignment]] = Field(alias="assignments",default=None,)
	categories: Optional[list[MobileAppCategory]] = Field(alias="categories",default=None,)
	relationships: SerializeAsAny[Optional[list[MobileAppRelationship]]] = Field(alias="relationships",default=None,)
	committedContentVersion: Optional[str] = Field(alias="committedContentVersion",default=None,)
	fileName: Optional[str] = Field(alias="fileName",default=None,)
	size: Optional[int] = Field(alias="size",default=None,)
	contentVersions: Optional[list[MobileAppContent]] = Field(alias="contentVersions",default=None,)
	allowAvailableUninstall: Optional[bool] = Field(alias="allowAvailableUninstall",default=None,)
	applicableArchitectures: Optional[WindowsArchitecture | str] = Field(alias="applicableArchitectures",default=None,)
	detectionRules: SerializeAsAny[Optional[list[Win32LobAppDetection]]] = Field(alias="detectionRules",default=None,)
	displayVersion: Optional[str] = Field(alias="displayVersion",default=None,)
	installCommandLine: Optional[str] = Field(alias="installCommandLine",default=None,)
	installExperience: Optional[Win32LobAppInstallExperience] = Field(alias="installExperience",default=None,)
	minimumCpuSpeedInMHz: Optional[int] = Field(alias="minimumCpuSpeedInMHz",default=None,)
	minimumFreeDiskSpaceInMB: Optional[int] = Field(alias="minimumFreeDiskSpaceInMB",default=None,)
	minimumMemoryInMB: Optional[int] = Field(alias="minimumMemoryInMB",default=None,)
	minimumNumberOfProcessors: Optional[int] = Field(alias="minimumNumberOfProcessors",default=None,)
	minimumSupportedOperatingSystem: Optional[WindowsMinimumOperatingSystem] = Field(alias="minimumSupportedOperatingSystem",default=None,)
	minimumSupportedWindowsRelease: Optional[str] = Field(alias="minimumSupportedWindowsRelease",default=None,)
	msiInformation: Optional[Win32LobAppMsiInformation] = Field(alias="msiInformation",default=None,)
	requirementRules: SerializeAsAny[Optional[list[Win32LobAppRequirement]]] = Field(alias="requirementRules",default=None,)
	returnCodes: Optional[list[Win32LobAppReturnCode]] = Field(alias="returnCodes",default=None,)
	rules: SerializeAsAny[Optional[list[Win32LobAppRule]]] = Field(alias="rules",default=None,)
	setupFilePath: Optional[str] = Field(alias="setupFilePath",default=None,)
	uninstallCommandLine: Optional[str] = Field(alias="uninstallCommandLine",default=None,)

	@model_validator(mode="wrap")
	def convert_discriminator_class(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
		try:
			# check with parent model to catch any errors
			parent_validated_model = handler(data)
			# check if the discriminator field is present
			if "@odata.type" not in data:
				return parent_validated_model
			# get the discriminator value
			mapping_key = data["@odata.type"]
			if mapping_key == "#microsoft.graph.win32CatalogApp":
				from .win32_catalog_app import Win32CatalogApp
				return Win32CatalogApp.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .mime_content import MimeContent
from .mobile_app_publishing_state import MobileAppPublishingState
from .mobile_app_assignment import MobileAppAssignment
from .mobile_app_category import MobileAppCategory
from .mobile_app_relationship import MobileAppRelationship
from .mobile_app_content import MobileAppContent
from .windows_architecture import WindowsArchitecture
from .win32_lob_app_detection import Win32LobAppDetection
from .win32_lob_app_install_experience import Win32LobAppInstallExperience
from .windows_minimum_operating_system import WindowsMinimumOperatingSystem
from .win32_lob_app_msi_information import Win32LobAppMsiInformation
from .win32_lob_app_requirement import Win32LobAppRequirement
from .win32_lob_app_return_code import Win32LobAppReturnCode
from .win32_lob_app_rule import Win32LobAppRule

