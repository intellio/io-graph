from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class Bitlocker(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.bitlocker"] = Field(alias="@odata.type", default="#microsoft.graph.bitlocker")
	recoveryKeys: Optional[list[BitlockerRecoveryKey]] = Field(alias="recoveryKeys", default=None,)

from .bitlocker_recovery_key import BitlockerRecoveryKey
