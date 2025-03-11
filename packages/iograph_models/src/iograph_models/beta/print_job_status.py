from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PrintJobStatus(BaseModel):
	acquiredByPrinter: Optional[bool] = Field(alias="acquiredByPrinter",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	details: Optional[list[PrintJobStateDetail | str]] = Field(alias="details",default=None,)
	isAcquiredByPrinter: Optional[bool] = Field(alias="isAcquiredByPrinter",default=None,)
	processingState: Optional[PrintJobProcessingState | str] = Field(alias="processingState",default=None,)
	processingStateDescription: Optional[str] = Field(alias="processingStateDescription",default=None,)
	state: Optional[PrintJobProcessingState | str] = Field(alias="state",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .print_job_state_detail import PrintJobStateDetail
from .print_job_processing_state import PrintJobProcessingState
from .print_job_processing_state import PrintJobProcessingState

