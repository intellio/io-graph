from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AssignedComputeInstanceDetails(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	accessedStorageBuckets: SerializeAsAny[Optional[list[AuthorizationSystemResource]]] = Field(alias="accessedStorageBuckets",default=None,)
	assignedComputeInstance: SerializeAsAny[Optional[AuthorizationSystemResource]] = Field(alias="assignedComputeInstance",default=None,)

from .authorization_system_resource import AuthorizationSystemResource
from .authorization_system_resource import AuthorizationSystemResource

