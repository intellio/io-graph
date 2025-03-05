from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookWorksheet(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	name: Optional[str] = Field(default=None,alias="name",)
	position: Optional[int] = Field(default=None,alias="position",)
	visibility: Optional[str] = Field(default=None,alias="visibility",)
	charts: Optional[list[WorkbookChart]] = Field(default=None,alias="charts",)
	names: Optional[list[WorkbookNamedItem]] = Field(default=None,alias="names",)
	pivotTables: Optional[list[WorkbookPivotTable]] = Field(default=None,alias="pivotTables",)
	protection: Optional[WorkbookWorksheetProtection] = Field(default=None,alias="protection",)
	tables: Optional[list[WorkbookTable]] = Field(default=None,alias="tables",)

from .workbook_chart import WorkbookChart
from .workbook_named_item import WorkbookNamedItem
from .workbook_pivot_table import WorkbookPivotTable
from .workbook_worksheet_protection import WorkbookWorksheetProtection
from .workbook_table import WorkbookTable

