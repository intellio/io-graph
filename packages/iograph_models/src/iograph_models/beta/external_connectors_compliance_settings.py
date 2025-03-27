from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalConnectorsComplianceSettings(BaseModel):
	eDiscoveryResultTemplates: Optional[list[ExternalConnectorsDisplayTemplate]] = Field(alias="eDiscoveryResultTemplates", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .external_connectors_display_template import ExternalConnectorsDisplayTemplate

