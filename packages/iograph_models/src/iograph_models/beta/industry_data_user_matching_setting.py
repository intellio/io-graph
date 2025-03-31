from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IndustryDataUserMatchingSetting(BaseModel):
	matchTarget: Optional[IndustryDataUserMatchTargetReferenceValue] = Field(alias="matchTarget", default=None,)
	priorityOrder: Optional[int] = Field(alias="priorityOrder", default=None,)
	sourceIdentifier: Optional[IndustryDataIdentifierTypeReferenceValue] = Field(alias="sourceIdentifier", default=None,)
	roleGroup: Optional[IndustryDataRoleGroup] = Field(alias="roleGroup", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .industry_data_user_match_target_reference_value import IndustryDataUserMatchTargetReferenceValue
from .industry_data_identifier_type_reference_value import IndustryDataIdentifierTypeReferenceValue
from .industry_data_role_group import IndustryDataRoleGroup
