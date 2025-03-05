from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookRange(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	address: Optional[str] = Field(default=None,alias="address",)
	addressLocal: Optional[str] = Field(default=None,alias="addressLocal",)
	cellCount: Optional[int] = Field(default=None,alias="cellCount",)
	columnCount: Optional[int] = Field(default=None,alias="columnCount",)
	columnHidden: Optional[bool] = Field(default=None,alias="columnHidden",)
	columnIndex: Optional[int] = Field(default=None,alias="columnIndex",)
	formulas: Optional[str] = Field(default=None,alias="formulas",)
	formulasLocal: Optional[str] = Field(default=None,alias="formulasLocal",)
	formulasR1C1: Optional[str] = Field(default=None,alias="formulasR1C1",)
	hidden: Optional[bool] = Field(default=None,alias="hidden",)
	numberFormat: Optional[str] = Field(default=None,alias="numberFormat",)
	rowCount: Optional[int] = Field(default=None,alias="rowCount",)
	rowHidden: Optional[bool] = Field(default=None,alias="rowHidden",)
	rowIndex: Optional[int] = Field(default=None,alias="rowIndex",)
	text: Optional[str] = Field(default=None,alias="text",)
	values: Optional[str] = Field(default=None,alias="values",)
	valueTypes: Optional[str] = Field(default=None,alias="valueTypes",)
	format: Optional[WorkbookRangeFormat] = Field(default=None,alias="format",)
	sort: Optional[WorkbookRangeSort] = Field(default=None,alias="sort",)
	worksheet: Optional[WorkbookWorksheet] = Field(default=None,alias="worksheet",)

from .workbook_range_format import WorkbookRangeFormat
from .workbook_range_sort import WorkbookRangeSort
from .workbook_worksheet import WorkbookWorksheet

