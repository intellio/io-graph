from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class OutlookUser(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.outlookUser"] = Field(alias="@odata.type", default="#microsoft.graph.outlookUser")
	masterCategories: Optional[list[OutlookCategory]] = Field(alias="masterCategories", default=None,)
	taskFolders: Optional[list[OutlookTaskFolder]] = Field(alias="taskFolders", default=None,)
	taskGroups: Optional[list[OutlookTaskGroup]] = Field(alias="taskGroups", default=None,)
	tasks: Optional[list[OutlookTask]] = Field(alias="tasks", default=None,)

from .outlook_category import OutlookCategory
from .outlook_task_folder import OutlookTaskFolder
from .outlook_task_group import OutlookTaskGroup
from .outlook_task import OutlookTask
