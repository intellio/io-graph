from __future__ import annotations
from typing import Optional
from typing import Union
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class OpenNetworkAzureSecurityGroupFinding(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	inboundPorts: Optional[Union[AllInboundPorts, EnumeratedInboundPorts]] = Field(alias="inboundPorts", default=None,discriminator="odata_type", )
	securityGroup: Optional[Union[AwsAuthorizationSystemResource, AzureAuthorizationSystemResource, GcpAuthorizationSystemResource]] = Field(alias="securityGroup", default=None,discriminator="odata_type", )
	virtualMachines: Optional[list[VirtualMachineDetails]] = Field(alias="virtualMachines", default=None,)

from .all_inbound_ports import AllInboundPorts
from .enumerated_inbound_ports import EnumeratedInboundPorts
from .aws_authorization_system_resource import AwsAuthorizationSystemResource
from .azure_authorization_system_resource import AzureAuthorizationSystemResource
from .gcp_authorization_system_resource import GcpAuthorizationSystemResource
from .virtual_machine_details import VirtualMachineDetails

