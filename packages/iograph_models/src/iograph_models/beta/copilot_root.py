from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CopilotRoot(BaseModel):
	admin: Optional[CopilotAdmin] = Field(alias="admin", default=None,)
	interactionHistory: Optional[AiInteractionHistory] = Field(alias="interactionHistory", default=None,)
	users: Optional[list[AiUser]] = Field(alias="users", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .copilot_admin import CopilotAdmin
from .ai_interaction_history import AiInteractionHistory
from .ai_user import AiUser
