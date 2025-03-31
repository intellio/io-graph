from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field


class WindowsUniversalAppX(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsUniversalAppX"] = Field(alias="@odata.type", default="#microsoft.graph.windowsUniversalAppX")
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
	applicableArchitectures: Optional[WindowsArchitecture | str] = Field(alias="applicableArchitectures", default=None,)
	applicableDeviceTypes: Optional[WindowsDeviceType | str] = Field(alias="applicableDeviceTypes", default=None,)
	identityName: Optional[str] = Field(alias="identityName", default=None,)
	identityPublisherHash: Optional[str] = Field(alias="identityPublisherHash", default=None,)
	identityResourceIdentifier: Optional[str] = Field(alias="identityResourceIdentifier", default=None,)
	identityVersion: Optional[str] = Field(alias="identityVersion", default=None,)
	isBundle: Optional[bool] = Field(alias="isBundle", default=None,)
	minimumSupportedOperatingSystem: Optional[WindowsMinimumOperatingSystem] = Field(alias="minimumSupportedOperatingSystem", default=None,)
	committedContainedApps: Optional[list[Annotated[Union[WindowsUniversalAppXContainedApp],Field(discriminator="odata_type")]]] = Field(alias="committedContainedApps", default=None,)

from .mime_content import MimeContent
from .mobile_app_publishing_state import MobileAppPublishingState
from .mobile_app_assignment import MobileAppAssignment
from .mobile_app_category import MobileAppCategory
from .mobile_app_content import MobileAppContent
from .windows_architecture import WindowsArchitecture
from .windows_device_type import WindowsDeviceType
from .windows_minimum_operating_system import WindowsMinimumOperatingSystem
from .windows_universal_app_x_contained_app import WindowsUniversalAppXContainedApp
