from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class OfficeSuiteApp(BaseModel):
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
	autoAcceptEula: Optional[bool] = Field(alias="autoAcceptEula",default=None,)
	excludedApps: Optional[ExcludedApps] = Field(alias="excludedApps",default=None,)
	installProgressDisplayLevel: Optional[OfficeSuiteInstallProgressDisplayLevel | str] = Field(alias="installProgressDisplayLevel",default=None,)
	localesToInstall: Optional[list[str]] = Field(alias="localesToInstall",default=None,)
	officeConfigurationXml: Optional[str] = Field(alias="officeConfigurationXml",default=None,)
	officePlatformArchitecture: Optional[WindowsArchitecture | str] = Field(alias="officePlatformArchitecture",default=None,)
	officeSuiteAppDefaultFileFormat: Optional[OfficeSuiteDefaultFileFormatType | str] = Field(alias="officeSuiteAppDefaultFileFormat",default=None,)
	productIds: Optional[list[OfficeProductId | str]] = Field(alias="productIds",default=None,)
	shouldUninstallOlderVersionsOfOffice: Optional[bool] = Field(alias="shouldUninstallOlderVersionsOfOffice",default=None,)
	targetVersion: Optional[str] = Field(alias="targetVersion",default=None,)
	updateChannel: Optional[OfficeUpdateChannel | str] = Field(alias="updateChannel",default=None,)
	updateVersion: Optional[str] = Field(alias="updateVersion",default=None,)
	useSharedComputerActivation: Optional[bool] = Field(alias="useSharedComputerActivation",default=None,)

from .mime_content import MimeContent
from .mobile_app_publishing_state import MobileAppPublishingState
from .mobile_app_assignment import MobileAppAssignment
from .mobile_app_category import MobileAppCategory
from .mobile_app_relationship import MobileAppRelationship
from .excluded_apps import ExcludedApps
from .office_suite_install_progress_display_level import OfficeSuiteInstallProgressDisplayLevel
from .windows_architecture import WindowsArchitecture
from .office_suite_default_file_format_type import OfficeSuiteDefaultFileFormatType
from .office_product_id import OfficeProductId
from .office_update_channel import OfficeUpdateChannel

