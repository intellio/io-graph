from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserRegistrationFeatureCount(BaseModel):
	feature: Optional[AuthenticationMethodFeature] = Field(default=None,alias="feature",)
	userCount: Optional[int] = Field(default=None,alias="userCount",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .authentication_method_feature import AuthenticationMethodFeature

