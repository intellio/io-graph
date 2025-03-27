from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidDeviceOwnerDelegatedScopeAppSetting(BaseModel):
	appDetail: Optional[Union[AppleAppListItem]] = Field(alias="appDetail", default=None,discriminator="odata_type", )
	appScopes: Optional[list[AndroidDeviceOwnerDelegatedAppScopeType | str]] = Field(alias="appScopes", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .apple_app_list_item import AppleAppListItem
from .android_device_owner_delegated_app_scope_type import AndroidDeviceOwnerDelegatedAppScopeType

