from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class External_connectors_add_activitiesPostRequest(BaseModel):
	activities: Optional[list[ExternalConnectorsExternalActivity]] = Field(default=None,alias="activities",)

from .external_connectors_external_activity import ExternalConnectorsExternalActivity

