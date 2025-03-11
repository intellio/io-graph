from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Windows10XTrustedRootCertificate(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	creationDateTime: Optional[datetime] = Field(alias="creationDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds",default=None,)
	version: Optional[int] = Field(alias="version",default=None,)
	assignments: Optional[list[DeviceManagementResourceAccessProfileAssignment]] = Field(alias="assignments",default=None,)
	certFileName: Optional[str] = Field(alias="certFileName",default=None,)
	destinationStore: Optional[CertificateDestinationStore | str] = Field(alias="destinationStore",default=None,)
	trustedRootCertificate: Optional[str] = Field(alias="trustedRootCertificate",default=None,)

from .device_management_resource_access_profile_assignment import DeviceManagementResourceAccessProfileAssignment
from .certificate_destination_store import CertificateDestinationStore

