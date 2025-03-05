from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalLink(BaseModel):
	href: Optional[str] = Field(default=None,alias="href",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


