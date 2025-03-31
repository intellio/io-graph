from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WorkbookPivotTable(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.workbookPivotTable"] = Field(alias="@odata.type",)
	name: Optional[str] = Field(alias="name", default=None,)
	worksheet: Optional[WorkbookWorksheet] = Field(alias="worksheet", default=None,)

from .workbook_worksheet import WorkbookWorksheet
