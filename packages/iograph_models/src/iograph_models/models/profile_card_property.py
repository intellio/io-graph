from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ProfileCardProperty(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	annotations: list[ProfileCardAnnotation] = Field(alias="annotations",)
	directoryPropertyName: Optional[str] = Field(default=None,alias="directoryPropertyName",)

from .profile_card_annotation import ProfileCardAnnotation

