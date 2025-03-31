from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AdminTodo(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.adminTodo"] = Field(alias="@odata.type",)
	settings: Optional[TodoSettings] = Field(alias="settings", default=None,)

from .todo_settings import TodoSettings
