from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ChatRestrictions(BaseModel):
	allowTextOnly: Optional[bool] = Field(default=None,alias="allowTextOnly",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


