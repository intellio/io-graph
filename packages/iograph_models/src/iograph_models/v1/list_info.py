from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ListInfo(BaseModel):
	contentTypesEnabled: Optional[bool] = Field(alias="contentTypesEnabled",default=None,)
	hidden: Optional[bool] = Field(alias="hidden",default=None,)
	template: Optional[str] = Field(alias="template",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


