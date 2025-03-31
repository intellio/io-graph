from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class RemoveContentFooterAction(BaseModel):
	odata_type: Literal["#microsoft.graph.removeContentFooterAction"] = Field(alias="@odata.type", default="#microsoft.graph.removeContentFooterAction")
	uiElementNames: Optional[list[str]] = Field(alias="uiElementNames", default=None,)

