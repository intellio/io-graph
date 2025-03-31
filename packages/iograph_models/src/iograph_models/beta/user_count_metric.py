from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UserCountMetric(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userCountMetric"] = Field(alias="@odata.type",)
	count: Optional[int] = Field(alias="count", default=None,)
	factDate: Optional[str] = Field(alias="factDate", default=None,)
	language: Optional[str] = Field(alias="language", default=None,)

