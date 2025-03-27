from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TermsOfUseContainer(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	agreementAcceptances: Optional[list[AgreementAcceptance]] = Field(alias="agreementAcceptances", default=None,)
	agreements: Optional[list[Agreement]] = Field(alias="agreements", default=None,)

from .agreement_acceptance import AgreementAcceptance
from .agreement import Agreement

