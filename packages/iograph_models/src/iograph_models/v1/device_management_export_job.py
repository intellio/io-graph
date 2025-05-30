from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceManagementExportJob(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementExportJob"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementExportJob")
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime", default=None,)
	filter: Optional[str] = Field(alias="filter", default=None,)
	format: Optional[DeviceManagementReportFileFormat | str] = Field(alias="format", default=None,)
	localizationType: Optional[DeviceManagementExportJobLocalizationType | str] = Field(alias="localizationType", default=None,)
	reportName: Optional[str] = Field(alias="reportName", default=None,)
	requestDateTime: Optional[datetime] = Field(alias="requestDateTime", default=None,)
	select: Optional[list[str]] = Field(alias="select", default=None,)
	snapshotId: Optional[str] = Field(alias="snapshotId", default=None,)
	status: Optional[DeviceManagementReportStatus | str] = Field(alias="status", default=None,)
	url: Optional[str] = Field(alias="url", default=None,)

from .device_management_report_file_format import DeviceManagementReportFileFormat
from .device_management_export_job_localization_type import DeviceManagementExportJobLocalizationType
from .device_management_report_status import DeviceManagementReportStatus
