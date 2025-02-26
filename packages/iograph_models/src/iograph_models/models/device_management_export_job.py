from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceManagementExportJob(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	expirationDateTime: Optional[datetime] = Field(default=None,alias="expirationDateTime",)
	filter: Optional[str] = Field(default=None,alias="filter",)
	format: Optional[DeviceManagementReportFileFormat] = Field(default=None,alias="format",)
	localizationType: Optional[DeviceManagementExportJobLocalizationType] = Field(default=None,alias="localizationType",)
	reportName: Optional[str] = Field(default=None,alias="reportName",)
	requestDateTime: Optional[datetime] = Field(default=None,alias="requestDateTime",)
	select: list[Optional[str]] = Field(alias="select",)
	snapshotId: Optional[str] = Field(default=None,alias="snapshotId",)
	status: Optional[DeviceManagementReportStatus] = Field(default=None,alias="status",)
	url: Optional[str] = Field(default=None,alias="url",)

from .device_management_report_file_format import DeviceManagementReportFileFormat
from .device_management_export_job_localization_type import DeviceManagementExportJobLocalizationType
from .device_management_report_status import DeviceManagementReportStatus

