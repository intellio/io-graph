from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class OpenNetworkAzureSecurityGroupFinding(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	inboundPorts: SerializeAsAny[Optional[InboundPorts]] = Field(alias="inboundPorts",default=None,)
	securityGroup: SerializeAsAny[Optional[AuthorizationSystemResource]] = Field(alias="securityGroup",default=None,)
	virtualMachines: Optional[list[VirtualMachineDetails]] = Field(alias="virtualMachines",default=None,)

from .inbound_ports import InboundPorts
from .authorization_system_resource import AuthorizationSystemResource
from .virtual_machine_details import VirtualMachineDetails

