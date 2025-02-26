from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuthenticationCombinationConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[AuthenticationCombinationConfiguration] = Field(alias="value",)

from .authentication_combination_configuration import AuthenticationCombinationConfiguration

