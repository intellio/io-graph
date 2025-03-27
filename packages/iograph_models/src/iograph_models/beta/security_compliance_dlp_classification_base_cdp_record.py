from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityComplianceDlpClassificationBaseCdpRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.complianceDlpClassificationBaseCdpRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.complianceDlpClassificationBaseCdpRecord")


