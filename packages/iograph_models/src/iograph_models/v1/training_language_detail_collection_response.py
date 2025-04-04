from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TrainingLanguageDetailCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[TrainingLanguageDetail]] = Field(alias="value", default=None,)

from .training_language_detail import TrainingLanguageDetail
