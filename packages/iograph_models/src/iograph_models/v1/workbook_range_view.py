from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WorkbookRangeView(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.workbookRangeView"] = Field(alias="@odata.type", default="#microsoft.graph.workbookRangeView")
	cellAddresses: Optional[str] = Field(alias="cellAddresses", default=None,)
	columnCount: Optional[int] = Field(alias="columnCount", default=None,)
	formulas: Optional[str] = Field(alias="formulas", default=None,)
	formulasLocal: Optional[str] = Field(alias="formulasLocal", default=None,)
	formulasR1C1: Optional[str] = Field(alias="formulasR1C1", default=None,)
	index: Optional[int] = Field(alias="index", default=None,)
	numberFormat: Optional[str] = Field(alias="numberFormat", default=None,)
	rowCount: Optional[int] = Field(alias="rowCount", default=None,)
	text: Optional[str] = Field(alias="text", default=None,)
	values: Optional[str] = Field(alias="values", default=None,)
	valueTypes: Optional[str] = Field(alias="valueTypes", default=None,)
	rows: Optional[list[WorkbookRangeView]] = Field(alias="rows", default=None,)

