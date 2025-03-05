from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementReports(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	exportJobs: Optional[list[DeviceManagementExportJob]] = Field(default=None,alias="exportJobs",)

from .device_management_export_job import DeviceManagementExportJob

