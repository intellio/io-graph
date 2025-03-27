from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidDeviceComplianceLocalActionLockDevice(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.androidDeviceComplianceLocalActionLockDevice"] = Field(alias="@odata.type", default="#microsoft.graph.androidDeviceComplianceLocalActionLockDevice")
	gracePeriodInMinutes: Optional[int] = Field(alias="gracePeriodInMinutes", default=None,)


