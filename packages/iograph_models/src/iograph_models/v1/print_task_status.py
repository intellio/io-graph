from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PrintTaskStatus(BaseModel):
	description: Optional[str] = Field(alias="description", default=None,)
	state: Optional[PrintTaskProcessingState | str] = Field(alias="state", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .print_task_processing_state import PrintTaskProcessingState
