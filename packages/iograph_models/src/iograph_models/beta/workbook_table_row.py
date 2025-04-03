from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WorkbookTableRow(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.workbookTableRow"] = Field(alias="@odata.type", default="#microsoft.graph.workbookTableRow")
	index: Optional[int] = Field(alias="index", default=None,)
	values: Optional[str] = Field(alias="values", default=None,)

