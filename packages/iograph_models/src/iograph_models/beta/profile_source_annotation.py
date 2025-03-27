from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ProfileSourceAnnotation(BaseModel):
	isDefaultSource: Optional[bool] = Field(alias="isDefaultSource", default=None,)
	properties: Optional[list[str]] = Field(alias="properties", default=None,)
	sourceId: Optional[str] = Field(alias="sourceId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


