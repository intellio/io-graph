from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class MacOSDmgApp(BaseModel):
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
	publishingState: Optional[MobileAppPublishingState | str] = Field(alias="publishingState",default=None,)
	assignments: Optional[list[MobileAppAssignment]] = Field(alias="assignments",default=None,)
	categories: Optional[list[MobileAppCategory]] = Field(alias="categories",default=None,)
	committedContentVersion: Optional[str] = Field(alias="committedContentVersion",default=None,)
	fileName: Optional[str] = Field(alias="fileName",default=None,)
	size: Optional[int] = Field(alias="size",default=None,)
	contentVersions: Optional[list[MobileAppContent]] = Field(alias="contentVersions",default=None,)
	ignoreVersionDetection: Optional[bool] = Field(alias="ignoreVersionDetection",default=None,)
	includedApps: Optional[list[MacOSIncludedApp]] = Field(alias="includedApps",default=None,)
	minimumSupportedOperatingSystem: Optional[MacOSMinimumOperatingSystem] = Field(alias="minimumSupportedOperatingSystem",default=None,)
	primaryBundleId: Optional[str] = Field(alias="primaryBundleId",default=None,)
	primaryBundleVersion: Optional[str] = Field(alias="primaryBundleVersion",default=None,)

from .mime_content import MimeContent
from .mobile_app_publishing_state import MobileAppPublishingState
from .mobile_app_assignment import MobileAppAssignment
from .mobile_app_category import MobileAppCategory
from .mobile_app_content import MobileAppContent
from .mac_o_s_included_app import MacOSIncludedApp
from .mac_o_s_minimum_operating_system import MacOSMinimumOperatingSystem

