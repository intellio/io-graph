from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PrintJobStatus(BaseModel):
	description: Optional[str] = Field(default=None,alias="description",)
	details: list[PrintJobStateDetail] = Field(alias="details",)
	isAcquiredByPrinter: Optional[bool] = Field(default=None,alias="isAcquiredByPrinter",)
	state: Optional[PrintJobProcessingState] = Field(default=None,alias="state",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .print_job_state_detail import PrintJobStateDetail
from .print_job_processing_state import PrintJobProcessingState

