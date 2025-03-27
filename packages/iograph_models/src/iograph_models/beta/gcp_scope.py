from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class GcpScope(BaseModel):
	resourceType: Optional[str] = Field(alias="resourceType", default=None,)
	service: Optional[AuthorizationSystemTypeService] = Field(alias="service", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .authorization_system_type_service import AuthorizationSystemTypeService

