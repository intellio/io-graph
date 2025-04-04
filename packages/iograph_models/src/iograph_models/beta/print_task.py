from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PrintTask(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.printTask"] = Field(alias="@odata.type", default="#microsoft.graph.printTask")
	parentUrl: Optional[str] = Field(alias="parentUrl", default=None,)
	status: Optional[PrintTaskStatus] = Field(alias="status", default=None,)
	definition: Optional[PrintTaskDefinition] = Field(alias="definition", default=None,)
	trigger: Optional[PrintTaskTrigger] = Field(alias="trigger", default=None,)

from .print_task_status import PrintTaskStatus
from .print_task_definition import PrintTaskDefinition
from .print_task_trigger import PrintTaskTrigger
