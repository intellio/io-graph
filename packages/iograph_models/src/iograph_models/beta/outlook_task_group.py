from __future__ import annotations
from uuid import UUID
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class OutlookTaskGroup(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.outlookTaskGroup"] = Field(alias="@odata.type",)
	changeKey: Optional[str] = Field(alias="changeKey", default=None,)
	groupKey: Optional[UUID] = Field(alias="groupKey", default=None,)
	isDefaultGroup: Optional[bool] = Field(alias="isDefaultGroup", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	taskFolders: Optional[list[OutlookTaskFolder]] = Field(alias="taskFolders", default=None,)

from .outlook_task_folder import OutlookTaskFolder
