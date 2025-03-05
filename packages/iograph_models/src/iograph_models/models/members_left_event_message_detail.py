from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MembersLeftEventMessageDetail(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	initiator: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="initiator",)
	members: Optional[list[TeamworkUserIdentity]] = Field(default=None,alias="members",)

from .identity_set import IdentitySet
from .teamwork_user_identity import TeamworkUserIdentity

