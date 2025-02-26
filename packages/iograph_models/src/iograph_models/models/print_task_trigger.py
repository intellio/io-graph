from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PrintTaskTrigger(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	event: Optional[PrintEvent] = Field(default=None,alias="event",)
	definition: Optional[PrintTaskDefinition] = Field(default=None,alias="definition",)

from .print_event import PrintEvent
from .print_task_definition import PrintTaskDefinition

