from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityUnclassifiedArtifact(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	kind: Optional[str] = Field(default=None,alias="kind",)
	value: Optional[str] = Field(default=None,alias="value",)


