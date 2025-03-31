from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RequiredResourceAccess(BaseModel):
	resourceAccess: Optional[list[ResourceAccess]] = Field(alias="resourceAccess", default=None,)
	resourceAppId: Optional[str] = Field(alias="resourceAppId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .resource_access import ResourceAccess
