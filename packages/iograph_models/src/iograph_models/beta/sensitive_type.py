from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SensitiveType(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	classificationMethod: Optional[ClassificationMethod | str] = Field(alias="classificationMethod", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	publisherName: Optional[str] = Field(alias="publisherName", default=None,)
	rulePackageId: Optional[str] = Field(alias="rulePackageId", default=None,)
	rulePackageType: Optional[str] = Field(alias="rulePackageType", default=None,)
	scope: Optional[SensitiveTypeScope | str] = Field(alias="scope", default=None,)
	sensitiveTypeSource: Optional[SensitiveTypeSource | str] = Field(alias="sensitiveTypeSource", default=None,)
	state: Optional[str] = Field(alias="state", default=None,)

from .classification_method import ClassificationMethod
from .sensitive_type_scope import SensitiveTypeScope
from .sensitive_type_source import SensitiveTypeSource

