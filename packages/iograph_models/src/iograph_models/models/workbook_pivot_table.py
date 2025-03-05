from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookPivotTable(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	name: Optional[str] = Field(default=None,alias="name",)
	worksheet: Optional[WorkbookWorksheet] = Field(default=None,alias="worksheet",)

from .workbook_worksheet import WorkbookWorksheet

