from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedIOSLobApp(BaseModel):
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
	appAvailability: Optional[ManagedAppAvailability] = Field(default=None,alias="appAvailability",)
	version: Optional[str] = Field(default=None,alias="version",)
	committedContentVersion: Optional[str] = Field(default=None,alias="committedContentVersion",)
	fileName: Optional[str] = Field(default=None,alias="fileName",)
	size: Optional[int] = Field(default=None,alias="size",)
	contentVersions: Optional[list[MobileAppContent]] = Field(default=None,alias="contentVersions",)
	applicableDeviceType: Optional[IosDeviceType] = Field(default=None,alias="applicableDeviceType",)
	buildNumber: Optional[str] = Field(default=None,alias="buildNumber",)
	bundleId: Optional[str] = Field(default=None,alias="bundleId",)
	expirationDateTime: Optional[datetime] = Field(default=None,alias="expirationDateTime",)
	minimumSupportedOperatingSystem: Optional[IosMinimumOperatingSystem] = Field(default=None,alias="minimumSupportedOperatingSystem",)
	versionNumber: Optional[str] = Field(default=None,alias="versionNumber",)

from .mime_content import MimeContent
from .mobile_app_publishing_state import MobileAppPublishingState
from .mobile_app_assignment import MobileAppAssignment
from .mobile_app_category import MobileAppCategory
from .managed_app_availability import ManagedAppAvailability
from .mobile_app_content import MobileAppContent
from .ios_device_type import IosDeviceType
from .ios_minimum_operating_system import IosMinimumOperatingSystem

