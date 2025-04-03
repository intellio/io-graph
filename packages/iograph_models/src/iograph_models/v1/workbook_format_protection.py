from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WorkbookFormatProtection(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.workbookFormatProtection"] = Field(alias="@odata.type", default="#microsoft.graph.workbookFormatProtection")
	formulaHidden: Optional[bool] = Field(alias="formulaHidden", default=None,)
	locked: Optional[bool] = Field(alias="locked", default=None,)

