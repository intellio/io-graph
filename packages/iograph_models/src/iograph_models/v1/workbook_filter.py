from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WorkbookFilter(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.workbookFilter"] = Field(alias="@odata.type", default="#microsoft.graph.workbookFilter")
	criteria: Optional[WorkbookFilterCriteria] = Field(alias="criteria", default=None,)

from .workbook_filter_criteria import WorkbookFilterCriteria
