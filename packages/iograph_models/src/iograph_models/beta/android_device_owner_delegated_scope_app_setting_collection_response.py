from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AndroidDeviceOwnerDelegatedScopeAppSettingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AndroidDeviceOwnerDelegatedScopeAppSetting]] = Field(alias="value", default=None,)

from .android_device_owner_delegated_scope_app_setting import AndroidDeviceOwnerDelegatedScopeAppSetting
