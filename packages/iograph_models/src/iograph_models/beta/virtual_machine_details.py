from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class VirtualMachineDetails(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.virtualMachineDetails"] = Field(alias="@odata.type", default="#microsoft.graph.virtualMachineDetails")
	virtualMachine: Optional[Union[AwsAuthorizationSystemResource, AzureAuthorizationSystemResource, GcpAuthorizationSystemResource]] = Field(alias="virtualMachine", default=None,discriminator="odata_type", )

from .aws_authorization_system_resource import AwsAuthorizationSystemResource
from .azure_authorization_system_resource import AzureAuthorizationSystemResource
from .gcp_authorization_system_resource import GcpAuthorizationSystemResource
