from __future__ import annotations
from typing import Optional
from typing import Union
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AccessReviewDecision(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
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
from .audit_user_identity import AuditUserIdentity

