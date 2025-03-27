from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ArtifactQuery(BaseModel):
	artifactType: Optional[RestorableArtifact | str] = Field(alias="artifactType", default=None,)
	queryExpression: Optional[str] = Field(alias="queryExpression", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .restorable_artifact import RestorableArtifact

