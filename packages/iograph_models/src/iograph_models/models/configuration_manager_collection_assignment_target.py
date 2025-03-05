from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ConfigurationManagerCollectionAssignmentTarget(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	collectionId: Optional[str] = Field(alias="collectionId",default=None,)


