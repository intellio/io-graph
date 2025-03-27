from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ResourceOperation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	actionName: Optional[str] = Field(alias="actionName", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	enabledForScopeValidation: Optional[bool] = Field(alias="enabledForScopeValidation", default=None,)
	resource: Optional[str] = Field(alias="resource", default=None,)
	resourceName: Optional[str] = Field(alias="resourceName", default=None,)


