from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ActionStep(BaseModel):
	actionUrl: Optional[ActionUrl] = Field(alias="actionUrl",default=None,)
	stepNumber: Optional[int] = Field(alias="stepNumber",default=None,)
	text: Optional[str] = Field(alias="text",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .action_url import ActionUrl

