from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AgentReference(BaseModel):
	path: Optional[str] = Field(alias="path", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

