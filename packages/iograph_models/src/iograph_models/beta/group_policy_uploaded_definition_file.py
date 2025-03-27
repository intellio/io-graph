from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class GroupPolicyUploadedDefinitionFile(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.groupPolicyUploadedDefinitionFile"] = Field(alias="@odata.type", default="#microsoft.graph.groupPolicyUploadedDefinitionFile")
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	fileName: Optional[str] = Field(alias="fileName", default=None,)
	languageCodes: Optional[list[str]] = Field(alias="languageCodes", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	policyType: Optional[GroupPolicyType | str] = Field(alias="policyType", default=None,)
	revision: Optional[str] = Field(alias="revision", default=None,)
	targetNamespace: Optional[str] = Field(alias="targetNamespace", default=None,)
	targetPrefix: Optional[str] = Field(alias="targetPrefix", default=None,)
	definitions: Optional[list[GroupPolicyDefinition]] = Field(alias="definitions", default=None,)
	content: Optional[str] = Field(alias="content", default=None,)
	defaultLanguageCode: Optional[str] = Field(alias="defaultLanguageCode", default=None,)
	groupPolicyUploadedLanguageFiles: Optional[list[GroupPolicyUploadedLanguageFile]] = Field(alias="groupPolicyUploadedLanguageFiles", default=None,)
	status: Optional[GroupPolicyUploadedDefinitionFileStatus | str] = Field(alias="status", default=None,)
	uploadDateTime: Optional[datetime] = Field(alias="uploadDateTime", default=None,)
	groupPolicyOperations: Optional[list[GroupPolicyOperation]] = Field(alias="groupPolicyOperations", default=None,)

from .group_policy_type import GroupPolicyType
from .group_policy_definition import GroupPolicyDefinition
from .group_policy_uploaded_language_file import GroupPolicyUploadedLanguageFile
from .group_policy_uploaded_definition_file_status import GroupPolicyUploadedDefinitionFileStatus
from .group_policy_operation import GroupPolicyOperation

