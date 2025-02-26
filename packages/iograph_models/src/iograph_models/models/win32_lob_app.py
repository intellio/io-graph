from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class Win32LobApp(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	developer: Optional[str] = Field(default=None,alias="developer",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	informationUrl: Optional[str] = Field(default=None,alias="informationUrl",)
	isFeatured: Optional[bool] = Field(default=None,alias="isFeatured",)
	largeIcon: Optional[MimeContent] = Field(default=None,alias="largeIcon",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	notes: Optional[str] = Field(default=None,alias="notes",)
	owner: Optional[str] = Field(default=None,alias="owner",)
	privacyInformationUrl: Optional[str] = Field(default=None,alias="privacyInformationUrl",)
	publisher: Optional[str] = Field(default=None,alias="publisher",)
	publishingState: Optional[MobileAppPublishingState] = Field(default=None,alias="publishingState",)
	assignments: list[MobileAppAssignment] = Field(alias="assignments",)
	categories: list[MobileAppCategory] = Field(alias="categories",)
	committedContentVersion: Optional[str] = Field(default=None,alias="committedContentVersion",)
	fileName: Optional[str] = Field(default=None,alias="fileName",)
	size: Optional[int] = Field(default=None,alias="size",)
	contentVersions: list[MobileAppContent] = Field(alias="contentVersions",)
	applicableArchitectures: Optional[WindowsArchitecture] = Field(default=None,alias="applicableArchitectures",)
	installCommandLine: Optional[str] = Field(default=None,alias="installCommandLine",)
	installExperience: Optional[Win32LobAppInstallExperience] = Field(default=None,alias="installExperience",)
	minimumCpuSpeedInMHz: Optional[int] = Field(default=None,alias="minimumCpuSpeedInMHz",)
	minimumFreeDiskSpaceInMB: Optional[int] = Field(default=None,alias="minimumFreeDiskSpaceInMB",)
	minimumMemoryInMB: Optional[int] = Field(default=None,alias="minimumMemoryInMB",)
	minimumNumberOfProcessors: Optional[int] = Field(default=None,alias="minimumNumberOfProcessors",)
	minimumSupportedWindowsRelease: Optional[str] = Field(default=None,alias="minimumSupportedWindowsRelease",)
	msiInformation: Optional[Win32LobAppMsiInformation] = Field(default=None,alias="msiInformation",)
	returnCodes: list[Win32LobAppReturnCode] = Field(alias="returnCodes",)
	rules: list[Win32LobAppRule] = Field(alias="rules",)
	setupFilePath: Optional[str] = Field(default=None,alias="setupFilePath",)
	uninstallCommandLine: Optional[str] = Field(default=None,alias="uninstallCommandLine",)

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

