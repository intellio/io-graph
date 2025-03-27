from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityPurviewInsiderRiskAlertsRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.purviewInsiderRiskAlertsRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.purviewInsiderRiskAlertsRecord")


