from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RequiredResourceAccess(BaseModel):
	resourceAccess: list[ResourceAccess] = Field(alias="resourceAccess",)
	resourceAppId: Optional[str] = Field(default=None,alias="resourceAppId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .resource_access import ResourceAccess

