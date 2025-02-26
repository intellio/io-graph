from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WorkbookWorksheet(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	name: Optional[str] = Field(default=None,alias="name",)
	position: Optional[int] = Field(default=None,alias="position",)
	visibility: Optional[str] = Field(default=None,alias="visibility",)
	charts: list[WorkbookChart] = Field(alias="charts",)
	names: list[WorkbookNamedItem] = Field(alias="names",)
	pivotTables: list[WorkbookPivotTable] = Field(alias="pivotTables",)
	protection: Optional[WorkbookWorksheetProtection] = Field(default=None,alias="protection",)
	tables: list[WorkbookTable] = Field(alias="tables",)

from .workbook_chart import WorkbookChart
from .workbook_named_item import WorkbookNamedItem
from .workbook_pivot_table import WorkbookPivotTable
from .workbook_worksheet_protection import WorkbookWorksheetProtection
from .workbook_table import WorkbookTable

