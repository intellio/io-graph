from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PrintTask(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	parentUrl: Optional[str] = Field(default=None,alias="parentUrl",)
	status: Optional[PrintTaskStatus] = Field(default=None,alias="status",)
	definition: Optional[PrintTaskDefinition] = Field(default=None,alias="definition",)
	trigger: Optional[PrintTaskTrigger] = Field(default=None,alias="trigger",)

from .print_task_status import PrintTaskStatus
from .print_task_definition import PrintTaskDefinition
from .print_task_trigger import PrintTaskTrigger

