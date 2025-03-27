from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcBulkTroubleshoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.cloudPcBulkTroubleshoot"] = Field(alias="@odata.type", default="#microsoft.graph.cloudPcBulkTroubleshoot")
	actionSummary: Optional[CloudPcBulkActionSummary] = Field(alias="actionSummary", default=None,)
	cloudPcIds: Optional[list[str]] = Field(alias="cloudPcIds", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	initiatedByUserPrincipalName: Optional[str] = Field(alias="initiatedByUserPrincipalName", default=None,)
	scheduledDuringMaintenanceWindow: Optional[bool] = Field(alias="scheduledDuringMaintenanceWindow", default=None,)
	status: Optional[CloudPcBulkActionStatus | str] = Field(alias="status", default=None,)

from .cloud_pc_bulk_action_summary import CloudPcBulkActionSummary
from .cloud_pc_bulk_action_status import CloudPcBulkActionStatus

