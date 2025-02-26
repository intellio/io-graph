from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WorkbookFilter(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	criteria: Optional[WorkbookFilterCriteria] = Field(default=None,alias="criteria",)

from .workbook_filter_criteria import WorkbookFilterCriteria

