from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ConfigurationManagerCollectionAssignmentTarget(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	collectionId: Optional[str] = Field(default=None,alias="collectionId",)


