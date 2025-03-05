from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ContainerFilter(BaseModel):
	includedContainers: Optional[list[str]] = Field(default=None,alias="includedContainers",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


