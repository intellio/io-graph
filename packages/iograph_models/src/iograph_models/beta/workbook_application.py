from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WorkbookApplication(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.workbookApplication"] = Field(alias="@odata.type",)
	calculationMode: Optional[str] = Field(alias="calculationMode", default=None,)

