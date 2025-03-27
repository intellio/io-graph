from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SpaApplication(BaseModel):
	redirectUris: Optional[list[str]] = Field(alias="redirectUris", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


