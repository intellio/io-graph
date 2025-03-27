from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AzureADAuthentication(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	attainments: Optional[list[ServiceLevelAgreementAttainment]] = Field(alias="attainments", default=None,)

from .service_level_agreement_attainment import ServiceLevelAgreementAttainment

