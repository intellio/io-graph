from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ProtectGroup(BaseModel):
	name: Optional[str] = Field(alias="name",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	allowEmailFromGuestUsers: Optional[bool] = Field(alias="allowEmailFromGuestUsers",default=None,)
	allowGuestUsers: Optional[bool] = Field(alias="allowGuestUsers",default=None,)
	privacy: Optional[GroupPrivacy | str] = Field(alias="privacy",default=None,)

from .group_privacy import GroupPrivacy

