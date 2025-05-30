from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ContainerFilter(BaseModel):
	includedContainers: Optional[list[str]] = Field(alias="includedContainers", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

