from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ActionSummary(BaseModel):
	assigned: Optional[int] = Field(alias="assigned", default=None,)
	available: Optional[int] = Field(alias="available", default=None,)
	exercised: Optional[int] = Field(alias="exercised", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


