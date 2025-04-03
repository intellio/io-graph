from __future__ import annotations
from uuid import UUID
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SynchronizationTemplate(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.synchronizationTemplate"] = Field(alias="@odata.type", default="#microsoft.graph.synchronizationTemplate")
	applicationId: Optional[UUID] = Field(alias="applicationId", default=None,)
	default: Optional[bool] = Field(alias="default", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	discoverable: Optional[bool] = Field(alias="discoverable", default=None,)
	factoryTag: Optional[str] = Field(alias="factoryTag", default=None,)
	metadata: Optional[list[SynchronizationMetadataEntry]] = Field(alias="metadata", default=None,)
	schema_: Optional[SynchronizationSchema] = Field(alias="schema", default=None,)

from .synchronization_metadata_entry import SynchronizationMetadataEntry
from .synchronization_schema import SynchronizationSchema
