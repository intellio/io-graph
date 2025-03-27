from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityComplianceDlpExchangeClassificationCdpRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.complianceDlpExchangeClassificationCdpRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.complianceDlpExchangeClassificationCdpRecord")


