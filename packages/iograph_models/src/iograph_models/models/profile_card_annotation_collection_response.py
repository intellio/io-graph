from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ProfileCardAnnotationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[ProfileCardAnnotation] = Field(alias="value",)

from .profile_card_annotation import ProfileCardAnnotation

