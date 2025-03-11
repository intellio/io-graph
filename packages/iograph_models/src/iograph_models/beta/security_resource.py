from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityResource(BaseModel):
	resource: Optional[str] = Field(alias="resource",default=None,)
	resourceType: Optional[SecurityResourceType | str] = Field(alias="resourceType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .security_resource_type import SecurityResourceType

