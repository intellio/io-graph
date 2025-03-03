from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class MacOSDmgApp(BaseModel):
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
	ignoreVersionDetection: Optional[bool] = Field(default=None,alias="ignoreVersionDetection",)
	includedApps: Optional[list[MacOSIncludedApp]] = Field(default=None,alias="includedApps",)
	minimumSupportedOperatingSystem: Optional[MacOSMinimumOperatingSystem] = Field(default=None,alias="minimumSupportedOperatingSystem",)
	primaryBundleId: Optional[str] = Field(default=None,alias="primaryBundleId",)
	primaryBundleVersion: Optional[str] = Field(default=None,alias="primaryBundleVersion",)

from .mime_content import MimeContent
from .mobile_app_publishing_state import MobileAppPublishingState
from .mobile_app_assignment import MobileAppAssignment
from .mobile_app_category import MobileAppCategory
from .mobile_app_content import MobileAppContent
from .mac_o_s_included_app import MacOSIncludedApp
from .mac_o_s_minimum_operating_system import MacOSMinimumOperatingSystem

