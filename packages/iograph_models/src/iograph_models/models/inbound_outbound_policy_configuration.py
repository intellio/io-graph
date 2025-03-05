from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class InboundOutboundPolicyConfiguration(BaseModel):
	inboundAllowed: Optional[bool] = Field(default=None,alias="inboundAllowed",)
	outboundAllowed: Optional[bool] = Field(default=None,alias="outboundAllowed",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


