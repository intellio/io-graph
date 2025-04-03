from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AiInteractionMention(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.aiInteractionMention"] = Field(alias="@odata.type", default="#microsoft.graph.aiInteractionMention")
	mentioned: Optional[AiInteractionMentionedIdentitySet] = Field(alias="mentioned", default=None,)
	mentionId: Optional[int] = Field(alias="mentionId", default=None,)
	mentionText: Optional[str] = Field(alias="mentionText", default=None,)

from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
