from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Force_deletePostRequest(BaseModel):
	disableUserAccounts: Optional[bool] = Field(alias="disableUserAccounts", default=None,)

