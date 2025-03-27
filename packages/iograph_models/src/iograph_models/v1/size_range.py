from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SizeRange(BaseModel):
	maximumSize: Optional[int] = Field(alias="maximumSize", default=None,)
	minimumSize: Optional[int] = Field(alias="minimumSize", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


