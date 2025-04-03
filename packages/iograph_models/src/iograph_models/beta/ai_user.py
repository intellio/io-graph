from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AiUser(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.aiUser"] = Field(alias="@odata.type", default="#microsoft.graph.aiUser")
	interactionHistory: Optional[AiInteractionHistory] = Field(alias="interactionHistory", default=None,)

from .ai_interaction_history import AiInteractionHistory
