from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class GrantPostRequest(BaseModel):
	roles: Optional[list[str]] = Field(alias="roles",default=None,)
	recipients: Optional[list[DriveRecipient]] = Field(alias="recipients",default=None,)

from .drive_recipient import DriveRecipient

