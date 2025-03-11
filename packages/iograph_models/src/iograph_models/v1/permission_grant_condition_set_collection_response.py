from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PermissionGrantConditionSetCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[PermissionGrantConditionSet]] = Field(alias="value",default=None,)

from .permission_grant_condition_set import PermissionGrantConditionSet

