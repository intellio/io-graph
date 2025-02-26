from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WorkbookTable(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	highlightFirstColumn: Optional[bool] = Field(default=None,alias="highlightFirstColumn",)
	highlightLastColumn: Optional[bool] = Field(default=None,alias="highlightLastColumn",)
	legacyId: Optional[str] = Field(default=None,alias="legacyId",)
	name: Optional[str] = Field(default=None,alias="name",)
	showBandedColumns: Optional[bool] = Field(default=None,alias="showBandedColumns",)
	showBandedRows: Optional[bool] = Field(default=None,alias="showBandedRows",)
	showFilterButton: Optional[bool] = Field(default=None,alias="showFilterButton",)
	showHeaders: Optional[bool] = Field(default=None,alias="showHeaders",)
	showTotals: Optional[bool] = Field(default=None,alias="showTotals",)
	style: Optional[str] = Field(default=None,alias="style",)
	columns: list[WorkbookTableColumn] = Field(alias="columns",)
	rows: list[WorkbookTableRow] = Field(alias="rows",)
	sort: Optional[WorkbookTableSort] = Field(default=None,alias="sort",)
	worksheet: Optional[WorkbookWorksheet] = Field(default=None,alias="worksheet",)

from .workbook_table_column import WorkbookTableColumn
from .workbook_table_row import WorkbookTableRow
from .workbook_table_sort import WorkbookTableSort
from .workbook_worksheet import WorkbookWorksheet

