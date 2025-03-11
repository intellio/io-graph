from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class FeatureRolloutPolicy(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	feature: Optional[StagedFeatureName | str] = Field(alias="feature",default=None,)
	isAppliedToOrganization: Optional[bool] = Field(alias="isAppliedToOrganization",default=None,)
	isEnabled: Optional[bool] = Field(alias="isEnabled",default=None,)
	appliesTo: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="appliesTo",default=None,)

from .staged_feature_name import StagedFeatureName
from .directory_object import DirectoryObject

