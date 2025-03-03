from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class MacOSLobApp(BaseModel):
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
	assignments: Optional[list[MobileAppAssignment]] = Field(default=None,alias="assignments",)
	categories: Optional[list[MobileAppCategory]] = Field(default=None,alias="categories",)
	committedContentVersion: Optional[str] = Field(default=None,alias="committedContentVersion",)
	fileName: Optional[str] = Field(default=None,alias="fileName",)
	size: Optional[int] = Field(default=None,alias="size",)
	contentVersions: Optional[list[MobileAppContent]] = Field(default=None,alias="contentVersions",)
	buildNumber: Optional[str] = Field(default=None,alias="buildNumber",)
	bundleId: Optional[str] = Field(default=None,alias="bundleId",)
	childApps: Optional[list[MacOSLobChildApp]] = Field(default=None,alias="childApps",)
	ignoreVersionDetection: Optional[bool] = Field(default=None,alias="ignoreVersionDetection",)
	installAsManaged: Optional[bool] = Field(default=None,alias="installAsManaged",)
	md5Hash: Optional[list[str]] = Field(default=None,alias="md5Hash",)
	md5HashChunkSize: Optional[int] = Field(default=None,alias="md5HashChunkSize",)
	minimumSupportedOperatingSystem: Optional[MacOSMinimumOperatingSystem] = Field(default=None,alias="minimumSupportedOperatingSystem",)
	versionNumber: Optional[str] = Field(default=None,alias="versionNumber",)

from .mime_content import MimeContent
from .mobile_app_publishing_state import MobileAppPublishingState
from .mobile_app_assignment import MobileAppAssignment
from .mobile_app_category import MobileAppCategory
from .mobile_app_content import MobileAppContent
from .mac_o_s_lob_child_app import MacOSLobChildApp
from .mac_o_s_minimum_operating_system import MacOSMinimumOperatingSystem

