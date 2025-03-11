from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VirtualMachineDetails(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	virtualMachine: SerializeAsAny[Optional[AuthorizationSystemResource]] = Field(alias="virtualMachine",default=None,)

from .authorization_system_resource import AuthorizationSystemResource

