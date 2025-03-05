from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookPivotTable(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	worksheet: Optional[WorkbookWorksheet] = Field(alias="worksheet",default=None,)

from .workbook_worksheet import WorkbookWorksheet

