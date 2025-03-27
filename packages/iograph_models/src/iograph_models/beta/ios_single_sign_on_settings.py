from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class IosSingleSignOnSettings(BaseModel):
	allowedAppsList: Optional[list[Annotated[Union[AppleAppListItem]],Field(discriminator="odata_type")]]] = Field(alias="allowedAppsList", default=None,)
	allowedUrls: Optional[list[str]] = Field(alias="allowedUrls", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	kerberosPrincipalName: Optional[str] = Field(alias="kerberosPrincipalName", default=None,)
	kerberosRealm: Optional[str] = Field(alias="kerberosRealm", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .apple_app_list_item import AppleAppListItem

