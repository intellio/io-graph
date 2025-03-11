from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserCountMetric(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	count: Optional[int] = Field(alias="count",default=None,)
	factDate: Optional[str] = Field(alias="factDate",default=None,)
	language: Optional[str] = Field(alias="language",default=None,)


