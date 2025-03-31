from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ProtectGroup(BaseModel):
	name: Optional[str] = Field(alias="name", default=None,)
	odata_type: Literal["#microsoft.graph.protectGroup"] = Field(alias="@odata.type", default="#microsoft.graph.protectGroup")
	allowEmailFromGuestUsers: Optional[bool] = Field(alias="allowEmailFromGuestUsers", default=None,)
	allowGuestUsers: Optional[bool] = Field(alias="allowGuestUsers", default=None,)
	privacy: Optional[GroupPrivacy | str] = Field(alias="privacy", default=None,)

from .group_privacy import GroupPrivacy
