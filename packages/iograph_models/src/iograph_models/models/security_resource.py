from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityResource(BaseModel):
	resource: Optional[str] = Field(default=None,alias="resource",)
	resourceType: Optional[SecurityResourceType] = Field(default=None,alias="resourceType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .security_resource_type import SecurityResourceType

