from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class RemoveWatermarkAction(BaseModel):
	odata_type: Literal["#microsoft.graph.removeWatermarkAction"] = Field(alias="@odata.type", default="#microsoft.graph.removeWatermarkAction")
	uiElementNames: Optional[list[str]] = Field(alias="uiElementNames", default=None,)


