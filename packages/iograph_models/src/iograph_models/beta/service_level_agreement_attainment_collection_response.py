from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ServiceLevelAgreementAttainmentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[ServiceLevelAgreementAttainment]] = Field(alias="value",default=None,)

from .service_level_agreement_attainment import ServiceLevelAgreementAttainment

