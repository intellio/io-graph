from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ApplyPostRequest(BaseModel):
	fields: Optional[list[WorkbookSortField]] = Field(default=None,alias="fields",)
	matchCase: Optional[bool] = Field(default=None,alias="matchCase",)
	method: Optional[str] = Field(default=None,alias="method",)

from .workbook_sort_field import WorkbookSortField

