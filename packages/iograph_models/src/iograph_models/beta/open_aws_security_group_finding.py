from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class OpenAwsSecurityGroupFinding(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	inboundPorts: SerializeAsAny[Optional[InboundPorts]] = Field(alias="inboundPorts",default=None,)
	totalStorageBucketCount: Optional[int] = Field(alias="totalStorageBucketCount",default=None,)
	assignedComputeInstancesDetails: Optional[list[AssignedComputeInstanceDetails]] = Field(alias="assignedComputeInstancesDetails",default=None,)
	securityGroup: Optional[AwsAuthorizationSystemResource] = Field(alias="securityGroup",default=None,)

from .inbound_ports import InboundPorts
from .assigned_compute_instance_details import AssignedComputeInstanceDetails
from .aws_authorization_system_resource import AwsAuthorizationSystemResource

