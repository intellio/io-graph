from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeviceManagementReports(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementReports"] = Field(alias="@odata.type",)
	exportJobs: Optional[list[DeviceManagementExportJob]] = Field(alias="exportJobs", default=None,)

from .device_management_export_job import DeviceManagementExportJob
