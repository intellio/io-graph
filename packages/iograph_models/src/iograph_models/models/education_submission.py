from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EducationSubmission(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	excusedBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="excusedBy",)
	excusedDateTime: Optional[datetime] = Field(default=None,alias="excusedDateTime",)
	reassignedBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="reassignedBy",)
	reassignedDateTime: Optional[datetime] = Field(default=None,alias="reassignedDateTime",)
	recipient: SerializeAsAny[Optional[EducationSubmissionRecipient]] = Field(default=None,alias="recipient",)
	resourcesFolderUrl: Optional[str] = Field(default=None,alias="resourcesFolderUrl",)
	returnedBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="returnedBy",)
	returnedDateTime: Optional[datetime] = Field(default=None,alias="returnedDateTime",)
	status: Optional[EducationSubmissionStatus] = Field(default=None,alias="status",)
	submittedBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="submittedBy",)
	submittedDateTime: Optional[datetime] = Field(default=None,alias="submittedDateTime",)
	unsubmittedBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="unsubmittedBy",)
	unsubmittedDateTime: Optional[datetime] = Field(default=None,alias="unsubmittedDateTime",)
	webUrl: Optional[str] = Field(default=None,alias="webUrl",)
	outcomes: SerializeAsAny[Optional[list[EducationOutcome]]] = Field(default=None,alias="outcomes",)
	resources: Optional[list[EducationSubmissionResource]] = Field(default=None,alias="resources",)
	submittedResources: Optional[list[EducationSubmissionResource]] = Field(default=None,alias="submittedResources",)

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

