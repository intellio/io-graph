from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EducationSubmission(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	excusedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="excusedBy",default=None,)
	excusedDateTime: Optional[datetime] = Field(alias="excusedDateTime",default=None,)
	reassignedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="reassignedBy",default=None,)
	reassignedDateTime: Optional[datetime] = Field(alias="reassignedDateTime",default=None,)
	recipient: SerializeAsAny[Optional[EducationSubmissionRecipient]] = Field(alias="recipient",default=None,)
	resourcesFolderUrl: Optional[str] = Field(alias="resourcesFolderUrl",default=None,)
	returnedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="returnedBy",default=None,)
	returnedDateTime: Optional[datetime] = Field(alias="returnedDateTime",default=None,)
	status: Optional[str | EducationSubmissionStatus] = Field(alias="status",default=None,)
	submittedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="submittedBy",default=None,)
	submittedDateTime: Optional[datetime] = Field(alias="submittedDateTime",default=None,)
	unsubmittedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="unsubmittedBy",default=None,)
	unsubmittedDateTime: Optional[datetime] = Field(alias="unsubmittedDateTime",default=None,)
	webUrl: Optional[str] = Field(alias="webUrl",default=None,)
	outcomes: SerializeAsAny[Optional[list[EducationOutcome]]] = Field(alias="outcomes",default=None,)
	resources: Optional[list[EducationSubmissionResource]] = Field(alias="resources",default=None,)
	submittedResources: Optional[list[EducationSubmissionResource]] = Field(alias="submittedResources",default=None,)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .education_submission_recipient import EducationSubmissionRecipient
from .identity_set import IdentitySet
from .education_submission_status import EducationSubmissionStatus
from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .education_outcome import EducationOutcome
from .education_submission_resource import EducationSubmissionResource
from .education_submission_resource import EducationSubmissionResource

