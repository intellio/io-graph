from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DirectorySizeQuota(BaseModel):
	total: Optional[int] = Field(alias="total", default=None,)
	used: Optional[int] = Field(alias="used", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


