from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessConditionalAccessSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	signalingStatus: Optional[NetworkaccessStatus | str] = Field(alias="signalingStatus", default=None,)

from .networkaccess_status import NetworkaccessStatus

