from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class AndroidStoreApp(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.androidStoreApp"] = Field(alias="@odata.type", default="#microsoft.graph.androidStoreApp")
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
	appStoreUrl: Optional[str] = Field(alias="appStoreUrl", default=None,)
	minimumSupportedOperatingSystem: Optional[AndroidMinimumOperatingSystem] = Field(alias="minimumSupportedOperatingSystem", default=None,)
	packageId: Optional[str] = Field(alias="packageId", default=None,)

from .mime_content import MimeContent
from .mobile_app_publishing_state import MobileAppPublishingState
from .mobile_app_assignment import MobileAppAssignment
from .mobile_app_category import MobileAppCategory
from .android_minimum_operating_system import AndroidMinimumOperatingSystem
