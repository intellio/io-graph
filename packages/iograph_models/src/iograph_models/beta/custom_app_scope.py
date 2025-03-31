from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CustomAppScope(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.customAppScope"] = Field(alias="@odata.type", default="#microsoft.graph.customAppScope")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	type: Optional[str] = Field(alias="type", default=None,)
	customAttributes: Optional[CustomAppScopeAttributesDictionary] = Field(alias="customAttributes", default=None,)

from .custom_app_scope_attributes_dictionary import CustomAppScopeAttributesDictionary
