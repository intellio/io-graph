from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MembersLeftEventMessageDetail(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	initiator: SerializeAsAny[Optional[IdentitySet]] = Field(alias="initiator",default=None,)
	members: Optional[list[TeamworkUserIdentity]] = Field(alias="members",default=None,)

from .identity_set import IdentitySet
from .teamwork_user_identity import TeamworkUserIdentity

