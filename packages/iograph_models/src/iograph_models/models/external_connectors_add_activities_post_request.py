from __future__ import annotations
from pydantic import BaseModel, Field


class External_connectors_add_activitiesPostRequest(BaseModel):
	activities: list[ExternalConnectorsExternalActivity] = Field(alias="activities",)

from .external_connectors_external_activity import ExternalConnectorsExternalActivity

