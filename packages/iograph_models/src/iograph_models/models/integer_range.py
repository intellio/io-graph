from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IntegerRange(BaseModel):
	end: Optional[int] = Field(alias="end",default=None,)
	start: Optional[int] = Field(alias="start",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


