from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CallParticipantInfo(BaseModel):
	participant: SerializeAsAny[Optional[IdentitySet]] = Field(alias="participant",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .identity_set import IdentitySet

