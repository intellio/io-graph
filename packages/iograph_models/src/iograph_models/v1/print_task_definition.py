from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PrintTaskDefinition(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.printTaskDefinition"] = Field(alias="@odata.type",)
	createdBy: Optional[AppIdentity] = Field(alias="createdBy", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	tasks: Optional[list[PrintTask]] = Field(alias="tasks", default=None,)

from .app_identity import AppIdentity
from .print_task import PrintTask
