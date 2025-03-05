from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class FeatureRolloutPolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[FeatureRolloutPolicy]] = Field(default=None,alias="value",)

from .feature_rollout_policy import FeatureRolloutPolicy

