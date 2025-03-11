from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AiInteractionMention(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	mentioned: Optional[AiInteractionMentionedIdentitySet] = Field(alias="mentioned",default=None,)
	mentionId: Optional[int] = Field(alias="mentionId",default=None,)
	mentionText: Optional[str] = Field(alias="mentionText",default=None,)

from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet

