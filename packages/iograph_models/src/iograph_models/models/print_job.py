from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class PrintJob(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	configuration: Optional[PrintJobConfiguration] = Field(default=None,alias="configuration",)
	createdBy: Optional[UserIdentity] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	isFetchable: Optional[bool] = Field(default=None,alias="isFetchable",)
	redirectedFrom: Optional[str] = Field(default=None,alias="redirectedFrom",)
	redirectedTo: Optional[str] = Field(default=None,alias="redirectedTo",)
	status: Optional[PrintJobStatus] = Field(default=None,alias="status",)
	documents: Optional[list[PrintDocument]] = Field(default=None,alias="documents",)
	tasks: Optional[list[PrintTask]] = Field(default=None,alias="tasks",)

from .print_job_configuration import PrintJobConfiguration
from .user_identity import UserIdentity
from .print_job_status import PrintJobStatus
from .print_document import PrintDocument
from .print_task import PrintTask

