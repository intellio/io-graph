from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class OpenAwsSecurityGroupFinding(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.openAwsSecurityGroupFinding"] = Field(alias="@odata.type", default="#microsoft.graph.openAwsSecurityGroupFinding")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	inboundPorts: Optional[Union[AllInboundPorts, EnumeratedInboundPorts]] = Field(alias="inboundPorts", default=None,discriminator="odata_type", )
	totalStorageBucketCount: Optional[int] = Field(alias="totalStorageBucketCount", default=None,)
	assignedComputeInstancesDetails: Optional[list[AssignedComputeInstanceDetails]] = Field(alias="assignedComputeInstancesDetails", default=None,)
	securityGroup: Optional[AwsAuthorizationSystemResource] = Field(alias="securityGroup", default=None,)

from .all_inbound_ports import AllInboundPorts
from .enumerated_inbound_ports import EnumeratedInboundPorts
from .assigned_compute_instance_details import AssignedComputeInstanceDetails
from .aws_authorization_system_resource import AwsAuthorizationSystemResource
