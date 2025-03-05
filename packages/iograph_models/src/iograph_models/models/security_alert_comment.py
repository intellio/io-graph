from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityAlertComment(BaseModel):
	comment: Optional[str] = Field(alias="comment",default=None,)
	createdByDisplayName: Optional[str] = Field(alias="createdByDisplayName",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


