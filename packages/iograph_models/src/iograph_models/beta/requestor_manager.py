from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class RequestorManager(BaseModel):
	isBackup: Optional[bool] = Field(alias="isBackup", default=None,)
	odata_type: Literal["#microsoft.graph.requestorManager"] = Field(alias="@odata.type", default="#microsoft.graph.requestorManager")
	managerLevel: Optional[int] = Field(alias="managerLevel", default=None,)


