from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ChatRestrictions(BaseModel):
	allowTextOnly: Optional[bool] = Field(alias="allowTextOnly", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

