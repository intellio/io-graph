from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Notification(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayTimeToLive: Optional[int] = Field(alias="displayTimeToLive",default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime",default=None,)
	groupName: Optional[str] = Field(alias="groupName",default=None,)
	payload: Optional[PayloadTypes] = Field(alias="payload",default=None,)
	priority: Optional[Priority | str] = Field(alias="priority",default=None,)
	targetHostName: Optional[str] = Field(alias="targetHostName",default=None,)
	targetPolicy: Optional[TargetPolicyEndpoints] = Field(alias="targetPolicy",default=None,)

from .payload_types import PayloadTypes
from .priority import Priority
from .target_policy_endpoints import TargetPolicyEndpoints

