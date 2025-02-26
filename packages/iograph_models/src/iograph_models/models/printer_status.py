from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PrinterStatus(BaseModel):
	description: Optional[str] = Field(default=None,alias="description",)
	details: list[PrinterProcessingStateDetail] = Field(alias="details",)
	state: Optional[PrinterProcessingState] = Field(default=None,alias="state",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .printer_processing_state_detail import PrinterProcessingStateDetail
from .printer_processing_state import PrinterProcessingState

