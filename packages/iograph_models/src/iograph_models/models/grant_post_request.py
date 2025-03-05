from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class GrantPostRequest(BaseModel):
	roles: Optional[list[str]] = Field(default=None,alias="roles",)
	recipients: Optional[list[DriveRecipient]] = Field(default=None,alias="recipients",)

from .drive_recipient import DriveRecipient

