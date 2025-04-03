from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class PartnerSecurityAdditionalDataDictionary(BaseModel):
	odata_type: Literal["#microsoft.graph.partner.security.additionalDataDictionary"] = Field(alias="@odata.type", default="#microsoft.graph.partner.security.additionalDataDictionary")

