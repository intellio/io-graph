from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SourcedAttribute(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	id: Optional[str] = Field(alias="id",default=None,)
	isExtensionAttribute: Optional[bool] = Field(alias="isExtensionAttribute",default=None,)
	source: Optional[str] = Field(alias="source",default=None,)


