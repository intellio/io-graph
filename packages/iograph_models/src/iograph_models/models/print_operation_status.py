from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PrintOperationStatus(BaseModel):
	description: Optional[str] = Field(default=None,alias="description",)
	state: Optional[PrintOperationProcessingState] = Field(default=None,alias="state",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .print_operation_processing_state import PrintOperationProcessingState

