from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class MacOSLobApp(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.macOSLobApp"] = Field(alias="@odata.type", default="#microsoft.graph.macOSLobApp")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	developer: Optional[str] = Field(alias="developer", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	informationUrl: Optional[str] = Field(alias="informationUrl", default=None,)
	isFeatured: Optional[bool] = Field(alias="isFeatured", default=None,)
	largeIcon: Optional[MimeContent] = Field(alias="largeIcon", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	notes: Optional[str] = Field(alias="notes", default=None,)
	owner: Optional[str] = Field(alias="owner", default=None,)
	privacyInformationUrl: Optional[str] = Field(alias="privacyInformationUrl", default=None,)
	publisher: Optional[str] = Field(alias="publisher", default=None,)
	publishingState: Optional[MobileAppPublishingState | str] = Field(alias="publishingState", default=None,)
	assignments: Optional[list[MobileAppAssignment]] = Field(alias="assignments", default=None,)
	categories: Optional[list[MobileAppCategory]] = Field(alias="categories", default=None,)
	committedContentVersion: Optional[str] = Field(alias="committedContentVersion", default=None,)
	fileName: Optional[str] = Field(alias="fileName", default=None,)
	size: Optional[int] = Field(alias="size", default=None,)
	contentVersions: Optional[list[MobileAppContent]] = Field(alias="contentVersions", default=None,)
	buildNumber: Optional[str] = Field(alias="buildNumber", default=None,)
	bundleId: Optional[str] = Field(alias="bundleId", default=None,)
	childApps: Optional[list[MacOSLobChildApp]] = Field(alias="childApps", default=None,)
	ignoreVersionDetection: Optional[bool] = Field(alias="ignoreVersionDetection", default=None,)
	installAsManaged: Optional[bool] = Field(alias="installAsManaged", default=None,)
	md5Hash: Optional[list[str]] = Field(alias="md5Hash", default=None,)
	md5HashChunkSize: Optional[int] = Field(alias="md5HashChunkSize", default=None,)
	minimumSupportedOperatingSystem: Optional[MacOSMinimumOperatingSystem] = Field(alias="minimumSupportedOperatingSystem", default=None,)
	versionNumber: Optional[str] = Field(alias="versionNumber", default=None,)

from .mime_content import MimeContent
from .mobile_app_publishing_state import MobileAppPublishingState
from .mobile_app_assignment import MobileAppAssignment
from .mobile_app_category import MobileAppCategory
from .mobile_app_content import MobileAppContent
from .mac_o_s_lob_child_app import MacOSLobChildApp
from .mac_o_s_minimum_operating_system import MacOSMinimumOperatingSystem
