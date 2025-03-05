from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EducationFeedback(BaseModel):
	feedbackBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="feedbackBy",default=None,)
	feedbackDateTime: Optional[datetime] = Field(alias="feedbackDateTime",default=None,)
	text: Optional[EducationItemBody] = Field(alias="text",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .identity_set import IdentitySet
from .education_item_body import EducationItemBody

