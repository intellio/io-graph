from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ShareAction(BaseModel):
	recipients: SerializeAsAny[Optional[list[IdentitySet]]] = Field(alias="recipients",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .identity_set import IdentitySet

