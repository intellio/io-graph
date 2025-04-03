from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WorkbookRangeBorder(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.workbookRangeBorder"] = Field(alias="@odata.type", default="#microsoft.graph.workbookRangeBorder")
	color: Optional[str] = Field(alias="color", default=None,)
	sideIndex: Optional[str] = Field(alias="sideIndex", default=None,)
	style: Optional[str] = Field(alias="style", default=None,)
	weight: Optional[str] = Field(alias="weight", default=None,)

