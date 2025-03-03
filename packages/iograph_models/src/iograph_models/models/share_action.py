from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ShareAction(BaseModel):
	recipients: Optional[list[IdentitySet]] = Field(default=None,alias="recipients",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .identity_set import IdentitySet

