from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ConversationMemberRoleUpdatedEventMessageDetail(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	conversationMemberRoles: Optional[list[str]] = Field(default=None,alias="conversationMemberRoles",)
	conversationMemberUser: Optional[TeamworkUserIdentity] = Field(default=None,alias="conversationMemberUser",)
	initiator: Optional[IdentitySet] = Field(default=None,alias="initiator",)

from .teamwork_user_identity import TeamworkUserIdentity
from .identity_set import IdentitySet

