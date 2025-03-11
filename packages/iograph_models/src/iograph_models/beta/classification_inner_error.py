from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ClassificationInnerError(BaseModel):
	activityId: Optional[str] = Field(alias="activityId",default=None,)
	clientRequestId: Optional[str] = Field(alias="clientRequestId",default=None,)
	code: Optional[str] = Field(alias="code",default=None,)
	errorDateTime: Optional[datetime] = Field(alias="errorDateTime",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


