from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudRealtimeCommunicationInfo(BaseModel):
	isSipEnabled: Optional[bool] = Field(alias="isSipEnabled", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


