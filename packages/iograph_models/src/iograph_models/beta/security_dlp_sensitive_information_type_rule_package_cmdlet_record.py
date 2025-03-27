from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityDlpSensitiveInformationTypeRulePackageCmdletRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.dlpSensitiveInformationTypeRulePackageCmdletRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.dlpSensitiveInformationTypeRulePackageCmdletRecord")


