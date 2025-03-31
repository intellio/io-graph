from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field


class ResourceAccess(BaseModel):
	id: Optional[UUID] = Field(alias="id", default=None,)
	type: Optional[str] = Field(alias="type", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

