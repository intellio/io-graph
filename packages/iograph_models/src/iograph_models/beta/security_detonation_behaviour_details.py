from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityDetonationBehaviourDetails(BaseModel):
	actionStatus: Optional[str] = Field(alias="actionStatus",default=None,)
	behaviourCapability: Optional[str] = Field(alias="behaviourCapability",default=None,)
	behaviourGroup: Optional[str] = Field(alias="behaviourGroup",default=None,)
	details: Optional[str] = Field(alias="details",default=None,)
	eventDateTime: Optional[datetime] = Field(alias="eventDateTime",default=None,)
	operation: Optional[str] = Field(alias="operation",default=None,)
	processId: Optional[str] = Field(alias="processId",default=None,)
	processName: Optional[str] = Field(alias="processName",default=None,)
	target: Optional[str] = Field(alias="target",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


