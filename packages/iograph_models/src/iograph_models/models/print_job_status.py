from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PrintJobStatus(BaseModel):
	description: Optional[str] = Field(alias="description",default=None,)
	details: Optional[list[str | PrintJobStateDetail]] = Field(alias="details",default=None,)
	isAcquiredByPrinter: Optional[bool] = Field(alias="isAcquiredByPrinter",default=None,)
	state: Optional[str | PrintJobProcessingState] = Field(alias="state",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .print_job_state_detail import PrintJobStateDetail
from .print_job_processing_state import PrintJobProcessingState

