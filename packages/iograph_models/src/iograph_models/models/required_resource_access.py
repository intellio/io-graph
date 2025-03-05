from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RequiredResourceAccess(BaseModel):
	resourceAccess: Optional[list[ResourceAccess]] = Field(default=None,alias="resourceAccess",)
	resourceAppId: Optional[str] = Field(default=None,alias="resourceAppId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .resource_access import ResourceAccess

