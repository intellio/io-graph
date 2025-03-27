from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookRange(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	address: Optional[str] = Field(alias="address", default=None,)
	addressLocal: Optional[str] = Field(alias="addressLocal", default=None,)
	cellCount: Optional[int] = Field(alias="cellCount", default=None,)
	columnCount: Optional[int] = Field(alias="columnCount", default=None,)
	columnHidden: Optional[bool] = Field(alias="columnHidden", default=None,)
	columnIndex: Optional[int] = Field(alias="columnIndex", default=None,)
	formulas: Optional[str] = Field(alias="formulas", default=None,)
	formulasLocal: Optional[str] = Field(alias="formulasLocal", default=None,)
	formulasR1C1: Optional[str] = Field(alias="formulasR1C1", default=None,)
	hidden: Optional[bool] = Field(alias="hidden", default=None,)
	numberFormat: Optional[str] = Field(alias="numberFormat", default=None,)
	rowCount: Optional[int] = Field(alias="rowCount", default=None,)
	rowHidden: Optional[bool] = Field(alias="rowHidden", default=None,)
	rowIndex: Optional[int] = Field(alias="rowIndex", default=None,)
	text: Optional[str] = Field(alias="text", default=None,)
	values: Optional[str] = Field(alias="values", default=None,)
	valueTypes: Optional[str] = Field(alias="valueTypes", default=None,)
	format: Optional[WorkbookRangeFormat] = Field(alias="format", default=None,)
	sort: Optional[WorkbookRangeSort] = Field(alias="sort", default=None,)
	worksheet: Optional[WorkbookWorksheet] = Field(alias="worksheet", default=None,)

from .workbook_range_format import WorkbookRangeFormat
from .workbook_range_sort import WorkbookRangeSort
from .workbook_worksheet import WorkbookWorksheet

