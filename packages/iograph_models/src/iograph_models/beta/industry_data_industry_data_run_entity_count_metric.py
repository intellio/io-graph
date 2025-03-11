from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataIndustryDataRunEntityCountMetric(BaseModel):
	active: Optional[int] = Field(alias="active",default=None,)
	inactive: Optional[int] = Field(alias="inactive",default=None,)
	total: Optional[int] = Field(alias="total",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


