from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceManagementCachedReportConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementCachedReportConfiguration"] = Field(alias="@odata.type",)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime", default=None,)
	filter: Optional[str] = Field(alias="filter", default=None,)
	lastRefreshDateTime: Optional[datetime] = Field(alias="lastRefreshDateTime", default=None,)
	metadata: Optional[str] = Field(alias="metadata", default=None,)
	orderBy: Optional[list[str]] = Field(alias="orderBy", default=None,)
	reportName: Optional[str] = Field(alias="reportName", default=None,)
	select: Optional[list[str]] = Field(alias="select", default=None,)
	status: Optional[DeviceManagementReportStatus | str] = Field(alias="status", default=None,)

from .device_management_report_status import DeviceManagementReportStatus
