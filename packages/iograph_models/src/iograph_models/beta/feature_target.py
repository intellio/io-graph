from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class FeatureTarget(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	targetType: Optional[FeatureTargetType | str] = Field(alias="targetType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .feature_target_type import FeatureTargetType
