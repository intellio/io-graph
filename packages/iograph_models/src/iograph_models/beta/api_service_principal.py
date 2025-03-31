from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ApiServicePrincipal(BaseModel):
	resourceSpecificApplicationPermissions: Optional[list[ResourceSpecificPermission]] = Field(alias="resourceSpecificApplicationPermissions", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .resource_specific_permission import ResourceSpecificPermission
