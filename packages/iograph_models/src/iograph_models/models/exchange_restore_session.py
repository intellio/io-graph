from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class ExchangeRestoreSession(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	completedDateTime: Optional[datetime] = Field(default=None,alias="completedDateTime",)
	createdBy: Optional[IdentitySet] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	error: Optional[PublicError] = Field(default=None,alias="error",)
	lastModifiedBy: Optional[IdentitySet] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	status: Optional[RestoreSessionStatus] = Field(default=None,alias="status",)
	granularMailboxRestoreArtifacts: Optional[list[GranularMailboxRestoreArtifact]] = Field(default=None,alias="granularMailboxRestoreArtifacts",)
	mailboxRestoreArtifacts: Optional[list[MailboxRestoreArtifact]] = Field(default=None,alias="mailboxRestoreArtifacts",)

from .identity_set import IdentitySet
from .public_error import PublicError
from .identity_set import IdentitySet
from .restore_session_status import RestoreSessionStatus
from .granular_mailbox_restore_artifact import GranularMailboxRestoreArtifact
from .mailbox_restore_artifact import MailboxRestoreArtifact

