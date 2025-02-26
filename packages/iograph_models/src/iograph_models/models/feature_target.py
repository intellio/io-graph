from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class FeatureTarget(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	targetType: Optional[FeatureTargetType] = Field(default=None,alias="targetType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .feature_target_type import FeatureTargetType

