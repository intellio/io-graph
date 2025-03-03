from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Todo(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	lists: Optional[list[TodoTaskList]] = Field(default=None,alias="lists",)

from .todo_task_list import TodoTaskList

