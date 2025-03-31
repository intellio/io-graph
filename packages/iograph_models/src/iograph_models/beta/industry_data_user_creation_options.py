from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IndustryDataUserCreationOptions(BaseModel):
	configurations: Optional[list[IndustryDataUserConfiguration]] = Field(alias="configurations", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .industry_data_user_configuration import IndustryDataUserConfiguration
