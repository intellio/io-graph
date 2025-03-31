from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ConfigurationManagerCollectionAssignmentTarget(BaseModel):
	odata_type: Literal["#microsoft.graph.configurationManagerCollectionAssignmentTarget"] = Field(alias="@odata.type", default="#microsoft.graph.configurationManagerCollectionAssignmentTarget")
	collectionId: Optional[str] = Field(alias="collectionId", default=None,)

