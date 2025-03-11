from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsInformationProtectionIPRangeCollection(BaseModel):
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	ranges: SerializeAsAny[Optional[list[IpRange]]] = Field(alias="ranges",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .ip_range import IpRange

