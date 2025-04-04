from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ConnectionInfo(BaseModel):
	url: Optional[str] = Field(alias="url", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

