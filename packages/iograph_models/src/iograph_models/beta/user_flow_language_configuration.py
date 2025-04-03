from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UserFlowLanguageConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userFlowLanguageConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.userFlowLanguageConfiguration")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isEnabled: Optional[bool] = Field(alias="isEnabled", default=None,)
	defaultPages: Optional[list[UserFlowLanguagePage]] = Field(alias="defaultPages", default=None,)
	overridesPages: Optional[list[UserFlowLanguagePage]] = Field(alias="overridesPages", default=None,)

from .user_flow_language_page import UserFlowLanguagePage
