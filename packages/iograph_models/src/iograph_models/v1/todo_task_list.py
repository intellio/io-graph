from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class TodoTaskList(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.todoTaskList"] = Field(alias="@odata.type", default="#microsoft.graph.todoTaskList")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isOwner: Optional[bool] = Field(alias="isOwner", default=None,)
	isShared: Optional[bool] = Field(alias="isShared", default=None,)
	wellknownListName: Optional[WellknownListName | str] = Field(alias="wellknownListName", default=None,)
	extensions: Optional[list[Annotated[Union[OpenTypeExtension],Field(discriminator="odata_type")]]] = Field(alias="extensions", default=None,)
	tasks: Optional[list[TodoTask]] = Field(alias="tasks", default=None,)

from .wellknown_list_name import WellknownListName
from .open_type_extension import OpenTypeExtension
from .todo_task import TodoTask
