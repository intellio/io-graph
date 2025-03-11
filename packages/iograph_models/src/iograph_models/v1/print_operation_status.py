from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PrintOperationStatus(BaseModel):
	description: Optional[str] = Field(alias="description",default=None,)
	state: Optional[PrintOperationProcessingState | str] = Field(alias="state",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .print_operation_processing_state import PrintOperationProcessingState

