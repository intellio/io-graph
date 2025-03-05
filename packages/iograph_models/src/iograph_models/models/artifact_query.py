from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ArtifactQuery(BaseModel):
	artifactType: Optional[RestorableArtifact] = Field(default=None,alias="artifactType",)
	queryExpression: Optional[str] = Field(default=None,alias="queryExpression",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .restorable_artifact import RestorableArtifact

