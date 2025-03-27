from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataUserManagementOptions(BaseModel):
	additionalAttributes: Optional[list[IndustryDataAdditionalUserAttributes | str]] = Field(alias="additionalAttributes", default=None,)
	additionalOptions: Optional[IndustryDataAdditionalUserOptions] = Field(alias="additionalOptions", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .industry_data_additional_user_attributes import IndustryDataAdditionalUserAttributes
from .industry_data_additional_user_options import IndustryDataAdditionalUserOptions

