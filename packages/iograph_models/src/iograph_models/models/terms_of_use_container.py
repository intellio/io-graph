from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TermsOfUseContainer(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	agreementAcceptances: list[AgreementAcceptance] = Field(alias="agreementAcceptances",)
	agreements: list[Agreement] = Field(alias="agreements",)

from .agreement_acceptance import AgreementAcceptance
from .agreement import Agreement

