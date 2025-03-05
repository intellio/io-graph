from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserRegistrationFeatureSummary(BaseModel):
	totalUserCount: Optional[int] = Field(default=None,alias="totalUserCount",)
	userRegistrationFeatureCounts: Optional[list[UserRegistrationFeatureCount]] = Field(default=None,alias="userRegistrationFeatureCounts",)
	userRoles: Optional[IncludedUserRoles] = Field(default=None,alias="userRoles",)
	userTypes: Optional[IncludedUserTypes] = Field(default=None,alias="userTypes",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .user_registration_feature_count import UserRegistrationFeatureCount
from .included_user_roles import IncludedUserRoles
from .included_user_types import IncludedUserTypes

