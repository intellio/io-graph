from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WorkbookWorksheet(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.workbookWorksheet"] = Field(alias="@odata.type", default="#microsoft.graph.workbookWorksheet")
	name: Optional[str] = Field(alias="name", default=None,)
	position: Optional[int] = Field(alias="position", default=None,)
	visibility: Optional[str] = Field(alias="visibility", default=None,)
	charts: Optional[list[WorkbookChart]] = Field(alias="charts", default=None,)
	names: Optional[list[WorkbookNamedItem]] = Field(alias="names", default=None,)
	pivotTables: Optional[list[WorkbookPivotTable]] = Field(alias="pivotTables", default=None,)
	protection: Optional[WorkbookWorksheetProtection] = Field(alias="protection", default=None,)
	tables: Optional[list[WorkbookTable]] = Field(alias="tables", default=None,)
	tasks: Optional[list[WorkbookDocumentTask]] = Field(alias="tasks", default=None,)

from .workbook_chart import WorkbookChart
from .workbook_named_item import WorkbookNamedItem
from .workbook_pivot_table import WorkbookPivotTable
from .workbook_worksheet_protection import WorkbookWorksheetProtection
from .workbook_table import WorkbookTable
from .workbook_document_task import WorkbookDocumentTask
