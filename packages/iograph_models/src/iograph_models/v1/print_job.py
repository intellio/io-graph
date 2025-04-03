from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class PrintJob(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.printJob"] = Field(alias="@odata.type", default="#microsoft.graph.printJob")
	configuration: Optional[PrintJobConfiguration] = Field(alias="configuration", default=None,)
	createdBy: Optional[UserIdentity] = Field(alias="createdBy", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	isFetchable: Optional[bool] = Field(alias="isFetchable", default=None,)
	redirectedFrom: Optional[str] = Field(alias="redirectedFrom", default=None,)
	redirectedTo: Optional[str] = Field(alias="redirectedTo", default=None,)
	status: Optional[PrintJobStatus] = Field(alias="status", default=None,)
	documents: Optional[list[PrintDocument]] = Field(alias="documents", default=None,)
	tasks: Optional[list[PrintTask]] = Field(alias="tasks", default=None,)

from .print_job_configuration import PrintJobConfiguration
from .user_identity import UserIdentity
from .print_job_status import PrintJobStatus
from .print_document import PrintDocument
from .print_task import PrintTask
