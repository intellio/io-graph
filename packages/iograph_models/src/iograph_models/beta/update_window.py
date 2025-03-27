from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UpdateWindow(BaseModel):
	updateWindowEndTime: Optional[str] = Field(alias="updateWindowEndTime", default=None,)
	updateWindowStartTime: Optional[str] = Field(alias="updateWindowStartTime", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


