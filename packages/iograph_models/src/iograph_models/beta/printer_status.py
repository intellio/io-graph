from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PrinterStatus(BaseModel):
	description: Optional[str] = Field(alias="description",default=None,)
	details: Optional[list[PrinterProcessingStateDetail | str]] = Field(alias="details",default=None,)
	processingState: Optional[PrinterProcessingState | str] = Field(alias="processingState",default=None,)
	processingStateDescription: Optional[str] = Field(alias="processingStateDescription",default=None,)
	processingStateReasons: Optional[list[PrinterProcessingStateReason | str]] = Field(alias="processingStateReasons",default=None,)
	state: Optional[PrinterProcessingState | str] = Field(alias="state",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .printer_processing_state_detail import PrinterProcessingStateDetail
from .printer_processing_state import PrinterProcessingState
from .printer_processing_state_reason import PrinterProcessingStateReason
from .printer_processing_state import PrinterProcessingState

