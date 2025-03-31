from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WhatIfUserActionContext(BaseModel):
	odata_type: Literal["#microsoft.graph.whatIfUserActionContext"] = Field(alias="@odata.type", default="#microsoft.graph.whatIfUserActionContext")
	userAction: Optional[UserAction | str] = Field(alias="userAction", default=None,)

from .user_action import UserAction
