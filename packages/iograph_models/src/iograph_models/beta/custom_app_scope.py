from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CustomAppScope(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	type: Optional[str] = Field(alias="type",default=None,)
	customAttributes: Optional[CustomAppScopeAttributesDictionary] = Field(alias="customAttributes",default=None,)

from .custom_app_scope_attributes_dictionary import CustomAppScopeAttributesDictionary

