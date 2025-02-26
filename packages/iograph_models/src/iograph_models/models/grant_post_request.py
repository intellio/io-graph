from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class GrantPostRequest(BaseModel):
	roles: list[Optional[str]] = Field(alias="roles",)
	recipients: list[DriveRecipient] = Field(alias="recipients",)

from .drive_recipient import DriveRecipient

