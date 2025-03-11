from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ConditionalAccessDeviceStates(BaseModel):
	excludeStates: Optional[list[str]] = Field(alias="excludeStates",default=None,)
	includeStates: Optional[list[str]] = Field(alias="includeStates",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


