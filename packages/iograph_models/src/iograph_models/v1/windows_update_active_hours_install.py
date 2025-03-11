from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdateActiveHoursInstall(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	activeHoursEnd: Optional[str] = Field(alias="activeHoursEnd",default=None,)
	activeHoursStart: Optional[str] = Field(alias="activeHoursStart",default=None,)


