from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserRegistrationFeatureCount(BaseModel):
	feature: Optional[str | AuthenticationMethodFeature] = Field(alias="feature",default=None,)
	userCount: Optional[int] = Field(alias="userCount",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .authentication_method_feature import AuthenticationMethodFeature

