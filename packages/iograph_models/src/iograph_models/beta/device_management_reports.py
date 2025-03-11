from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementReports(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	cachedReportConfigurations: Optional[list[DeviceManagementCachedReportConfiguration]] = Field(alias="cachedReportConfigurations",default=None,)
	exportJobs: Optional[list[DeviceManagementExportJob]] = Field(alias="exportJobs",default=None,)

from .device_management_cached_report_configuration import DeviceManagementCachedReportConfiguration
from .device_management_export_job import DeviceManagementExportJob

