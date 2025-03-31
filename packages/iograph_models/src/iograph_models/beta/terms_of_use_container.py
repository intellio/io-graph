from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class TermsOfUseContainer(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.termsOfUseContainer"] = Field(alias="@odata.type",)
	agreementAcceptances: Optional[list[AgreementAcceptance]] = Field(alias="agreementAcceptances", default=None,)
	agreements: Optional[list[Agreement]] = Field(alias="agreements", default=None,)

from .agreement_acceptance import AgreementAcceptance
from .agreement import Agreement
