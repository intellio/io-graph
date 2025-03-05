from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookWorksheetProtectionOptions(BaseModel):
	allowAutoFilter: Optional[bool] = Field(default=None,alias="allowAutoFilter",)
	allowDeleteColumns: Optional[bool] = Field(default=None,alias="allowDeleteColumns",)
	allowDeleteRows: Optional[bool] = Field(default=None,alias="allowDeleteRows",)
	allowFormatCells: Optional[bool] = Field(default=None,alias="allowFormatCells",)
	allowFormatColumns: Optional[bool] = Field(default=None,alias="allowFormatColumns",)
	allowFormatRows: Optional[bool] = Field(default=None,alias="allowFormatRows",)
	allowInsertColumns: Optional[bool] = Field(default=None,alias="allowInsertColumns",)
	allowInsertHyperlinks: Optional[bool] = Field(default=None,alias="allowInsertHyperlinks",)
	allowInsertRows: Optional[bool] = Field(default=None,alias="allowInsertRows",)
	allowPivotTables: Optional[bool] = Field(default=None,alias="allowPivotTables",)
	allowSort: Optional[bool] = Field(default=None,alias="allowSort",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


