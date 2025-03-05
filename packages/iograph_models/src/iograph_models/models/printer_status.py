from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PrinterStatus(BaseModel):
	description: Optional[str] = Field(alias="description",default=None,)
	details: Optional[list[str | PrinterProcessingStateDetail]] = Field(alias="details",default=None,)
	state: Optional[str | PrinterProcessingState] = Field(alias="state",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .printer_processing_state_detail import PrinterProcessingStateDetail
from .printer_processing_state import PrinterProcessingState

