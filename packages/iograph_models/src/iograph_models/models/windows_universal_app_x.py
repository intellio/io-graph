from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class WindowsUniversalAppX(BaseModel):
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
	applicableDeviceTypes: Optional[WindowsDeviceType] = Field(default=None,alias="applicableDeviceTypes",)
	identityName: Optional[str] = Field(default=None,alias="identityName",)
	identityPublisherHash: Optional[str] = Field(default=None,alias="identityPublisherHash",)
	identityResourceIdentifier: Optional[str] = Field(default=None,alias="identityResourceIdentifier",)
	identityVersion: Optional[str] = Field(default=None,alias="identityVersion",)
	isBundle: Optional[bool] = Field(default=None,alias="isBundle",)
	minimumSupportedOperatingSystem: Optional[WindowsMinimumOperatingSystem] = Field(default=None,alias="minimumSupportedOperatingSystem",)
	committedContainedApps: list[MobileContainedApp] = Field(alias="committedContainedApps",)

from .mime_content import MimeContent
from .mobile_app_publishing_state import MobileAppPublishingState
from .mobile_app_assignment import MobileAppAssignment
from .mobile_app_category import MobileAppCategory
from .mobile_app_content import MobileAppContent
from .windows_architecture import WindowsArchitecture
from .windows_device_type import WindowsDeviceType
from .windows_minimum_operating_system import WindowsMinimumOperatingSystem
from .mobile_contained_app import MobileContainedApp

