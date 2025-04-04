from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WorkbookChartLineFormat(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.workbookChartLineFormat"] = Field(alias="@odata.type", default="#microsoft.graph.workbookChartLineFormat")
	color: Optional[str] = Field(alias="color", default=None,)

