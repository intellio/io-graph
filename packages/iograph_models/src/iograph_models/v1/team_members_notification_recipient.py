from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class TeamMembersNotificationRecipient(BaseModel):
	odata_type: Literal["#microsoft.graph.teamMembersNotificationRecipient"] = Field(alias="@odata.type", default="#microsoft.graph.teamMembersNotificationRecipient")
	teamId: Optional[str] = Field(alias="teamId", default=None,)

