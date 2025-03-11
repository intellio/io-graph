from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidDeviceOwnerDelegatedScopeAppSetting(BaseModel):
	appDetail: SerializeAsAny[Optional[AppListItem]] = Field(alias="appDetail",default=None,)
	appScopes: Optional[list[AndroidDeviceOwnerDelegatedAppScopeType | str]] = Field(alias="appScopes",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .app_list_item import AppListItem
from .android_device_owner_delegated_app_scope_type import AndroidDeviceOwnerDelegatedAppScopeType

