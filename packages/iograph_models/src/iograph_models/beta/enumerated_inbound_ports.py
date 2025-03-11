from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EnumeratedInboundPorts(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	ports: Optional[list[str]] = Field(alias="ports",default=None,)


