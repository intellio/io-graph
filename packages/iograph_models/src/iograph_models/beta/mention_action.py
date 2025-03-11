from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MentionAction(BaseModel):
	mentionees: SerializeAsAny[Optional[list[IdentitySet]]] = Field(alias="mentionees",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .identity_set import IdentitySet

