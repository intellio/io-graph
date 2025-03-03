from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TodoTaskList(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	isOwner: Optional[bool] = Field(default=None,alias="isOwner",)
	isShared: Optional[bool] = Field(default=None,alias="isShared",)
	wellknownListName: Optional[WellknownListName] = Field(default=None,alias="wellknownListName",)
	extensions: Optional[list[Extension]] = Field(default=None,alias="extensions",)
	tasks: Optional[list[TodoTask]] = Field(default=None,alias="tasks",)

from .wellknown_list_name import WellknownListName
from .extension import Extension
from .todo_task import TodoTask

