from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Win32LobApp(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	developer: Optional[str] = Field(alias="developer",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	informationUrl: Optional[str] = Field(alias="informationUrl",default=None,)
	isFeatured: Optional[bool] = Field(alias="isFeatured",default=None,)
	largeIcon: Optional[MimeContent] = Field(alias="largeIcon",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	notes: Optional[str] = Field(alias="notes",default=None,)
	owner: Optional[str] = Field(alias="owner",default=None,)
	privacyInformationUrl: Optional[str] = Field(alias="privacyInformationUrl",default=None,)
	publisher: Optional[str] = Field(alias="publisher",default=None,)
	publishingState: Optional[str | MobileAppPublishingState] = Field(alias="publishingState",default=None,)
	assignments: Optional[list[MobileAppAssignment]] = Field(alias="assignments",default=None,)
	categories: Optional[list[MobileAppCategory]] = Field(alias="categories",default=None,)
	committedContentVersion: Optional[str] = Field(alias="committedContentVersion",default=None,)
	fileName: Optional[str] = Field(alias="fileName",default=None,)
	size: Optional[int] = Field(alias="size",default=None,)
	contentVersions: Optional[list[MobileAppContent]] = Field(alias="contentVersions",default=None,)
	applicableArchitectures: Optional[str | WindowsArchitecture] = Field(alias="applicableArchitectures",default=None,)
	installCommandLine: Optional[str] = Field(alias="installCommandLine",default=None,)
	installExperience: Optional[Win32LobAppInstallExperience] = Field(alias="installExperience",default=None,)
	minimumCpuSpeedInMHz: Optional[int] = Field(alias="minimumCpuSpeedInMHz",default=None,)
	minimumFreeDiskSpaceInMB: Optional[int] = Field(alias="minimumFreeDiskSpaceInMB",default=None,)
	minimumMemoryInMB: Optional[int] = Field(alias="minimumMemoryInMB",default=None,)
	minimumNumberOfProcessors: Optional[int] = Field(alias="minimumNumberOfProcessors",default=None,)
	minimumSupportedWindowsRelease: Optional[str] = Field(alias="minimumSupportedWindowsRelease",default=None,)
	msiInformation: Optional[Win32LobAppMsiInformation] = Field(alias="msiInformation",default=None,)
	returnCodes: Optional[list[Win32LobAppReturnCode]] = Field(alias="returnCodes",default=None,)
	rules: SerializeAsAny[Optional[list[Win32LobAppRule]]] = Field(alias="rules",default=None,)
	setupFilePath: Optional[str] = Field(alias="setupFilePath",default=None,)
	uninstallCommandLine: Optional[str] = Field(alias="uninstallCommandLine",default=None,)

from .mime_content import MimeContent
from .mobile_app_publishing_state import MobileAppPublishingState
from .mobile_app_assignment import MobileAppAssignment
from .mobile_app_category import MobileAppCategory
from .mobile_app_content import MobileAppContent
from .windows_architecture import WindowsArchitecture
from .win32_lob_app_install_experience import Win32LobAppInstallExperience
from .win32_lob_app_msi_information import Win32LobAppMsiInformation
from .win32_lob_app_return_code import Win32LobAppReturnCode
from .win32_lob_app_rule import Win32LobAppRule

