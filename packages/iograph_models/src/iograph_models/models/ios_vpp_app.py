from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class IosVppApp(BaseModel):
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
	applicableDeviceType: Optional[IosDeviceType] = Field(alias="applicableDeviceType",default=None,)
	appStoreUrl: Optional[str] = Field(alias="appStoreUrl",default=None,)
	bundleId: Optional[str] = Field(alias="bundleId",default=None,)
	licensingType: Optional[VppLicensingType] = Field(alias="licensingType",default=None,)
	releaseDateTime: Optional[datetime] = Field(alias="releaseDateTime",default=None,)
	totalLicenseCount: Optional[int] = Field(alias="totalLicenseCount",default=None,)
	usedLicenseCount: Optional[int] = Field(alias="usedLicenseCount",default=None,)
	vppTokenAccountType: Optional[str | VppTokenAccountType] = Field(alias="vppTokenAccountType",default=None,)
	vppTokenAppleId: Optional[str] = Field(alias="vppTokenAppleId",default=None,)
	vppTokenOrganizationName: Optional[str] = Field(alias="vppTokenOrganizationName",default=None,)

from .mime_content import MimeContent
from .mobile_app_publishing_state import MobileAppPublishingState
from .mobile_app_assignment import MobileAppAssignment
from .mobile_app_category import MobileAppCategory
from .ios_device_type import IosDeviceType
from .vpp_licensing_type import VppLicensingType
from .vpp_token_account_type import VppTokenAccountType

