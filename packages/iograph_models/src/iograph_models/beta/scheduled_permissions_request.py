from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ScheduledPermissionsRequest(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.scheduledPermissionsRequest"] = Field(alias="@odata.type",)
	action: Optional[UnifiedRoleScheduleRequestActions | str] = Field(alias="action", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	justification: Optional[str] = Field(alias="justification", default=None,)
	notes: Optional[str] = Field(alias="notes", default=None,)
	requestedPermissions: Optional[Union[AwsPermissionsDefinition, SingleResourceAzurePermissionsDefinition, SingleResourceGcpPermissionsDefinition]] = Field(alias="requestedPermissions", default=None,discriminator="odata_type", )
	scheduleInfo: Optional[RequestSchedule] = Field(alias="scheduleInfo", default=None,)
	statusDetail: Optional[StatusDetail | str] = Field(alias="statusDetail", default=None,)
	ticketInfo: Optional[TicketInfo] = Field(alias="ticketInfo", default=None,)

from .unified_role_schedule_request_actions import UnifiedRoleScheduleRequestActions
from .aws_permissions_definition import AwsPermissionsDefinition
from .single_resource_azure_permissions_definition import SingleResourceAzurePermissionsDefinition
from .single_resource_gcp_permissions_definition import SingleResourceGcpPermissionsDefinition
from .request_schedule import RequestSchedule
from .status_detail import StatusDetail
from .ticket_info import TicketInfo
