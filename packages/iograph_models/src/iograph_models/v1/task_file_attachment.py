from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class TaskFileAttachment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.taskFileAttachment"] = Field(alias="@odata.type", default="#microsoft.graph.taskFileAttachment")
	contentType: Optional[str] = Field(alias="contentType", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	size: Optional[int] = Field(alias="size", default=None,)
	contentBytes: Optional[str] = Field(alias="contentBytes", default=None,)


