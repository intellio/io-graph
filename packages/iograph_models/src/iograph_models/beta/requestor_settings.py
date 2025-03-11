from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RequestorSettings(BaseModel):
	acceptRequests: Optional[bool] = Field(alias="acceptRequests",default=None,)
	allowedRequestors: SerializeAsAny[Optional[list[UserSet]]] = Field(alias="allowedRequestors",default=None,)
	scopeType: Optional[str] = Field(alias="scopeType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .user_set import UserSet

