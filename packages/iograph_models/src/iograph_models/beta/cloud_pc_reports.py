from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CloudPcReports(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.cloudPcReports"] = Field(alias="@odata.type",)
	exportJobs: Optional[list[CloudPcExportJob]] = Field(alias="exportJobs", default=None,)

from .cloud_pc_export_job import CloudPcExportJob
