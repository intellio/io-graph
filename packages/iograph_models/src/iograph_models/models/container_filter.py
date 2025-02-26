from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ContainerFilter(BaseModel):
	includedContainers: list[Optional[str]] = Field(alias="includedContainers",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


