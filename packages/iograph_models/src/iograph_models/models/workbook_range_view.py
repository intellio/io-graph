from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WorkbookRangeView(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	cellAddresses: Optional[str] = Field(default=None,alias="cellAddresses",)
	columnCount: Optional[int] = Field(default=None,alias="columnCount",)
	formulas: Optional[str] = Field(default=None,alias="formulas",)
	formulasLocal: Optional[str] = Field(default=None,alias="formulasLocal",)
	formulasR1C1: Optional[str] = Field(default=None,alias="formulasR1C1",)
	index: Optional[int] = Field(default=None,alias="index",)
	numberFormat: Optional[str] = Field(default=None,alias="numberFormat",)
	rowCount: Optional[int] = Field(default=None,alias="rowCount",)
	text: Optional[str] = Field(default=None,alias="text",)
	values: Optional[str] = Field(default=None,alias="values",)
	valueTypes: Optional[str] = Field(default=None,alias="valueTypes",)
	rows: Optional[list[WorkbookRangeView]] = Field(default=None,alias="rows",)


