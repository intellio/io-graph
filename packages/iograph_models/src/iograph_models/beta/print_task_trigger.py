from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PrintTaskTrigger(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	event: Optional[PrintEvent | str] = Field(alias="event", default=None,)
	definition: Optional[PrintTaskDefinition] = Field(alias="definition", default=None,)

from .print_event import PrintEvent
from .print_task_definition import PrintTaskDefinition

