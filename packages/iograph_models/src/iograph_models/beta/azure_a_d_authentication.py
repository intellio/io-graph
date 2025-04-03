from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AzureADAuthentication(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.azureADAuthentication"] = Field(alias="@odata.type", default="#microsoft.graph.azureADAuthentication")
	attainments: Optional[list[ServiceLevelAgreementAttainment]] = Field(alias="attainments", default=None,)

from .service_level_agreement_attainment import ServiceLevelAgreementAttainment
