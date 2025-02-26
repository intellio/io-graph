from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ParseExpressionResponse(BaseModel):
	error: Optional[PublicError] = Field(default=None,alias="error",)
	evaluationResult: list[Optional[str]] = Field(alias="evaluationResult",)
	evaluationSucceeded: Optional[bool] = Field(default=None,alias="evaluationSucceeded",)
	parsedExpression: Optional[AttributeMappingSource] = Field(default=None,alias="parsedExpression",)
	parsingSucceeded: Optional[bool] = Field(default=None,alias="parsingSucceeded",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .public_error import PublicError
from .attribute_mapping_source import AttributeMappingSource

