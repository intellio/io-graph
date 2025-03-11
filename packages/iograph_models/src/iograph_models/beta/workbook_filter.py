from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookFilter(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	criteria: Optional[WorkbookFilterCriteria] = Field(alias="criteria",default=None,)

from .workbook_filter_criteria import WorkbookFilterCriteria

