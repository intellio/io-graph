from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PrintTaskDefinitionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[PrintTaskDefinition] = Field(alias="value",)

from .print_task_definition import PrintTaskDefinition

