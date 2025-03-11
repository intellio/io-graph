from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ExchangeRestoreSession(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	error: Optional[PublicError] = Field(alias="error",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	restoreJobType: Optional[RestoreJobType | str] = Field(alias="restoreJobType",default=None,)
	restoreSessionArtifactCount: Optional[RestoreSessionArtifactCount] = Field(alias="restoreSessionArtifactCount",default=None,)
	status: Optional[RestoreSessionStatus | str] = Field(alias="status",default=None,)
	granularMailboxRestoreArtifacts: Optional[list[GranularMailboxRestoreArtifact]] = Field(alias="granularMailboxRestoreArtifacts",default=None,)
	mailboxRestoreArtifacts: SerializeAsAny[Optional[list[MailboxRestoreArtifact]]] = Field(alias="mailboxRestoreArtifacts",default=None,)
	mailboxRestoreArtifactsBulkAdditionRequests: Optional[list[MailboxRestoreArtifactsBulkAdditionRequest]] = Field(alias="mailboxRestoreArtifactsBulkAdditionRequests",default=None,)

from .identity_set import IdentitySet
from .public_error import PublicError
from .identity_set import IdentitySet
from .restore_job_type import RestoreJobType
from .restore_session_artifact_count import RestoreSessionArtifactCount
from .restore_session_status import RestoreSessionStatus
from .granular_mailbox_restore_artifact import GranularMailboxRestoreArtifact
from .mailbox_restore_artifact import MailboxRestoreArtifact
from .mailbox_restore_artifacts_bulk_addition_request import MailboxRestoreArtifactsBulkAdditionRequest

