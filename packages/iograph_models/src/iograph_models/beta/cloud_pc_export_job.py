from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcExportJob(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime",default=None,)
	exportJobStatus: Optional[CloudPcExportJobStatus | str] = Field(alias="exportJobStatus",default=None,)
	exportUrl: Optional[str] = Field(alias="exportUrl",default=None,)
	filter: Optional[str] = Field(alias="filter",default=None,)
	format: Optional[str] = Field(alias="format",default=None,)
	reportName: Optional[CloudPcReportName | str] = Field(alias="reportName",default=None,)
	requestDateTime: Optional[datetime] = Field(alias="requestDateTime",default=None,)
	select: Optional[list[str]] = Field(alias="select",default=None,)

from .cloud_pc_export_job_status import CloudPcExportJobStatus
from .cloud_pc_report_name import CloudPcReportName

