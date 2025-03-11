from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataSourceSystemDefinition(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	userMatchingSettings: Optional[list[IndustryDataUserMatchingSetting]] = Field(alias="userMatchingSettings",default=None,)
	vendor: Optional[str] = Field(alias="vendor",default=None,)

from .industry_data_user_matching_setting import IndustryDataUserMatchingSetting

