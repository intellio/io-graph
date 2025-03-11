from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcBulkActionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[CloudPcBulkAction]]] = Field(alias="value",default=None,)

from .cloud_pc_bulk_action import CloudPcBulkAction

