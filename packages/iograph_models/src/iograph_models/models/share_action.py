from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ShareAction(BaseModel):
	recipients: list[IdentitySet] = Field(alias="recipients",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .identity_set import IdentitySet

