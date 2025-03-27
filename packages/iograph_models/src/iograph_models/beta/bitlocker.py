from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Bitlocker(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	recoveryKeys: Optional[list[BitlockerRecoveryKey]] = Field(alias="recoveryKeys", default=None,)

from .bitlocker_recovery_key import BitlockerRecoveryKey

