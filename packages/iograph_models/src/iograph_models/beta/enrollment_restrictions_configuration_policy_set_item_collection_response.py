from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EnrollmentRestrictionsConfigurationPolicySetItemCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[EnrollmentRestrictionsConfigurationPolicySetItem]] = Field(alias="value", default=None,)

from .enrollment_restrictions_configuration_policy_set_item import EnrollmentRestrictionsConfigurationPolicySetItem

