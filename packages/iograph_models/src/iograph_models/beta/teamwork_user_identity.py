from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamworkUserIdentity(BaseModel):
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	userIdentityType: Optional[TeamworkUserIdentityType | str] = Field(alias="userIdentityType",default=None,)

from .teamwork_user_identity_type import TeamworkUserIdentityType

