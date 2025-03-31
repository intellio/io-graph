from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AiInteractionLink(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.aiInteractionLink"] = Field(alias="@odata.type",)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	linkType: Optional[str] = Field(alias="linkType", default=None,)
	linkUrl: Optional[str] = Field(alias="linkUrl", default=None,)

