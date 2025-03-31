from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AllowedValue(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.allowedValue"] = Field(alias="@odata.type",)
	isActive: Optional[bool] = Field(alias="isActive", default=None,)

