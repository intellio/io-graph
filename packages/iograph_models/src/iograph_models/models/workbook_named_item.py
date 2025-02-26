from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WorkbookNamedItem(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	comment: Optional[str] = Field(default=None,alias="comment",)
	name: Optional[str] = Field(default=None,alias="name",)
	scope: Optional[str] = Field(default=None,alias="scope",)
	type: Optional[str] = Field(default=None,alias="type",)
	value: Optional[str] = Field(default=None,alias="value",)
	visible: Optional[bool] = Field(default=None,alias="visible",)
	worksheet: Optional[WorkbookWorksheet] = Field(default=None,alias="worksheet",)

from .workbook_worksheet import WorkbookWorksheet

