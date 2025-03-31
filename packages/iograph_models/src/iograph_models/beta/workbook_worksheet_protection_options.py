from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WorkbookWorksheetProtectionOptions(BaseModel):
	allowAutoFilter: Optional[bool] = Field(alias="allowAutoFilter", default=None,)
	allowDeleteColumns: Optional[bool] = Field(alias="allowDeleteColumns", default=None,)
	allowDeleteRows: Optional[bool] = Field(alias="allowDeleteRows", default=None,)
	allowFormatCells: Optional[bool] = Field(alias="allowFormatCells", default=None,)
	allowFormatColumns: Optional[bool] = Field(alias="allowFormatColumns", default=None,)
	allowFormatRows: Optional[bool] = Field(alias="allowFormatRows", default=None,)
	allowInsertColumns: Optional[bool] = Field(alias="allowInsertColumns", default=None,)
	allowInsertHyperlinks: Optional[bool] = Field(alias="allowInsertHyperlinks", default=None,)
	allowInsertRows: Optional[bool] = Field(alias="allowInsertRows", default=None,)
	allowPivotTables: Optional[bool] = Field(alias="allowPivotTables", default=None,)
	allowSort: Optional[bool] = Field(alias="allowSort", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

