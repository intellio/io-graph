from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SynchronizationTemplate(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	applicationId: Optional[UUID] = Field(default=None,alias="applicationId",)
	default: Optional[bool] = Field(default=None,alias="default",)
	description: Optional[str] = Field(default=None,alias="description",)
	discoverable: Optional[bool] = Field(default=None,alias="discoverable",)
	factoryTag: Optional[str] = Field(default=None,alias="factoryTag",)
	metadata: Optional[list[SynchronizationMetadataEntry]] = Field(default=None,alias="metadata",)
	schema: Optional[SynchronizationSchema] = Field(default=None,alias="schema",)

from .synchronization_metadata_entry import SynchronizationMetadataEntry
from .synchronization_schema import SynchronizationSchema

