from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PrintTaskDefinition(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdBy: Optional[AppIdentity] = Field(alias="createdBy", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	tasks: Optional[list[PrintTask]] = Field(alias="tasks", default=None,)

from .app_identity import AppIdentity
from .print_task import PrintTask

