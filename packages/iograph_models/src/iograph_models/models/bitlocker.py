from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Bitlocker(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	recoveryKeys: list[BitlockerRecoveryKey] = Field(alias="recoveryKeys",)

from .bitlocker_recovery_key import BitlockerRecoveryKey

