from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PrintJob(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	acknowledgedDateTime: Optional[datetime] = Field(alias="acknowledgedDateTime",default=None,)
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime",default=None,)
	configuration: Optional[PrintJobConfiguration] = Field(alias="configuration",default=None,)
	createdBy: SerializeAsAny[Optional[UserIdentity]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	errorCode: Optional[int] = Field(alias="errorCode",default=None,)
	isFetchable: Optional[bool] = Field(alias="isFetchable",default=None,)
	redirectedFrom: Optional[str] = Field(alias="redirectedFrom",default=None,)
	redirectedTo: Optional[str] = Field(alias="redirectedTo",default=None,)
	status: Optional[PrintJobStatus] = Field(alias="status",default=None,)
	documents: Optional[list[PrintDocument]] = Field(alias="documents",default=None,)
	tasks: Optional[list[PrintTask]] = Field(alias="tasks",default=None,)

from .print_job_configuration import PrintJobConfiguration
from .user_identity import UserIdentity
from .print_job_status import PrintJobStatus
from .print_document import PrintDocument
from .print_task import PrintTask

