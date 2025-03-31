from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AiInteractionContext(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.aiInteractionContext"] = Field(alias="@odata.type",)
	contextReference: Optional[str] = Field(alias="contextReference", default=None,)
	contextType: Optional[str] = Field(alias="contextType", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)

