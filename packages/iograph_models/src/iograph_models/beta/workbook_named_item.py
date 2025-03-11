from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookNamedItem(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	comment: Optional[str] = Field(alias="comment",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	scope: Optional[str] = Field(alias="scope",default=None,)
	type: Optional[str] = Field(alias="type",default=None,)
	value: Optional[str] = Field(alias="value",default=None,)
	visible: Optional[bool] = Field(alias="visible",default=None,)
	worksheet: Optional[WorkbookWorksheet] = Field(alias="worksheet",default=None,)

from .workbook_worksheet import WorkbookWorksheet

