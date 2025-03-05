from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserRegistrationFeatureSummary(BaseModel):
	totalUserCount: Optional[int] = Field(alias="totalUserCount",default=None,)
	userRegistrationFeatureCounts: Optional[list[UserRegistrationFeatureCount]] = Field(alias="userRegistrationFeatureCounts",default=None,)
	userRoles: Optional[str | IncludedUserRoles] = Field(alias="userRoles",default=None,)
	userTypes: Optional[str | IncludedUserTypes] = Field(alias="userTypes",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .user_registration_feature_count import UserRegistrationFeatureCount
from .included_user_roles import IncludedUserRoles
from .included_user_types import IncludedUserTypes

