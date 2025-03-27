from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcReports(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	exportJobs: Optional[list[CloudPcExportJob]] = Field(alias="exportJobs", default=None,)

from .cloud_pc_export_job import CloudPcExportJob

