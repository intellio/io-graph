from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SecurityRemoveWatermarkAction(BaseModel):
	odata_type: Literal["#microsoft.graph.security.removeWatermarkAction"] = Field(alias="@odata.type", default="#microsoft.graph.security.removeWatermarkAction")
	uiElementNames: Optional[list[str]] = Field(alias="uiElementNames", default=None,)

