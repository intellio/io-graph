from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class FeatureRolloutPolicy(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	feature: Optional[StagedFeatureName] = Field(default=None,alias="feature",)
	isAppliedToOrganization: Optional[bool] = Field(default=None,alias="isAppliedToOrganization",)
	isEnabled: Optional[bool] = Field(default=None,alias="isEnabled",)
	appliesTo: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(default=None,alias="appliesTo",)

from .staged_feature_name import StagedFeatureName
from .directory_object import DirectoryObject

