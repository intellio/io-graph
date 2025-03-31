from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SensitiveType(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.sensitiveType"] = Field(alias="@odata.type",)
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
