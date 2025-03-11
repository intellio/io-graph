from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AiUser(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	interactionHistory: Optional[AiInteractionHistory] = Field(alias="interactionHistory",default=None,)

from .ai_interaction_history import AiInteractionHistory

