from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class AccessReviewDecision(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.accessReviewDecision"] = Field(alias="@odata.type",)
	accessRecommendation: Optional[str] = Field(alias="accessRecommendation", default=None,)
	accessReviewId: Optional[str] = Field(alias="accessReviewId", default=None,)
	appliedBy: Optional[Union[AuditUserIdentity]] = Field(alias="appliedBy", default=None,discriminator="odata_type", )
	appliedDateTime: Optional[datetime] = Field(alias="appliedDateTime", default=None,)
	applyResult: Optional[str] = Field(alias="applyResult", default=None,)
	justification: Optional[str] = Field(alias="justification", default=None,)
	reviewedBy: Optional[Union[AuditUserIdentity]] = Field(alias="reviewedBy", default=None,discriminator="odata_type", )
	reviewedDateTime: Optional[datetime] = Field(alias="reviewedDateTime", default=None,)
	reviewResult: Optional[str] = Field(alias="reviewResult", default=None,)

from .audit_user_identity import AuditUserIdentity
