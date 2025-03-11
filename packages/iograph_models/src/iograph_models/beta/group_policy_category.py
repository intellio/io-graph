from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class GroupPolicyCategory(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	ingestionSource: Optional[IngestionSource | str] = Field(alias="ingestionSource",default=None,)
	isRoot: Optional[bool] = Field(alias="isRoot",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	children: Optional[list[GroupPolicyCategory]] = Field(alias="children",default=None,)
	definitionFile: SerializeAsAny[Optional[GroupPolicyDefinitionFile]] = Field(alias="definitionFile",default=None,)
	definitions: Optional[list[GroupPolicyDefinition]] = Field(alias="definitions",default=None,)
	parent: Optional[GroupPolicyCategory] = Field(alias="parent",default=None,)

from .ingestion_source import IngestionSource
from .group_policy_definition_file import GroupPolicyDefinitionFile
from .group_policy_definition import GroupPolicyDefinition

