from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CredentialUsageSummary(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	authMethod: Optional[UsageAuthMethod | str] = Field(alias="authMethod",default=None,)
	failureActivityCount: Optional[int] = Field(alias="failureActivityCount",default=None,)
	feature: Optional[FeatureType | str] = Field(alias="feature",default=None,)
	successfulActivityCount: Optional[int] = Field(alias="successfulActivityCount",default=None,)

from .usage_auth_method import UsageAuthMethod
from .feature_type import FeatureType

