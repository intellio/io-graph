from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsInformationProtectionNetworkLearningSummary(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	deviceCount: Optional[int] = Field(alias="deviceCount",default=None,)
	url: Optional[str] = Field(alias="url",default=None,)


