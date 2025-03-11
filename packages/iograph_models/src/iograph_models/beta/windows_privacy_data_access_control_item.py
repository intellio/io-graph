from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsPrivacyDataAccessControlItem(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	accessLevel: Optional[WindowsPrivacyDataAccessLevel | str] = Field(alias="accessLevel",default=None,)
	appDisplayName: Optional[str] = Field(alias="appDisplayName",default=None,)
	appPackageFamilyName: Optional[str] = Field(alias="appPackageFamilyName",default=None,)
	dataCategory: Optional[WindowsPrivacyDataCategory | str] = Field(alias="dataCategory",default=None,)

from .windows_privacy_data_access_level import WindowsPrivacyDataAccessLevel
from .windows_privacy_data_category import WindowsPrivacyDataCategory

