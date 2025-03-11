from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class UserCredentialUsageDetails(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	authMethod: Optional[UsageAuthMethod | str] = Field(alias="authMethod",default=None,)
	eventDateTime: Optional[datetime] = Field(alias="eventDateTime",default=None,)
	failureReason: Optional[str] = Field(alias="failureReason",default=None,)
	feature: Optional[FeatureType | str] = Field(alias="feature",default=None,)
	isSuccess: Optional[bool] = Field(alias="isSuccess",default=None,)
	userDisplayName: Optional[str] = Field(alias="userDisplayName",default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName",default=None,)

from .usage_auth_method import UsageAuthMethod
from .feature_type import FeatureType

