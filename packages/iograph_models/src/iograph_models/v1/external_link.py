from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalLink(BaseModel):
	href: Optional[str] = Field(alias="href", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


