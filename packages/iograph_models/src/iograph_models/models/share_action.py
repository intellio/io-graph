from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ShareAction(BaseModel):
	recipients: SerializeAsAny[Optional[list[IdentitySet]]] = Field(default=None,alias="recipients",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .identity_set import IdentitySet

