from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MentionAction(BaseModel):
	mentionees: SerializeAsAny[Optional[list[IdentitySet]]] = Field(default=None,alias="mentionees",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .identity_set import IdentitySet

