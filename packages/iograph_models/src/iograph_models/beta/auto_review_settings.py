from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AutoReviewSettings(BaseModel):
	notReviewedResult: Optional[str] = Field(alias="notReviewedResult", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

