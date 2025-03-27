from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Create_migration_reportPostRequest(BaseModel):
	groupPolicyObjectFile: Optional[GroupPolicyObjectFile] = Field(alias="groupPolicyObjectFile", default=None,)

from .group_policy_object_file import GroupPolicyObjectFile

