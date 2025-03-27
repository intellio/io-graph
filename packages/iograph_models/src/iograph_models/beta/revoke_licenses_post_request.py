from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Revoke_licensesPostRequest(BaseModel):
	notifyManagedDevices: Optional[bool] = Field(alias="notifyManagedDevices", default=None,)
	revokeUntrackedLicenses: Optional[bool] = Field(alias="revokeUntrackedLicenses", default=None,)


