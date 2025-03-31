from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class RemoveContentHeaderAction(BaseModel):
	odata_type: Literal["#microsoft.graph.removeContentHeaderAction"] = Field(alias="@odata.type", default="#microsoft.graph.removeContentHeaderAction")
	uiElementNames: Optional[list[str]] = Field(alias="uiElementNames", default=None,)

