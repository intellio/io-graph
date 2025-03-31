from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserRegistrationFeatureCountCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[UserRegistrationFeatureCount]] = Field(alias="value", default=None,)

from .user_registration_feature_count import UserRegistrationFeatureCount
