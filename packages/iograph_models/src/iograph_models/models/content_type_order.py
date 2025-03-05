from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ContentTypeOrder(BaseModel):
	default: Optional[bool] = Field(alias="default",default=None,)
	position: Optional[int] = Field(alias="position",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


