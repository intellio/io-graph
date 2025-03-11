from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookTable(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	highlightFirstColumn: Optional[bool] = Field(alias="highlightFirstColumn",default=None,)
	highlightLastColumn: Optional[bool] = Field(alias="highlightLastColumn",default=None,)
	legacyId: Optional[str] = Field(alias="legacyId",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	showBandedColumns: Optional[bool] = Field(alias="showBandedColumns",default=None,)
	showBandedRows: Optional[bool] = Field(alias="showBandedRows",default=None,)
	showFilterButton: Optional[bool] = Field(alias="showFilterButton",default=None,)
	showHeaders: Optional[bool] = Field(alias="showHeaders",default=None,)
	showTotals: Optional[bool] = Field(alias="showTotals",default=None,)
	style: Optional[str] = Field(alias="style",default=None,)
	columns: Optional[list[WorkbookTableColumn]] = Field(alias="columns",default=None,)
	rows: Optional[list[WorkbookTableRow]] = Field(alias="rows",default=None,)
	sort: Optional[WorkbookTableSort] = Field(alias="sort",default=None,)
	worksheet: Optional[WorkbookWorksheet] = Field(alias="worksheet",default=None,)

from .workbook_table_column import WorkbookTableColumn
from .workbook_table_row import WorkbookTableRow
from .workbook_table_sort import WorkbookTableSort
from .workbook_worksheet import WorkbookWorksheet

