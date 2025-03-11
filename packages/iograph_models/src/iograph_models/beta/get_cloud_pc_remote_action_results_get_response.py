from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Get_cloud_pc_remote_action_resultsGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[CloudPcRemoteActionResult]] = Field(alias="value",default=None,)

from .cloud_pc_remote_action_result import CloudPcRemoteActionResult

