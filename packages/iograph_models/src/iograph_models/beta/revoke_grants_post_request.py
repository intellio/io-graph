from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Revoke_grantsPostRequest(BaseModel):
	grantees: Optional[list[DriveRecipient]] = Field(alias="grantees",default=None,)

from .drive_recipient import DriveRecipient

