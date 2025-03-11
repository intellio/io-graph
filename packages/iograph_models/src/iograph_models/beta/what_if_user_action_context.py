from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WhatIfUserActionContext(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	userAction: Optional[UserAction | str] = Field(alias="userAction",default=None,)

from .user_action import UserAction

