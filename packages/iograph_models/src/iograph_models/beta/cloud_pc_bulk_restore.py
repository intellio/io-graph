from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class CloudPcBulkRestore(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.cloudPcBulkRestore"] = Field(alias="@odata.type", default="#microsoft.graph.cloudPcBulkRestore")
	actionSummary: Optional[CloudPcBulkActionSummary] = Field(alias="actionSummary", default=None,)
	cloudPcIds: Optional[list[str]] = Field(alias="cloudPcIds", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	initiatedByUserPrincipalName: Optional[str] = Field(alias="initiatedByUserPrincipalName", default=None,)
	scheduledDuringMaintenanceWindow: Optional[bool] = Field(alias="scheduledDuringMaintenanceWindow", default=None,)
	status: Optional[CloudPcBulkActionStatus | str] = Field(alias="status", default=None,)
	restorePointDateTime: Optional[datetime] = Field(alias="restorePointDateTime", default=None,)
	timeRange: Optional[RestoreTimeRange | str] = Field(alias="timeRange", default=None,)

from .cloud_pc_bulk_action_summary import CloudPcBulkActionSummary
from .cloud_pc_bulk_action_status import CloudPcBulkActionStatus
from .restore_time_range import RestoreTimeRange
