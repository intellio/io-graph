from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class Todo(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.todo"] = Field(alias="@odata.type",)
	lists: Optional[list[TodoTaskList]] = Field(alias="lists", default=None,)

from .todo_task_list import TodoTaskList
