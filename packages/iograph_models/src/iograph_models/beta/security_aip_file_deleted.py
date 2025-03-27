from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityAipFileDeleted(BaseModel):
	odata_type: Literal["#microsoft.graph.security.aipFileDeleted"] = Field(alias="@odata.type", default="#microsoft.graph.security.aipFileDeleted")


