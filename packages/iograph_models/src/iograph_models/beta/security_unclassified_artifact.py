from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityUnclassifiedArtifact(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.unclassifiedArtifact"] = Field(alias="@odata.type", default="#microsoft.graph.security.unclassifiedArtifact")
	kind: Optional[str] = Field(alias="kind", default=None,)
	value: Optional[str] = Field(alias="value", default=None,)


