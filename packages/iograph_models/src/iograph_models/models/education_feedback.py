from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class EducationFeedback(BaseModel):
	feedbackBy: Optional[IdentitySet] = Field(default=None,alias="feedbackBy",)
	feedbackDateTime: Optional[datetime] = Field(default=None,alias="feedbackDateTime",)
	text: Optional[EducationItemBody] = Field(default=None,alias="text",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .identity_set import IdentitySet
from .education_item_body import EducationItemBody

