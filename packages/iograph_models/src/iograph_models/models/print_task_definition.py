from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PrintTaskDefinition(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdBy: Optional[AppIdentity] = Field(default=None,alias="createdBy",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	tasks: Optional[list[PrintTask]] = Field(default=None,alias="tasks",)

from .app_identity import AppIdentity
from .print_task import PrintTask

