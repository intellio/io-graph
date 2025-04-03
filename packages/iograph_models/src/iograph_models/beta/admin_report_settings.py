from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AdminReportSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.adminReportSettings"] = Field(alias="@odata.type", default="#microsoft.graph.adminReportSettings")
	displayConcealedNames: Optional[bool] = Field(alias="displayConcealedNames", default=None,)

