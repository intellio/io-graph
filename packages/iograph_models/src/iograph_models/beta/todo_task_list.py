from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class TodoTaskList(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isOwner: Optional[bool] = Field(alias="isOwner", default=None,)
	isShared: Optional[bool] = Field(alias="isShared", default=None,)
	wellknownListName: Optional[WellknownListName | str] = Field(alias="wellknownListName", default=None,)
	extensions: Optional[list[Annotated[Union[OpenTypeExtension, PersonExtension],Field(discriminator="odata_type")]]] = Field(alias="extensions", default=None,)
	tasks: Optional[list[TodoTask]] = Field(alias="tasks", default=None,)

from .wellknown_list_name import WellknownListName
from .open_type_extension import OpenTypeExtension
from .person_extension import PersonExtension
from .todo_task import TodoTask

