from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WorkbookTableSort(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	fields: list[WorkbookSortField] = Field(alias="fields",)
	matchCase: Optional[bool] = Field(default=None,alias="matchCase",)
	method: Optional[str] = Field(default=None,alias="method",)

from .workbook_sort_field import WorkbookSortField

