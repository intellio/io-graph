from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ConversationMemberRoleUpdatedEventMessageDetail(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	conversationMemberRoles: Optional[list[str]] = Field(alias="conversationMemberRoles",default=None,)
	conversationMemberUser: Optional[TeamworkUserIdentity] = Field(alias="conversationMemberUser",default=None,)
	initiator: SerializeAsAny[Optional[IdentitySet]] = Field(alias="initiator",default=None,)

from .teamwork_user_identity import TeamworkUserIdentity
from .identity_set import IdentitySet

